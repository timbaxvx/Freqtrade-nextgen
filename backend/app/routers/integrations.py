from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..dependencies import get_db
from ..security import get_current_active_user, has_role

router = APIRouter(prefix="/integrations", tags=["integrations"])

@router.post("/accounts", response_model=schemas.Account, status_code=status.HTTP_201_CREATED)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_account = models.Account(**account.dict(), owner_id=current_user.id)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

@router.get("/accounts", response_model=List[schemas.Account])
def list_accounts(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    return db.query(models.Account).filter(models.Account.owner_id == current_user.id).all()

@router.get("/accounts/{account_id}", response_model=schemas.Account)
def get_account(account_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_account = db.query(models.Account).filter(models.Account.id == account_id, models.Account.owner_id == current_user.id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.put("/accounts/{account_id}", response_model=schemas.Account)
def update_account(account_id: int, account: schemas.AccountCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_account = db.query(models.Account).filter(models.Account.id == account_id, models.Account.owner_id == current_user.id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    for key, value in account.dict().items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return db_account

@router.delete("/accounts/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_account(account_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    db_account = db.query(models.Account).filter(models.Account.id == account_id, models.Account.owner_id == current_user.id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    db.delete(db_account)
    db.commit()
    audit_log = models.AuditLog(user_id=current_user.id, action="Account Deleted", details=f"Account {db_account.name} deleted by {current_user.email}.")
    db.add(audit_log)
    db.commit()
    return

@router.post("/bybit/connect")
async def connect_bybit(api_key: str = Body(..., embed=True), api_secret: str = Body(..., embed=True), current_user: models.User = Depends(get_current_active_user)):
    # Placeholder for Bybit API connection and OAuth flow
    # In a real application, you would validate credentials and store them securely
    return {"message": "Bybit connection initiated (placeholder)"}

@router.post("/binance/connect")
async def connect_binance(api_key: str = Body(..., embed=True), api_secret: str = Body(..., embed=True), current_user: models.User = Depends(get_current_active_user)):
    # Placeholder for Binance API connection and OAuth flow
    # In a real application, you would validate credentials and store them securely
    return {"message": "Binance connection initiated (placeholder)"}

@router.post("/telegram/connect")
async def connect_telegram(bot_token: str = Body(..., embed=True), chat_id: str = Body(..., embed=True), current_user: models.User = Depends(get_current_active_user)):
    # Placeholder for Telegram API connection and webhook setup
    # In a real application, you would validate the token and set up webhooks
    return {"message": "Telegram connection initiated (placeholder)"}