from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..dependencies import get_db
from ..security import get_current_user

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.post("/", response_model=schemas.Notification, status_code=status.HTTP_201_CREATED)
def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_notification = models.Notification(**notification.dict(), user_id=current_user.id)
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

@router.get("/", response_model=List[schemas.Notification])
def list_notifications(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return db.query(models.Notification).filter(models.Notification.user_id == current_user.id).all()

@router.get("/{notification_id}", response_model=schemas.Notification)
def get_notification(notification_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id, models.Notification.user_id == current_user.id).first()
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification

@router.put("/{notification_id}", response_model=schemas.Notification)
def update_notification(notification_id: int, notification: schemas.NotificationCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id, models.Notification.user_id == current_user.id).first()
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    for key, value in notification.dict().items():
        setattr(db_notification, key, value)
    db.commit()
    db.refresh(db_notification)
    return db_notification

@router.delete("/{notification_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_notification(notification_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id, models.Notification.user_id == current_user.id).first()
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    db.delete(db_notification)
    db.commit()
    return