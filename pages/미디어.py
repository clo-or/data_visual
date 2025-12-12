import streamlit as st

# 미디어 삽입

## 동영상: st.video()
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # YouTube 링크

## 이미지: st.image()
# pages 폴더 기준 상위 data 폴더의 파일 경로
st.image("data/heart_mask.png", use_container_width=True)

## 오디오: st.audio()
# st.audio("./After_You.mp3", format="audio/mpeg", loop=True)

# 콜아웃

## 정보: st.info()
st.info('This is a purely informational message', icon="i")

### 경고: st.warning()
st.warning('This is a warning message', icon="A")

## 에러: st.error()
st.error('This is an error message', icon="")

#### 성공: st.success()
st.success('This is a success message', icon="")
