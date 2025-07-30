from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..dependencies import get_db
from ..security import get_current_active_user, has_role

router = APIRouter(prefix="/audit_logs", tags=["audit_logs"], dependencies=[Depends(has_role(["admin"]))])

@router.get("/", response_model=List[schemas.AuditLog])
def list_audit_logs(db: Session = Depends(get_db)):
    return db.query(models.AuditLog).order_by(models.AuditLog.timestamp.desc()).all()

@router.get("/{log_id}", response_model=schemas.AuditLog)
def get_audit_log(log_id: int, db: Session = Depends(get_db)):
    db_log = db.query(models.AuditLog).filter(models.AuditLog.id == log_id).first()
    if db_log is None:
        raise HTTPException(status_code=404, detail="Audit log not found")
    return db_log