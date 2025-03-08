# app/services/ai_service.py
# AI 분석 및 추천 관련 서비스 로직을 통합하는 모듈입니다.
from app.ai_models import food_classifier, recommendation

def analyze_food_image(image_path: str):
    """
    음식 이미지를 분석하여 태그를 반환합니다.
    :param image_path: 이미지 파일 경로
    :return: 분석 결과 (예: {"tag": "Pizza"})
    """
    return food_classifier.classify_food(image_path)

def generate_recommendations(user_data):
    """
    사용자 데이터를 기반으로 맞춤 추천을 생성합니다.
    현재는 스텁 함수를 호출하지만, 추후 자체 개발 알고리즘으로 교체할 예정입니다.
    :param user_data: 사용자의 음식 기록, 태그, 평점 등
    :return: 추천 결과 리스트
    """
    return recommendation.get_custom_recommendations(user_data)
