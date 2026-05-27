import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정 (전체 화면을 넓게 사용하도록 wide로 설정)
st.set_page_config(page_title="벽돌깨기 게임", layout="wide")

# 화면을 3개의 구역으로 나눕니다. (왼쪽 여백 : 가운데 게임 : 오른쪽 여백)
# 비율을 1 : 1.5 : 1 로 주어 가운데를 조금 더 넓게 씁니다.
col1, col2, col3 = st.columns([1, 1.5, 1])

# 가운데 컬럼(col2)에만 요소들을 렌더링합니다.
with col2:
    # 텍스트를 가운데 정렬하는 HTML 꼼수 적용
    st.markdown("<h2 style='text-align: center;'>Ultimate Master Brick Breaker</h2>", unsafe_allow_html=True)
    
    # HTML 파일 읽기
    with open("ultimate_master_brick_breaker.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    # 하단 텍스트까지 잘리지 않게 height를 650 정도로 넉넉하게 줍니다.
    components.html(html_code, width=420, height=650, scrolling=False)
