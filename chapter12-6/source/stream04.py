import streamlit as st
import pandas as pd

st.title("Streamlit 도시 선택 📊")

# 샘플 데이터 생성
data = {
    "이름": ["철수", "영희", "민수", "지수", "태현"],
    "나이": [25, 30, 22, 27, 29],
    "도시": ["서울", "부산", "대전", "광주", "서울"]
}
df = pd.DataFrame(data)

# 도시 선택 필터
selected_city=st.selectbox("도시를 선택하세요:", df["도시"].unique())

#선택한 도시의 데이터만 표시
filtered_df=df[df["도시"]==selected_city]

st.write(f"**{selected_city}에 거주하는 사람들:**")
st.dataframe(filtered_df) #streamlit에서 데이터프레임 출력


