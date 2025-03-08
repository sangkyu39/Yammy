# app/models/groups.py
# 그룹(커뮤니티) 정보를 저장하는 모델입니다.
import uuid
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 그룹 이름
    name = Column(String(100), nullable=False)
    # 그룹 생성자 (users 테이블과 연결)
    owner_id = Column(UUID, nullable=False)
    # 그룹 생성일
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
