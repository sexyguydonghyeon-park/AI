import os
import streamlit as st
from dotenv import load_dotenv
import openai

# .env 파일에서 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv("CLIENT_ID")

# OpenAI GPT-3.5 Turbo 모델 호출 함수
def recommend_travel_spots(location):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 도움이 되는 어시스턴트입니다."},
            {"role": "user", "content": f"{location}에서 추천할 만한 여행지를 알려주세요."}
        ],
        max_tokens=400,  # max_tokens 값을 증가시킴
        temperature=0.7  # 출력의 다양성을 조정
    )
    return response.choices[0].message['content'].strip()

# Streamlit 웹 애플리케이션 설정
st.title("새 추억을 만들어보세요")

# 사용자로부터 지역 입력받기
location = st.text_input("여행지를 알고 싶은 지역을 입력해주세요 (예: 서울, 부산)")

# 버튼을 누르면 OpenAI 호출
if st.button("추억 생성하기"):
    if location:
        # OpenAI 모델 호출하여 여행지 추천
        travel_spots = recommend_travel_spots(location)
        
        # 추천된 여행지 출력
        st.write("추천된 여행지:")
        st.text_area("추천된 여행지 내용", travel_spots, height=200)  # 텍스트 영역에 출력
    else:
        st.write("여행지를 알고 싶은 지역을 입력해 주세요.")
