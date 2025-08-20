# 메인 & chatbot 페이지

# 라이브러리 호출
import streamlit as st
import pandas as pd

# services 호출
from services import classifier_model, generator_model
from services import classifier_model_path, generator_model_path

def main():
    st.title("감성 챗봇 페이지")
    classifier = classifier_model(classifier_model_path)
    generator = generator_model()

    prompt = st.chat_input("Say something")
    if prompt:
        st.chat_message("user").markdown(prompt)
        emotion = classifier.classify(prompt)
        st.write(emotion)
        response = generator.generate(prompt, emotion)
        st.chat_message("assistant").markdown(response)

if __name__ == "__main__":
    main()