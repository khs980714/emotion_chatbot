# 1. 환경 세팅
## 1-1. pip 사용시
### 가상환경 설치
`python -m venv .venv`

### 가상환경 세팅
`.venv\Scripts\activate`

### 의존성 라이브러리 설치
`pip install -r ./requirements.txt`

### torch cpu 버전일 경우
`pip install torch torchvision`

### torch cuda 12.8 버전일 경우
`pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128`

---

## 1-2. uv 사용시
### 가상환경 설치
`uv venv .venv`

### 가상환경 세팅
`.venv\Scripts\activate`

### 의존성 라이브러리 설치
`uv pip install -r ./requirements.txt`

### torch cpu 버전 설치
`uv pip install torch torchvision`

### torch cuda12.8 버전 설치
`uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128`

---

# 2. 프로젝트에 .env 파일 생성
```
HF_TOKEN=허깅페이스토큰
CLASSIFIER_MODEL=Jinuuuu/KoELECTRA_fine_tunning_emotion
GENERATION_MODEL=openai/gpt-oss-20b

```

# 3. LM Studio 세팅
<img width="323" height="238" alt="image" src="https://github.com/user-attachments/assets/afa8bb81-9d26-4b4a-8446-1dcdc989e515" />

# 4. streamlit 실행
`streamlit run main.py`