# app/models/users.py
# 사용자 정보를 저장하는 모델입니다.
import uuid
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class User(Base):
    __tablename__ = "users"

    # UUID를 기본 키로 사용합니다.
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 사용자 닉네임 (고유)
    username = Column(String(50), unique=True, nullable=False)
    # 사용자 이메일 (고유)
    email = Column(String(100), unique=True, nullable=False)
    # 해싱된 비밀번호
    password_hash = Column(String(255), nullable=False)
    # 프로필 이미지 URL (클라우드 스토리지에 업로드된 이미지)
    profile_image = Column(String, nullable=True)
    # 계정 생성일
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
