# app/routes/food_logs.py
# 음식 기록의 생성, 조회, 수정, 삭제 API 엔드포인트
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models.food_logs import FoodLog
from app.schemas import food_log_schema

router = APIRouter()

def get_db():
    """
    데이터베이스 세션 반환 의존성 함수.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=food_log_schema.FoodLogResponse)
def create_food_log(food_log: food_log_schema.FoodLogCreate, db: Session = Depends(get_db)):
    """
    새로운 음식 기록을 생성합니다.
    """
    new_log = FoodLog(
        user_id=food_log.user_id,
        title=food_log.title,
        content=food_log.content,
        image_url=food_log.image_url,
        rating=food_log.rating,
        tags=food_log.tags,
        visibility=food_log.visibility
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

@router.get("/{user_id}", response_model=list[food_log_schema.FoodLogResponse])
def get_user_food_logs(user_id: str, db: Session = Depends(get_db)):
    """
    특정 사용자의 모든 음식 기록을 조회합니다.
    """
    logs = db.query(FoodLog).filter(FoodLog.user_id == user_id).all()
    return logs
