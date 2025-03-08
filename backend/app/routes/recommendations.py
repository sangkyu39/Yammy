# app/routes/recommendations.py
# 추천 API 엔드포인트: 사용자 맞춤형 추천 결과 반환
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models.recommendations import Recommendation
from app.schemas import recommendation_schema
from app.ai_models import recommendation as ai_recommendation

router = APIRouter()

def get_db():
    """
    데이터베이스 세션 반환 함수.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}", response_model=list[recommendation_schema.RecommendationResponse])
def get_recommendations(user_id: str, db: Session = Depends(get_db)):
    """
    사용자에게 추천된 음식 기록 목록을 반환합니다.
    현재는 AI 스텁을 호출하거나 DB에서 직접 조회하는 예시입니다.
    """
    # TODO: 자체 추천 AI 알고리즘 연동 후 결과 반환
    # 아래는 임시로 DB에서 추천 정보를 조회하는 예시
    recommendations = db.query(Recommendation).filter(Recommendation.user_id == user_id).all()
    return recommendations
