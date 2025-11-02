import streamlit as st

# 페이지 제목 설정
st.title('🔢 규칙이 있는 함수 웹')


def add(a, b):
  
    result = a * b

    if result >= 9:
        #9보다 크거나 같으면 결과에서 9를 뺀다
        result = result - 9
    else:
        #9보다 작으면 결과를 그대로 반환
        pass

    return result


# 섹션 분리 (선택 사항)
st.markdown("---")

# 1. UI 화면 중앙 정렬을 위한 컨테이너 및 컬럼 사용
# 중앙 정렬을 완전히 보장하긴 어렵지만, 입력과 버튼을 보기 좋게 배치합니다.
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.header('계산기')
    
    # 인수로 받아들일 두 개의 숫자를 넣는 입력란 노출 (st.number_input 사용)
    num1 = st.number_input('첫 번째 숫자', value=0, step=1, key='num1')
    num2 = st.number_input('두 번째 숫자', value=0, step=1, key='num2')
    
    # 버튼 노출
    if st.button('결과 계산하기', use_container_width=True):
        # 2. 버튼 클릭 시 함수 호출 및 결과 계산
        try:
            result_value = add(num1, num2)
            
            # 계산 결과를 세션 상태에 저장하여 버튼 아래에 노출될 수 있도록 함
            st.session_state['result'] = result_value
            st.session_state['calculated'] = True
        except Exception as e:
            # 예외 처리 (필요한 경우)
            st.error(f"계산 중 오류가 발생했습니다: {e}")
            st.session_state['calculated'] = False

# 3. 함수가 리턴한 값을 버튼 아래에 큰 숫자로 노출
# 'calculated' 상태가 True일 때만 결과를 표시합니다.
if 'calculated' in st.session_state and st.session_state['calculated']:
    st.markdown("---")
    st.subheader('⭐ 계산 결과')
    
    # st.metric 또는 st.markdown을 사용하여 큰 숫자로 노출
    # st.metric은 레이블과 함께 표시하기 좋습니다.
    st.metric(label="함수 (add) 리턴 값", value=f"{st.session_state['result']:,.0f}")
    
    # 또는 st.markdown을 사용하여 아주 큰 폰트로 표시할 수도 있습니다.
    # st.markdown(f"## <p style='color:blue; font-size:48px;'>{st.session_state['result']:,.0f}</p>", unsafe_allow_html=True)