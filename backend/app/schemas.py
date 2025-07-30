from pydantic import BaseModel
from typing import List, Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_2fa_enabled: bool
    two_factor_secret: Optional[str] = None
    role_id: int

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

class BotBase(BaseModel):
    name: str
    status: str
    strategy_id: int
    account_id: int

class BotCreate(BotBase):
    pass

class Bot(BotBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class StrategyBase(BaseModel):
    name: str
    type: str
    content: str

class StrategyCreate(StrategyBase):
    pass

class Strategy(StrategyBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class TradeBase(BaseModel):
    symbol: str
    entry_price: float
    exit_price: Optional[float] = None
    amount: float
    trade_type: str
    status: str
    pnl: Optional[float] = None

class TradeCreate(TradeBase):
    pass

class Trade(TradeBase):
    id: int
    bot_id: int

    class Config:
        orm_mode = True

class AccountBase(BaseModel):
    name: str
    exchange: str
    api_key: str
    api_secret: str

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class NotificationBase(BaseModel):
    message: str
    type: str
    is_read: bool

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class AuditLogBase(BaseModel):
    action: str
    details: Optional[str] = None

class AuditLogCreate(AuditLogBase):
    pass

class AuditLog(AuditLogBase):
    id: int
    user_id: Optional[int] = None

    class Config:
        orm_mode = True