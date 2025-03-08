# app/models/feed.py
# 피드에 표시될 음식 기록 정보를 관리하는 모델입니다.
import uuid
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class Feed(Base):
    __tablename__ = "feed"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 피드를 조회하는 사용자 ID
    user_id = Column(UUID, nullable=False)
    # 표시할 음식 기록 ID
    food_log_id = Column(UUID, nullable=False)
    # 기록 출처: friend, recommendation, group 등
    source_type = Column(String, nullable=False)
    # 피드 항목 생성일
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
