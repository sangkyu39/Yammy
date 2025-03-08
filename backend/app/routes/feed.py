# app/routes/feed.py
# 피드 API 엔드포인트: 친구의 기록, 추천 기록, 그룹 기록 등을 혼합하여 반환합니다.
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.database import SessionLocal
from app.models.feed import Feed
from app.schemas import feed_schema

router = APIRouter()

def get_db():
    """
    DB 세션 반환 함수.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}", response_model=list[feed_schema.FeedResponse])
def get_feed(user_id: str, db: Session = Depends(get_db)):
    """
    특정 사용자의 피드(친구, 추천, 그룹 기록)를 반환합니다.
    """
    feed_items = db.query(Feed).filter(Feed.user_id == user_id).all()
    return feed_items
