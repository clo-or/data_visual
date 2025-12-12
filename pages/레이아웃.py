import streamlit as st

### : orange [컬럼: st.columns()]
col_1, col_2, col_3 = st.columns([1,2,1]) # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔

with col_1:
    st.write('1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
    st.write('## 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])  # 동일한 라디오 버튼을 생성
    # 사이드바에 이미 라디오 버튼이 생성되어 있기 때문에,
    # 여기서는 라디오 버튼의 내용을 변경해야 오류가 발생하지 않음

col_3.write('## 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])
# 사이드바에 이미 셀렉트박스가 생성되어 있기 때문에,
# 여기서는 셀렉트박스의 내용을 변경해야 오류가 발생하지 않음

## : orange [탭: st.tabs()]

# 탭인스턴스 생성. 3개의 탭을 생성
tab_1, tab_2, tab_3 = st.tabs(['Python', 'R', 'Julia'])

with tab_1:
    st.write(
        # python
        import pandas as pd

        df = pd.DataFrame(
            {
                'id': [1, 2, 3],
                'name': ['Alice', 'Bob', 'Charlie'],
                'age': [24, 34, 45]
            }
        )
    )

with tab_2:
    st.write(
        # r
        df = data.frame(
            id = c(1, 2, 3),
            name = c('Alice', 'Bob', 'Charlie'),
            age = c(24, 34, 45)
        )
    )

tab_3.write(
    # julia
    using DataFrames

    df = DataFrame(
        id = [1, 2, 3],
        name = ["Alice", "Bob", "Charlie"],
        age = [24, 34, 45]
    )
)

### : orange [확장 레이아웃 : st.expander()]
with st.expander('확장 레이아웃'):
    st.write('이곳은 확장 레이아웃입니다.')
    st.write('확장 레이아웃은 특정 컨텐츠를 숨기거나 보여줄 때 사용됩니다.')

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
    st.write(f'업로드된 파일: {file}')

# 파일을 별도로 저장하는 방법
import os
if file:
    # 파일을 저장할 경로 지정
    file_path = os.path.join('../data/', file.name)
    # 파일 저장
    with open(file_path, 'wb') as f:  # 'wb'는 바이너리 쓰기 모드
        f.write(file.getbuffer())
    st.success(f'파일이 저장되었습니다: {file_path}')
