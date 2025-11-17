import streamlit as st

st.title("서브페이지 1")
st.write("이것은 서브페이지 1입니다.")

# 음식 메뉴 추천
st.subheader("음식 메뉴 추천")
food_options = ["피자", "햄버거", "샐러드", "스시", "파스타", "떡볶이", "치킨", "라면"]
selected_food = st.selectbox("오늘의 음식 메뉴를 선택하세요:", food_options)
st.write("선택한 음식 메뉴:", selected_food)
