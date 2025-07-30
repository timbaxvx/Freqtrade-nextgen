from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..dependencies import get_db
from ..security import get_current_active_user, has_role

router = APIRouter(prefix="/admin", tags=["admin"], dependencies=[Depends(has_role(["admin"]))])

@router.post("/roles", response_model=schemas.Role, status_code=status.HTTP_201_CREATED)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    db_role = models.Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@router.get("/roles", response_model=List[schemas.Role])
def list_roles(db: Session = Depends(get_db)):
    return db.query(models.Role).all()

@router.put("/users/{user_id}/role", response_model=schemas.User)
def update_user_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_role = db.query(models.Role).filter(models.Role.id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    db_user.role_id = role_id
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users", response_model=List[schemas.User])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()