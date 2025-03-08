# app/routes/users.py
# 사용자 관련 API 엔드포인트 (회원가입, 프로필 조회 등)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models.users import User
from app.schemas import user_schema

router = APIRouter()

def get_db():
    """
    데이터베이스 세션을 반환하는 의존성 함수입니다.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    """
    신규 사용자를 생성하는 API입니다.
    """
    # 사용자 생성 전 중복 여부 확인 (예시)
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=user.password_hash,  # 실제 서비스에서는 해싱 필수
        profile_image=user.profile_image
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
