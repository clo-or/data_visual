import streamlit as st

'## : 일반 텍스트'
st.title('제목 : st.title()')

st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.markdown('# 마크다운 : st.markdown()')
st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

#: st.write()
st.write('# 마크다운 H1 : st.write()')
st.write('## 마크다운 H3 : st.write()')
st.write('')  # 빈 줄 추가

#: 색상이 있는 텍스트
st.write(':red[빨간색 텍스트]')
st.write(':blue[파란색 텍스트]')

### 코드 블록: st.code
st.code('print("Hello, World!")', language='python', line_numbers=True)

### 코드+결과: st.echo
with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = 'Chunghun Ha'
    st.write("Hello, Streamlit!", name)

### Latex 수식 작성: st.latex
st.latex(r'\int_a^b f(x)dx')

st.divider()  # 구분선

# abo 텍스트_미디어.py
# B: Streamlit Magic

# 마크다운 헤더3
st.markdown("### 마크다운 헤더3")

# 마크다운 목록
st.markdown("""
1. **굵게** 표시
2. *기울임* 표시
   - 목록2-1
   - 목록2-2
""")

# 마크다운 링크
st.markdown("[네이버](https://naver.com)")
st.markdown("[구글](https://google.com)")

# 마크다운 인용
st.markdown("> Streamlit은 데이터 앱을 쉽게 만들 수 있는 프레임워크입니다.")

# 마크다운 표
st.markdown("""
| 헤더1 | 헤더2 |
|-------|-------|
| 데이터1 | 데이터2 |
""")

# 마크다운 코드 블록
st.code("""
def hello_world():
    print("Hello, World!")
""", language='python')

# 미디어 삽입

## 이미지: st.image()
# pages 폴더 기준 상위 data 폴더의 파일 경로
st.image("../data/heart_mask.png", caption="파이썬 로고", use_container_width=True)


## 오디오: st.audio()
# st.audio("./After_You.mp3", format="audio/mpeg", loop=True)

## 동영상: st.video()
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # YouTube 링크

