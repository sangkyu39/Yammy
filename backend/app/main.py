# app/main.py
# FastAPI 애플리케이션의 엔트리 포인트 파일입니다.
from fastapi import FastAPI
# 각 기능별 라우터들을 가져옵니다.
from app.routes import users, food_logs, recommendations, groups, chat, feed, statistics
# 데이터베이스 초기화를 위한 함수를 가져옵니다.
from app.utils.database import init_db

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI(title="Food Journal API")

# 애플리케이션 시작 시 데이터베이스 초기화 (모든 모델 테이블 생성)
init_db()

# 각 라우터들을 등록합니다.
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(food_logs.router, prefix="/food-logs", tags=["Food Logs"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])
app.include_router(groups.router, prefix="/groups", tags=["Groups"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(feed.router, prefix="/feed", tags=["Feed"])
app.include_router(statistics.router, prefix="/statistics", tags=["Statistics"])

# 추가적으로 마이페이지 라우터 등을 등록할 수 있습니다.
