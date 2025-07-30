from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_2fa_enabled = Column(Boolean, default=False)
    two_factor_secret = Column(String, nullable=True)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")
    bots = relationship("Bot", back_populates="owner")
    strategies = relationship("Strategy", back_populates="owner")
    accounts = relationship("Account", back_populates="owner")
    notifications = relationship("Notification", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)

    users = relationship("User", back_populates="role")

class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, default="stopped") # e.g., "running", "stopped", "error"
    owner_id = Column(Integer, ForeignKey("users.id"))
    strategy_id = Column(Integer, ForeignKey("strategies.id"))
    account_id = Column(Integer, ForeignKey("accounts.id"))

    owner = relationship("User", back_populates="bots")
    strategy = relationship("Strategy", back_populates="bots")
    account = relationship("Account", back_populates="bots")
    trades = relationship("Trade", back_populates="bot")

class Strategy(Base):
    __tablename__ = "strategies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String) # e.g., "visual", "ai", "code"
    content = Column(String) # JSON or code content of the strategy
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="strategies")
    bots = relationship("Bot", back_populates="strategy")

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    bot_id = Column(Integer, ForeignKey("bots.id"))
    symbol = Column(String)
    entry_price = Column(Float)
    exit_price = Column(Float, nullable=True)
    amount = Column(Float)
    trade_type = Column(String) # e.g., "buy", "sell"
    status = Column(String) # e.g., "open", "closed"
    open_time = Column(DateTime(timezone=True), server_default=func.now())
    close_time = Column(DateTime(timezone=True), nullable=True)
    pnl = Column(Float, nullable=True)

    bot = relationship("Bot", back_populates="trades")

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    exchange = Column(String) # e.g., "bybit", "binance", "freqtrade"
    api_key = Column(String)
    api_secret = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="accounts")
    bots = relationship("Bot", back_populates="account")

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(String)
    type = Column(String) # e.g., "telegram", "email", "push"
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="notifications")

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True) # Nullable for system actions
    action = Column(String)
    details = Column(String, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="audit_logs")
