import cv2
import torch
import os
from ultralytics import YOLO

# YOLOv8 모델 로드 (학습된 모델 경로로 변경)
model = YOLO('./best.pt')

# 입력 및 출력 폴더 경로 설정
input_folder = './input'
output_folder = './output'

# 출력 폴더가 존재하지 않으면 생성
os.makedirs(output_folder, exist_ok=True)

# 입력 폴더의 모든 이미지 파일을 처리
for file_name in os.listdir(input_folder):
    if file_name.endswith(('.jpg', '.jpeg', '.png')):  # 이미지 파일만 처리
        image_path = os.path.join(input_folder, file_name)
        image = cv2.imread(image_path)

        # YOLOv8 모델을 사용하여 이미지에서 객체 검출
        results = model(image)

        # 결과에서 bounding box 정보를 얻어 이미지에 표시
        for result in results:  # 각 결과에 대해 반복
            boxes = result.boxes  # bounding box 정보 가져오기
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]  # bounding box 좌표
                conf = box.conf[0]  # confidence score
                cls = box.cls[0]  # 클래스 번호
                if conf > 0.5:  # confidence threshold
                    label = f'{model.names[int(cls)]} {conf:.2f}'
                    # Bounding box 그리기
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 0), 2)
                    # # 텍스트 표시
                    # cv2.putText(image, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)

        # 결과 이미지 저장
        output_image_path = os.path.join(output_folder, file_name)
        cv2.imwrite(output_image_path, image)

        # 처리된 이미지 파일 출력
        print(f"Processed image saved to {output_image_path}")
