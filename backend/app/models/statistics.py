# app/models/statistics.py
# 사용자의 음식 소비 패턴 통계 데이터를 저장하는 모델입니다.
import uuid
from sqlalchemy import Column, Integer, Float, JSON, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class Statistics(Base):
    __tablename__ = "statistics"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 통계를 집계할 사용자 ID
    user_id = Column(UUID, nullable=False)
    # 통계 대상 월 (1 ~ 12)
    month = Column(Integer, nullable=False)
    # 통계 대상 연도
    year = Column(Integer, nullable=False)
    # 해당 월의 총 음식 기록 수
    total_food_logs = Column(Integer, nullable=False)
    # 가장 많이 사용된 태그 목록 (JSON 배열 형식)
    top_tags = Column(JSON, nullable=True)
    # 해당 월의 평균 별점
    average_rating = Column(Float, nullable=True)
    # 자주 방문한 장소 목록 (JSON 배열 형식)
    top_places = Column(JSON, nullable=True)
    # 전월 대비 변화량 (JSON 형식)
    comparison_with_last_month = Column(JSON, nullable=True)
