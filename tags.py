import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import openai

# .env 파일에서 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

# OpenAI GPT-3.5 모델 호출 함수
def generate_quote(image_description):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a poetic quote or phrase related to this description: {image_description}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Streamlit 웹 애플리케이션 설정
st.title("이미지에 대한 감성적인 글귀 생성기")

# 사용자로부터 이미지 업로드 받기
uploaded_file = st.file_uploader("이미지를 업로드 해주세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 이미지 표시
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 이미지", use_column_width=True)
    
    # 이미지 설명 입력받기
    image_description = st.text_input("이미지에 대한 설명을 입력해주세요 (예: 아름다운 바다 풍경)")

    # 버튼을 누르면 OpenAI 호출
    if st.button("글귀 생성"):
        if image_description:
            # OpenAI 모델 호출하여 글귀 생성
            quote = generate_quote(image_description)
            
            # 생성된 글귀 출력
            st.write("생성된 글귀:")
            st.write(quote)
        else:
            st.write("이미지에 대한 설명을 입력해 주세요.")
