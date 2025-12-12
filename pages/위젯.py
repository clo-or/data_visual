import streamlit as st

# : blue [사용자 입력]

## orange : [텍스트 입력]
text = st.text_input('여기에 텍스트를 입력하세요')
st.write(f'입력된 텍스트: {text}')

### :orange[숫자 입력]
number = st.number_input('여기에 숫자를 입력하세요')
st.write(f'입력된 숫자: {number}')

### : orange[날짜 입력]
date = st.date_input('날짜를 선택하세요')
st.write(f'선택된 날짜: {date}')

## : orange [시간 입력]
time = st.time_input('시간을 선택하세요')
st.write(f'선택된 시간: {time}')

### : orange[파일 업로드]
file = st.file_uploader('파일을 업로드하세요')

# 파일을 임시적으로 사용하는 방법
if file:
    st.write(f'업로드된 파일: {file.name}')

    # 파일을 별도로 저장하는 방법
    import os
    # 파일을 저장할 경로 지정
    file_path = os.path.join('../data/', file.name)
    # 파일 저장
    with open(file_path, 'wb') as f:  # 'wb'는 바이너리 쓰기 모드
        f.write(file.getbuffer())
    st.success(f'파일이 저장되었습니다: {file_path}')

# :blue[위젯]

## :orange [기본 버튼: st.button()]
button = st.button('일반 버튼')
if button:
    st.write('버튼이 클릭되었습니다.')

primary_button = st.button('주요 버튼', type='primary')
if primary_button:
    st.write('주요 버튼이 클릭되었습니다.')

### : orange [다운로드 버튼: st.download_button()]
with open("./data/python.png", "rb") as file:
    st.download_button(
        label='이미지 파일 다운로드',  # 버튼 라벨
        data=file,                    # 다운로드할 파일 경로
        file_name='image.png',        # 다운로드 파일명
        mime='image/png'              # 파일 형식
    )

### :orange [피드백 버튼: st.feedback()]
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]} star(s)을 선택하였습니다.")

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]}을 선택하였습니다.")

### : orange [링크 버튼: st.link_button()]
st.link_button("갤러리 링크", "https://streamlit.io/gallery")

## : orange [체크박스]
check = st.checkbox('여기를 체크하세요')
if check:
    st.write('체크되었습니다.')

## : orange [라디오 버튼]
radio = st.radio('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(radio + '가 선택되었습니다.')

### : orange [셀렉트 박스]
select = st.selectbox('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(select + '가 선택되었습니다.')

### : orange [멀티 셀렉트 박스]
multi = st.multiselect('여기에서 여러 값을 선택하세요', ['선택 1', '선택 2', '선택 3'])
st.write(f'{type(multi)=}, {multi}가 선택되었습니다.')

# 슬라이더는 선택된 값을 반환
## : orange [슬라이더]
slider = st.slider('여기에서 값을 선택하세요', 0, 100, 50)
st.write(f'현재의 값은 {slider} 입니다.')

## orange [선택 슬라이더]
range_slider = st.select_slider('여기에서 값을 선택하세요', options=range(101), value=(25, 75))
st.write(f'현재의 값은 {range_slider} 입니다.')

## :orange[컬러 피커]
color = st.color_picker('색을 선택하세요', '#00f900')
st.write(f'선택된 색은 {color} 입니다.')

### : orange [프로그레스 바]
import time
button1 = st.button('실시')  # 버튼은 클릭 여부를 반환
if button1:
    progress = st.progress(0)
    for i in range(101):
        progress.progress(i)
        if i % 20 == 0:
            st.write(f'진행 상태 : {i}%')
        time.sleep(0.05)

## :orange[스피너]
button2 = st.button('로드')  # 버튼은 클릭 여부를 반환
if button2:
    with st.spinner('로딩 중입니다...'):
        time.sleep(3)
    st.success('로딩 완료!')

## :orange [풍선 애니메이션]
button4 = st.button('풍선을 띄워보세요')  # 버튼은 클릭 여부를 반환
if button4:
    st.balloons()  # 풍선 애니메이션 출력

## : orange[눈 애니메이션]
button5 = st.button('눈을 내려 보세요')  # 버튼은 클릭 여부를 반환
if button5:
    st.snow()  # 눈 애니메이션 출력
