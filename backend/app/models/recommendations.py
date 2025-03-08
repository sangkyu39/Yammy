# app/models/recommendations.py
# 사용자에게 추천된 음식 기록 정보를 저장하는 모델입니다.
import uuid
from sqlalchemy import Column, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 추천 받은 사용자 ID
    user_id = Column(UUID, nullable=False)
    # 추천된 음식 기록 ID
    food_log_id = Column(UUID, nullable=False)
    # 추천 점수 (0.0 ~ 1.0 사이)
    score = Column(Float, nullable=False)
    # 추천 생성일
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
