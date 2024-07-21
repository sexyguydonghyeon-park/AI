import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import cv2
import numpy as np

# .env 파일에서 환경 변수 로드
load_dotenv()

# 얼굴 인식 및 분류 함수
def detect_and_classify_faces(image_path):
    # Pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Load image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Dummy classification for demo purposes
    classifications = []
    for (x, y, w, h) in faces:
        face_region = gray[y:y+h, x:x+w]
        # For demonstration purposes, randomly assign a category
        category = np.random.choice(["할아버지", "할머니", "아버지", "어머니", "아들", "딸"])
        classifications.append((x, y, w, h, category))
    
    return classifications

# Streamlit 웹 애플리케이션 설정
st.title("이미지를 분류해 드릴게요")

# 사용자로부터 이미지 업로드 받기
uploaded_file = st.file_uploader("이미지를 업로드 해주세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 이미지 표시
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 이미지", use_column_width=True)
    
    # 이미지 저장
    if not os.path.exists("temp"):
        os.makedirs("temp")
    image_path = os.path.join("temp", uploaded_file.name)
    image.save(image_path)
    
    # 얼굴 인식 및 분류
    classifications = detect_and_classify_faces(image_path)
    
    if classifications:
        st.write("인식된 인물:")
        for (x, y, w, h, category) in classifications:
            st.write(f"위치: ({x}, {y}, {w}, {h}), 카테고리: {category}")
    else:
        st.write("인물 없음")
