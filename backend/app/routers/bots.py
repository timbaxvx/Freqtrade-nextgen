from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List

from .. import schemas, models
from ..dependencies import get_db
from ..security import get_current_user

router = APIRouter(prefix="/bots", tags=["bots"])

@router.post("/", response_model=schemas.Bot, status_code=status.HTTP_201_CREATED)
def create_bot(bot: schemas.BotCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_bot = models.Bot(**bot.dict(), owner_id=current_user.id)
    db.add(db_bot)
    db.commit()
    db.refresh(db_bot)
    return db_bot

@router.get("/", response_model=List[schemas.Bot])
def list_bots(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    # Only return bots owned by the current user
    return db.query(models.Bot).filter(models.Bot.owner_id == current_user.id).all()

@router.get("/{bot_id}", response_model=schemas.Bot)
def get_bot(bot_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_bot = db.query(models.Bot).filter(models.Bot.id == bot_id, models.Bot.owner_id == current_user.id).first()
    if db_bot is None:
        raise HTTPException(status_code=404, detail="Bot not found")
    return db_bot

@router.put("/{bot_id}", response_model=schemas.Bot)
def update_bot(bot_id: int, bot: schemas.BotCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_bot = db.query(models.Bot).filter(models.Bot.id == bot_id, models.Bot.owner_id == current_user.id).first()
    if db_bot is None:
        raise HTTPException(status_code=404, detail="Bot not found")
    for key, value in bot.dict().items():
        setattr(db_bot, key, value)
    db.commit()
    db.refresh(db_bot)
    return db_bot

@router.delete("/{bot_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bot(bot_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_bot = db.query(models.Bot).filter(models.Bot.id == bot_id, models.Bot.owner_id == current_user.id).first()
    if db_bot is None:
        raise HTTPException(status_code=404, detail="Bot not found")
    db.delete(db_bot)
    db.commit()
    audit_log = models.AuditLog(user_id=current_user.id, action="Bot Deleted", details=f"Bot {db_bot.name} deleted by {current_user.email}.")
    db.add(audit_log)
    db.commit()
    return