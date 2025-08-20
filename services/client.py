import os
from pathlib import Path
from dotenv import load_dotenv
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForCausalLM
from transformers import pipeline
from openai import OpenAI

# 환경변수 로드
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
CLASSIFIER_MODEL = os.getenv("CLASSIFIER_MODEL") if os.getenv("CLASSIFIER_MODEL") else "models/classifier_model/models--Jinuuuu--KoELECTRA_fine_tunning_emotion/snapshots/f3b1c1b572dd555048ce2150e3b77033222ff990"
GENERATOR_MODEL = os.getenv("GENERATOR_MODEL") if os.getenv("GENERATOR_MODEL") else "openai/gpt-oss-20b"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class classifier_model:
    def __init__(self, model_path):
        self.classifier = pipeline(
            "text-classification",
            model=CLASSIFIER_MODEL,
            tokenizer=CLASSIFIER_MODEL,
            device=device)
        self.labels = ["화남", "불안", "수치심", "기쁨", "마음 아픔", "슬픔"]
    
    def classify(self, text):
        result = self.classifier(text)
        print(f"classifier result: {result}")
        emotion = result[0]['label']

        return emotion
    
class generator_model:
    def __init__(self):
        self.client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")

    def generate(self, messages, emotion):
        system_prompt = f"""당신은 사람 감정에 따라 대화할 수 있는 상담사입니다.
사용자 감정은 {emotion}입니다.

# 행동 지시사항
- 사용자의 감정에 따라 적절한 대답을 해주세요.
- 사용자에게 친절하고 예의바르게 대답해주세요.
- 사용자의 감정을 이해하고 공감해주세요."""
        try:
            model_name = GENERATOR_MODEL
            response = self.client.chat.completions.create(
                model=GENERATOR_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": messages}
                ]
            )
            result = response.choices[0].message.content

            print(result)

            return result

        except Exception as e:
            print(f"Error generating response: {e}")
            return None

# 파이프라인으로 수정으로 코드 수정
# class classifier_model:
#     def __init__(self, model_path):
#         print(f"분류 모델 호출: {CLASSIFIER_MODEL}")
#         self.model = AutoModelForSequenceClassification.from_pretrained(CLASSIFIER_MODEL, cache_dir=model_path).to(device)
#         self.tokenizer = AutoTokenizer.from_pretrained(CLASSIFIER_MODEL, cache_dir=model_path)
#         self.labels = ["화남", "불안", "수치심", "기쁨", "마음 아픔", "슬픔"]
    
#     def classify(self, text):
#         inputs = self.tokenizer(
#             text,
#             return_tensors="pt",
#             padding=True,
#             truncation=True,
#             max_length=512,
#         )

#         with torch.no_grad():
#             outputs = self.model(**inputs.to(device))
        
#         probs = torch.softmax(outputs.logits, dim=1)
#         predicted_class = torch.argmax(probs, dim=1)
        
#         print(f"분류 결과: {self.labels[predicted_class]}")

#         return self.labels[predicted_class]

# class generator_model:
#     def __init__(self, model_path):
#         print(f"생성 모델 호출: {GENERATOR_MODEL}")
#         model = AutoModelForCausalLM.from_pretrained(GENERATOR_MODEL, cache_dir=model_path).to(device)
#         tokenizer = AutoTokenizer.from_pretrained(GENERATOR_MODEL, cache_dir=model_path)

#     def generate(self, text):
#         inputs = self.tokenizer(
#             text,
#             return_tensors="pt",
#             padding=True,
#             truncation=True,
#             max_length=512,
#         )

#         with torch.no_grad():
#             outputs = self.model.generate(**inputs.to(device))
        
#         response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
#         print(f"생성 결과: {response}")

#         return response