import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="벽돌깨기 게임", layout="wide")

# 1. 제목을 컬럼(구역)을 나누기 전에 '전체 화면' 너비에서 먼저 출력합니다.
# white-space: nowrap; 을 추가하여 절대 두 줄로 나뉘지 않게 강제합니다.
st.markdown("<h1 style='text-align: center; white-space: nowrap; margin-bottom: 20px;'>Ultimate Master Brick Breaker</h1>", unsafe_allow_html=True)

# 2. 화면을 3개의 구역으로 나누어 게임 화면만 가운데 배치합니다.
# 비율을 1 : 1.5 : 1 로 유지
col1, col2, col3 = st.columns([1, 1.5, 1])

# 가운데 구역(col2)에 게임 렌더링
with col2:
    # HTML 파일 읽기
    with open("ultimate_master_brick_breaker.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    # 하단 텍스트까지 잘리지 않게 height를 넉넉하게 650으로 설정
    components.html(html_code, width=420, height=650, scrolling=False)
