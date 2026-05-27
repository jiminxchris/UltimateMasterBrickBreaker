import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정 (선택 사항)
st.set_page_config(page_title="벽돌깨기 게임", layout="centered")

st.title("Ultimate Master Brick Breaker")

# HTML 파일 읽기
with open("ultimate_master_brick_breaker.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Streamlit 화면에 HTML 렌더링
# 게임 화면 크기(canvas)에 맞춰 width와 height를 넉넉하게 설정해 줍니다.
components.html(html_code, width=400, height=600, scrolling=False)
