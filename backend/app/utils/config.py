# app/utils/config.py
# 애플리케이션 설정 및 환경 변수 관리를 위한 파일입니다.
import os
from dotenv import load_dotenv

# .env 파일이 있는 경우 불러옵니다.
load_dotenv()

# 데이터베이스 접속 정보
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/foodjournal")

# AWS S3 관련 설정 (이미지 업로드에 사용)
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "your_aws_access_key")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "your_aws_secret_key")
AWS_REGION = os.getenv("AWS_REGION", "your_aws_region")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "your_bucket_name")
