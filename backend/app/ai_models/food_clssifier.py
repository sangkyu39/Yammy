# app/ai_models/food_classifier.py
# 사전 학습된 ResNet 모델을 이용해 음식 이미지를 분류하는 예제 코드입니다.
import torch
from torchvision import transforms
from PIL import Image

# 사전 학습된 ResNet18 모델을 로드 (필요에 따라 커스터마이징)
model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
model.eval()  # 평가 모드로 설정

# 예시 음식 태그 목록 (추후 자체 데이터셋으로 재학습 예정)
food_labels = ["Pizza", "Burger", "Sushi", "Pasta", "Steak"]

def classify_food(image_path: str):
    """
    이미지 파일 경로를 받아 음식 태그를 분류합니다.
    :param image_path: 이미지 파일 경로
    :return: 분류 결과 딕셔너리 (예: {"tag": "Pizza"})
    """
    # 이미지 열기 및 RGB 모드로 변환
    image = Image.open(image_path).convert("RGB")
    # 전처리: 사이즈 조정, 중앙 자르기, Tensor 변환
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])
    input_tensor = preprocess(image).unsqueeze(0)  # 배치 차원 추가

    with torch.no_grad():
        output = model(input_tensor)
        # 모델 예측 결과 중 가장 높은 확률의 인덱스 선택
        prediction = torch.argmax(output, dim=1).item()

    # 실제 태그 목록과 매핑하여 결과 반환
    return {"tag": food_labels[prediction]}
