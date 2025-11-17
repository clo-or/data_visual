import streamlit as st
import streamlit as st

st.title("Streamlit 설치 확인")
st.write("Streamlit이 정상적으로 실행되고 있습니다!")

number = st.number_input("숫자를 입력해보세요", 0, 100)
st.write("입력한 값:", number)