import os
from pathlib import Path
from .client import classifier_model, generator_model
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / '.env')

HF_TOKEN = os.getenv("HF_TOKEN")
CLASSIFIER_MODEL = os.getenv("CLASSIFIER_MODEL")
GENERATOR_MODEL = os.getenv("GENERATOR_MODEL")

print("services 초기화")

# 모델 경로 지정
model_path = Path(__file__).parent.parent / "models"
classifier_model_path = model_path / "classifier_model"
generator_model_path = model_path / "generator_model"

print("모델 경로: ", model_path)

if not model_path.exists():
    print("모델 폴더 생성")
    model_path.mkdir(parents=True, exist_ok=True)

if not classifier_model_path.exists():
    print("분류 모델 폴더 생성")
    classifier_model_path.mkdir(parents=True, exist_ok=True)

if not generator_model_path.exists():
    print("생성 모델 폴더 생성")
    generator_model_path.mkdir(parents=True, exist_ok=True)