# 미디어 삽입

## 이미지: st.image()
# pages 폴더 기준 상위 data 폴더의 파일 경로
st.image("../data/heart_mask.png", use_container_width=True)


## 오디오: st.audio()
# st.audio("./After_You.mp3", format="audio/mpeg", loop=True)

## 동영상: st.video()
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # YouTube 링크
