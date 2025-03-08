# app/utils/database.py
# SQLAlchemy를 사용해 데이터베이스 연결 및 세션, Base 객체를 설정합니다.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.utils.config import DATABASE_URL  # Supabase 연결 문자열 사용

# 데이터베이스 엔진 생성: Supabase의 PostgreSQL에 연결합니다.
engine = create_engine(DATABASE_URL)

# 데이터베이스 세션 생성기: 요청마다 새 세션을 생성합니다.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# 모든 모델이 상속할 기본 클래스 생성
Base = declarative_base()

def init_db():
    """
    모든 SQLAlchemy 모델을 임포트하여 데이터베이스에 테이블을 생성합니다.
    (프로젝트에서는 Alembic을 사용하여 마이그레이션하는 것이 좋습니다.)
    """
    from app.models import (
        users, food_logs, places, recommendations,
        feed, groups, group_members, group_posts,
        group_messages, statistics
    )
    Base.metadata.create_all(bind=engine)
