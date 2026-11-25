import streamlit as st

st.title("🧴 스킨케어 추천기")

# [리스트] 피부 고민 목록
concerns = ["여드름/트러블", "속건조", "모공/피지", "홍조/민감성"]


# [함수 + if-elif-else] 고민별 추천 성분과 루틴 반환
def get_care(concern):
    if concern == "여드름/트러블":
        return "살리실산, 시카", ["약산성 세안", "시카 토너", "진정 젤"]
    elif concern == "속건조":
        return "히알루론산, 세라마이드", ["미온수 세안", "수분 토너", "보습 크림"]
    elif concern == "모공/피지":
        return "나이아신아마이드, 클레이", ["클레이 팩", "나이아신아마이드 세럼", "가벼운 로션"]
    else:
        return "판테놀, 어성초", ["저자극 세안", "진정 패드", "판테놀 크림"]


# 1. 입력
name = st.text_input("이름", placeholder="예: 홍길동")
memo = st.text_area("피부 고민 메모", height=80)
budget = st.slider("예산 (만 원)", 1, 15, 3)

# 2. 선택 위젯
concern = st.selectbox("피부 고민 선택", concerns)
extra = st.multiselect("추가 케어", ["진정", "보습", "각질", "선케어"])
mode = st.segmented_control("보기 방식", ["간단히 보기", "자세히 보기"], default="자세히 보기")
alarm = st.toggle("루틴 알림", value=True)

ingredient, routine = get_care(concern)
result = f"이름: {name}\n고민: {concern}\n성분: {ingredient}\n예산: {budget}만 원"

# 3. 버튼 & 다운로드
if st.button("추천받기", type="primary"):
    st.write(f"**{name}님 추천 성분:** {ingredient}")
    if mode == "자세히 보기":
        # [for 반복문] 루틴 출력
        for i, step in enumerate(routine, start=1):
            st.write(f"{i}단계: {step}")
        if extra:
            st.write("추가 케어:", ", ".join(extra))
        if memo:
            st.info(memo)
    if alarm:
        st.success("아침·저녁 루틴을 잊지 마세요!")

st.download_button("결과 다운로드", data=result, file_name="skincare.txt")
