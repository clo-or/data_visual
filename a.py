import streamlit as st

st.set_page_config(
    page_title="하교수의 Streamlit",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("파이썬 프로그래밍 수업에 오신 것을 환영합니다!")
st.markdown("""
이 앱은 Streamlit 다중 페이지 예제입니다.  
사이드바에서 원하는 페이지를 선택하여 다양한 기능을 확인해보세요.
""")

st.image("main_illustration.png")  # 소개용 그림 등
