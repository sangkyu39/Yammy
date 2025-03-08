# Dockerfile: Python 3.9 기반 이미지 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 전체 소스코드 복사
COPY . .

# FastAPI 기본 포트 8000 노출
EXPOSE 8000

# 컨테이너 시작 시 uvicorn 실행 (프로덕션에서는 Gunicorn+Uvicorn Worker 사용 권장)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
