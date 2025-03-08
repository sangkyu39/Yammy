# app/services/s3_upload.py
# AWS S3를 이용하여 이미지 파일을 업로드하는 유틸리티입니다.
import boto3
import os
from uuid import uuid4
from app.utils.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET_NAME

# boto3 S3 클라이언트 생성
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def upload_image(file_path: str, file_name: str = None) -> str:
    """
    이미지 파일을 S3 버킷에 업로드하고, 접근 가능한 URL을 반환합니다.
    :param file_path: 로컬에 저장된 이미지 파일 경로
    :param file_name: S3에 저장할 파일명 (없으면 UUID 기반 생성)
    :return: 업로드된 이미지의 URL
    """
    if not file_name:
        file_name = str(uuid4())
    # S3에 파일 업로드
    s3_client.upload_file(file_path, S3_BUCKET_NAME, file_name)
    # S3 URL 구성 (버킷 정책에 따라 Public URL 또는 Signed URL 사용)
    url = f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{file_name}"
    return url
