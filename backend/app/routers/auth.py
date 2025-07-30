from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import pyotp

from .. import schemas, models
from ..dependencies import get_db
from ..security import verify_password, create_access_token, get_password_hash, get_current_active_user

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, role_id=1) # Assign a default role_id, e.g., 1 for 'beginner'
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

from fastapi_limiter.depends import RateLimiter

@router.post("/token", response_model=schemas.Token, dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if user.is_2fa_enabled:
        if not form_data.scopes or "2fa" not in form_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="2FA required",
                headers={"WWW-Authenticate": "Bearer"},
            )
        totp = pyotp.TOTP(user.two_factor_secret)
        if not totp.verify(form_data.scopes[form_data.scopes.index("2fa") + 1]): # Assuming 2fa code is next scope
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid 2FA code",
                headers={"WWW-Authenticate": "Bearer"},
            )

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_active_user)):
    return current_user

@router.post("/2fa/generate", response_model=dict)
async def generate_2fa_secret(current_user: models.User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if current_user.is_2fa_enabled:
        raise HTTPException(status_code=400, detail="2FA is already enabled for this user")
    
    secret = pyotp.random_base32()
    current_user.two_factor_secret = secret
    db.commit()
    db.refresh(current_user)
    
    # In a real application, you would return a QR code URL here
    return {"secret": secret, "qr_code_url": f"otpauth://totp/FreqtradeNextGen:{current_user.email}?secret={secret}&issuer=FreqtradeNextGen"}

@router.post("/2fa/verify", response_model=schemas.User)
async def verify_2fa(code: str = Body(..., embed=True), current_user: models.User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not current_user.two_factor_secret:
        raise HTTPException(status_code=400, detail="2FA secret not generated")
    
    totp = pyotp.TOTP(current_user.two_factor_secret)
    if not totp.verify(code):
        raise HTTPException(status_code=400, detail="Invalid 2FA code")
    
    current_user.is_2fa_enabled = True
    db.commit()
    db.refresh(current_user)
    return current_user

@router.post("/2fa/disable", response_model=schemas.User)
async def disable_2fa(current_user: models.User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not current_user.is_2fa_enabled:
        raise HTTPException(status_code=400, detail="2FA is not enabled for this user")
    
    current_user.is_2fa_enabled = False
    current_user.two_factor_secret = None
    db.commit()
    db.refresh(current_user)
    audit_log = models.AuditLog(user_id=current_user.id, action="2FA Disabled", details=f"2FA disabled for user {current_user.email}.")
    db.add(audit_log)
    db.commit()
    return current_user