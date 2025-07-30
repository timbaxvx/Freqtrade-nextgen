from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..dependencies import get_db
from ..security import get_current_user

router = APIRouter(prefix="/strategies", tags=["strategies"])

@router.post("/", response_model=schemas.Strategy, status_code=status.HTTP_201_CREATED)
def create_strategy(strategy: schemas.StrategyCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_strategy = models.Strategy(**strategy.dict(), owner_id=current_user.id)
    db.add(db_strategy)
    db.commit()
    db.refresh(db_strategy)
    return db_strategy

@router.get("/", response_model=List[schemas.Strategy])
def list_strategies(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return db.query(models.Strategy).filter(models.Strategy.owner_id == current_user.id).all()

@router.get("/{strategy_id}", response_model=schemas.Strategy)
def get_strategy(strategy_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_strategy = db.query(models.Strategy).filter(models.Strategy.id == strategy_id, models.Strategy.owner_id == current_user.id).first()
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return db_strategy

@router.put("/{strategy_id}", response_model=schemas.Strategy)
def update_strategy(strategy_id: int, strategy: schemas.StrategyCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_strategy = db.query(models.Strategy).filter(models.Strategy.id == strategy_id, models.Strategy.owner_id == current_user.id).first()
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    for key, value in strategy.dict().items():
        setattr(db_strategy, key, value)
    db.commit()
    db.refresh(db_strategy)
    return db_strategy

@router.delete("/{strategy_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_strategy(strategy_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_strategy = db.query(models.Strategy).filter(models.Strategy.id == strategy_id, models.Strategy.owner_id == current_user.id).first()
    if db_strategy is None:
        raise HTTPException(status_code=404, detail="Strategy not found")
    db.delete(db_strategy)
    db.commit()
    audit_log = models.AuditLog(user_id=current_user.id, action="Strategy Deleted", details=f"Strategy {db_strategy.name} deleted by {current_user.email}.")
    db.add(audit_log)
    db.commit()
    return