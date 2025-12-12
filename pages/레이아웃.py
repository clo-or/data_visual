import streamlit as st
import os

# --- 레이아웃 설정 ---

st.markdown('### :orange[컬럼: st.columns()]')
col_1, col_2, col_3 = st.columns([1, 2, 1])  # 1:2:1 비율로 컬럼 나눔

with col_1:
    st.write('1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
    st.write('## 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])

with col_3:
    st.write('## 3번 컬럼')
    st.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])


# --- 탭 설정 ---

st.markdown('## :orange[탭: st.tabs()]')
tab_1, tab_2, tab_3 = st.tabs(['Python', 'R', 'Julia'])

with tab_1:
    st.write("Python 예시")
    # 코드를 보여줄 때는 st.code()를 사용하고 문자열로 감싸야 합니다.
    st.code('''
import pandas as pd

df = pd.DataFrame(
    {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [24, 34, 45]
    }
)
    ''', language='python')

with tab_2:
    st.write("R 예시")
    st.code('''
df = data.frame(
    id = c(1, 2, 3),
    name = c('Alice', 'Bob', 'Charlie'),
    age = c(24, 34, 45)
)
    ''', language='r')

with tab_3:
    st.write("Julia 예시")
    st.code('''
using DataFrames

df = DataFrame(
    id = [1, 2, 3],
    name = ["Alice", "Bob", "Charlie"],
    age = [24, 34, 45]
)
    ''', language='julia')


# --- 확장 레이아웃 ---

st.markdown('### :orange[확장 레이아웃 : st.expander()]')
with st.expander('확장 레이아웃'):
    st.write('이곳은 확장 레이아웃입니다.')
    st.write('확장 레이아웃은 특정 컨텐츠를 숨기거나 보여줄 때 사용됩니다.')


# --- 사용자 입력 ---

st.markdown('## :blue[사용자 입력]')

st.markdown('### :orange[텍스트 입력]')
text = st.text_input('여기에 텍스트를 입력하세요')
st.write(f'입력된 텍스트: {text}')

st.markdown('### :orange[숫자 입력]')
number = st.number_input('여기에 숫자를 입력하세요', value=0)
st.write(f'입력된 숫자: {number}')

st.markdown('### :orange[날짜 입력]')
date = st.date_input('날짜를 선택하세요')
st.write(f'선택된 날짜: {date}')

st.markdown('### :orange[시간 입력]')
time = st.time_input('시간을 선택하세요')
st.write(f'선택된 시간: {time}')


# --- 파일 업로드 ---

st.markdown('### :orange[파일 업로드]')
file = st.file_uploader('파일을 업로드하세요')

# 파일을 임시적으로 사용하는 방법
if file:
    st.write(f'업로드된 파일: {file.name}')

    # 파일을 별도로 저장하는 방법
    # 저장할 디렉토리가 없으면 생성 (에러 방지)
    save_dir = '../data/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    file_path = os.path.join(save_dir, file.name)
    
    # 파일 저장
    with open(file_path, 'wb') as f:  # 'wb'는 바이너리 쓰기 모드
        f.write(file.getbuffer())
    st.success(f'파일이 저장되었습니다: {file_path}')

# 파일 하단에 있던 의미 없는 텍스트들(a, 그래프 등)은 제거했습니다.
