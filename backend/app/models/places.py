# app/models/places.py
# 사용자가 방문한 장소(위치) 정보를 저장하는 모델입니다.
import uuid
from sqlalchemy import Column, String, Float, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.utils.database import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # 장소 이름 (음식점, 카페 등)
    name = Column(String(100), nullable=False)
    # 위도, 경도 정보 (PostGIS를 사용하는 경우 Geometry 타입을 사용할 수 있음)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    # 장소 주소
    address = Column(String, nullable=True)
    # 장소 등록일
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
