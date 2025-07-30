from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .routers import bots, strategies, analytics, auth, gpt, integrations, notifications, admin, ai_proxy, trading, websocket, audit_logs
from .database import Base, engine
import sentry_sdk
from fastapi_limiter import FastAPILimiter
import redis.asyncio as redis

sentry_sdk.init(
    dsn="YOUR_SENTRY_DSN", # Replace with your Sentry DSN
    traces_sample_rate=1.0,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    r = redis.from_url("redis://localhost", encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(r)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# For more secure headers, consider using FastAPI-Helmet or manually adding headers
# app.add_middleware(...


app.include_router(auth.router)
app.include_router(bots.router)
app.include_router(strategies.router)
app.include_router(analytics.router)
app.include_router(gpt.router)
app.include_router(integrations.router)
app.include_router(notifications.router)
app.include_router(admin.router)
app.include_router(ai_proxy.router)
app.include_router(trading.router)
app.include_router(websocket.router)
app.include_router(audit_logs.router)

# Placeholder for Plugin System: Dynamic loading of routers/modules


@app.get("/")
def read_root():
    return {"msg": "Freqtrade NextGen API"}