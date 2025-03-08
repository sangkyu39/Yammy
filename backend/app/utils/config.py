# app/utils/config.py
# 환경 변수 및 설정 값을 관리하는 모듈입니다.
import os
from dotenv import load_dotenv

# .env 파일이 존재하면 환경 변수를 로드합니다.
load_dotenv()

# Supabase PostgreSQL 연결 문자열 (sslmode=require로 보안 연결)
# 기본값은 Supabase 대시보드에서 제공하는 연결 정보를 입력합니다.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://food_user:your_password@db.supabase.co:5432/foodjournal?sslmode=require"
)

# AWS S3 설정 (이미지 업로드를 위한 클라우드 스토리지)
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "your_aws_access_key")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "your_aws_secret_key")
AWS_REGION = os.getenv("AWS_REGION", "your_aws_region")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "your_bucket_name")
