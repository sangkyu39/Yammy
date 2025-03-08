# app/models/group_members.py
# 그룹에 속한 멤버 정보를 저장하는 모델입니다.
import uuid
from sqlalchemy import Column, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class GroupMember(Base):
    __tablename__ = "group_members"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 그룹 ID (groups 테이블과 연결)
    group_id = Column(UUID, nullable=False)
    # 사용자 ID (users 테이블과 연결)
    user_id = Column(UUID, nullable=False)
    # 그룹 가입일
    joined_at = Column(TIMESTAMP, default=datetime.utcnow)
