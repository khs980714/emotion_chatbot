# 1. pip 사용시
## 가상환경 설치
`python -m venv .venv`

## 가상환경 세팅
`.venv\Scripts\activate`

## 의존성 라이브러리 설치
`pip install -r ./requirements.txt`

## torch cpu 버전일 경우
`pip install torch torchvision`

## torch cuda 12.8 버전일 경우
`pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128`

---

# 2. uv 사용시
## 가상환경 설치
`uv venv .venv`

## 가상환경 세팅
`.venv\Scripts\activate`

## 의존성 라이브러리 설치
`uv pip install -r ./requirements.txt`

## torch cpu 버전 설치
`uv pip install torch torchvision`

## torch cuda12.8 버전 설치
`uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128`

# 3. .env 파일 생성
```
HF_TOKEN=허깅페이스토큰
CLASSIFIER_MODEL=Jinuuuu/KoELECTRA_fine_tunning_emotion
GENERATION_MODEL=openai/gpt-oss-20b
```

### 추가로 알거라 생각하지만 streamlit을 처음 실행할 때 터미널에서 이메일 주소 치는거 나오는데 나오면 치고 아니면 그냥 해도 될거