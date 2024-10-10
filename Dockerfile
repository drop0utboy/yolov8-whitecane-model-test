# Python 3.8 기반 이미지
FROM python:3.8-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 업데이트 및 필수 패키지 설치 (libGL 포함)
RUN apt-get update && apt-get install -y \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 로컬에서 requirements.txt 파일을 컨테이너로 복사하고 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 컨테이너 진입 시 bash로 실행
CMD ["/bin/bash"]