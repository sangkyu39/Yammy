# app/utils/database.py
# SQLAlchemy를 사용하여 데이터베이스 연결, 세션, Base 객체를 설정합니다.
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 환경변수에서 DATABASE_URL을 가져오며, 기본값은 로컬 PostgreSQL로 설정합니다.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/foodjournal")

# SQLAlchemy 엔진 생성 (데이터베이스 연결)
engine = create_engine(DATABASE_URL)

# 데이터베이스 세션 생성기 (매 요청마다 새 세션 생성)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# 모든 모델이 상속할 베이스 클래스 생성
Base = declarative_base()

def init_db():
    """
    모든 모델을 임포트하여 데이터베이스에 테이블 생성
    Alembic과 연동하여 마이그레이션으로 대체할 수 있음.
    """
    # 모델들을 가져와서 테이블 생성 (import 순서 주의)
    from app.models import users, food_logs, places, recommendations, feed, groups, group_members, group_posts, group_messages, statistics
    Base.metadata.create_all(bind=engine)
