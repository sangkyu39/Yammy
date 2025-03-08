# app/models/group_posts.py
# 그룹 내에서 공유된 음식 기록 정보를 저장하는 모델입니다.
import uuid
from sqlalchemy import Column, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class GroupPost(Base):
    __tablename__ = "group_posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 그룹 ID (groups 테이블과 연결)
    group_id = Column(UUID, nullable=False)
    # 공유된 음식 기록 ID (food_logs 테이블과 연결)
    food_log_id = Column(UUID, nullable=False)
    # 공유한 사용자 ID (users 테이블과 연결)
    user_id = Column(UUID, nullable=False)
    # 공유일
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
