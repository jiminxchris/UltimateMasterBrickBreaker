import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정
st.set_page_config(page_title="벽돌깨기 게임", layout="wide")

# 제목 (한 줄로 표시)
st.markdown("<h1 style='text-align: center; white-space: nowrap; margin-bottom: 20px;'>Ultimate Master Brick Breaker</h1>", unsafe_allow_html=True)

# 화면을 3개의 구역으로 나누어 중앙 정렬
col1, col2, col3 = st.columns([1, 1.5, 1])

with col2:
    # HTML 파일 읽기
    with open("ultimate_master_brick_breaker.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    # Streamlit 금고(Secrets)에서 안전하게 키 꺼내기
    # (코드가 깃허브에 올라가도 이 키 값은 보이지 않습니다)
    try:
        real_bin_id = st.secrets["BIN_ID"]
        real_api_key = st.secrets["API_KEY"]
    except FileNotFoundError:
        # 로컬 테스트 시 에러 방지용 임시 텍스트
        real_bin_id = "로컬_테스트_BIN"
        real_api_key = "로컬_테스트_KEY"

    # HTML 내용 중 가짜 글자(__BIN_ID__)를 진짜 키로 바꿔치기 (치환)
    html_code = html_code.replace("__BIN_ID__", real_bin_id)
    html_code = html_code.replace("__API_KEY__", real_api_key)

    # 완성된 코드를 화면에 렌더링
    components.html(html_code, width=420, height=650, scrolling=False)
