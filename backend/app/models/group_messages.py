# app/models/group_messages.py
# 그룹 내 실시간 채팅 메시지 기록을 저장하는 모델입니다.
import uuid
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class GroupMessage(Base):
    __tablename__ = "group_messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 채팅이 속한 그룹 ID
    group_id = Column(UUID, nullable=False)
    # 메시지를 보낸 사용자 ID
    user_id = Column(UUID, nullable=False)
    # 메시지 내용 (텍스트)
    message = Column(String, nullable=False)
    # (선택사항) 이미지 메시지 URL (클라우드 저장)
    image_url = Column(String, nullable=True)
    # 메시지 전송 시간
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
