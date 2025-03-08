# app/models/food_logs.py
# 사용자가 업로드한 음식 기록을 저장하는 모델입니다.
import uuid
from sqlalchemy import Column, String, Float, JSON, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class FoodLog(Base):
    __tablename__ = "food_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 음식 기록 작성자 (users 테이블과 연결)
    user_id = Column(UUID, nullable=False)
    # 음식 기록 제목
    title = Column(String(100), nullable=False)
    # 음식 기록 내용
    content = Column(String, nullable=True)
    # 이미지 URL (클라우드 스토리지에 업로드 후 URL 저장)
    image_url = Column(String, nullable=True)
    # 사용자가 부여한 별점
    rating = Column(Float, nullable=True)
    # AI가 자동 생성한 태그 (JSON 형식, 사용자가 수정 가능)
    tags = Column(JSON, nullable=True)
    # 공유 범위 (예: public, friends, private)
    visibility = Column(String, nullable=False, default="public")
    # 음식 기록 생성일
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
