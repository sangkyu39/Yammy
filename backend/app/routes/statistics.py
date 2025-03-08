# app/routes/statistics.py
# 통계 API 엔드포인트: 사용자의 음식 소비 패턴, 월별 통계 등 반환
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models.statistics import Statistics
from app.schemas import statistics_schema

router = APIRouter()

def get_db():
    """
    DB 세션 반환 함수.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}", response_model=statistics_schema.StatisticsResponse)
def get_user_statistics(user_id: str, db: Session = Depends(get_db)):
    """
    특정 사용자의 통계 데이터를 반환합니다.
    (예: 월별 기록, 평균 별점, 자주 방문한 장소 등)
    """
    stats = db.query(Statistics).filter(Statistics.user_id == user_id).first()
    if not stats:
        # 통계 데이터가 없으면 적절한 기본값 반환 또는 에러 처리
        return {}
    return stats
