import streamlit as st
import pandas as pd

st.title("CSV 파일 업로드 예제")

uploaded_file = st.file_uploader("CSV 파일을 선택하세요", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("파일 내용 미리보기:")
    st.dataframe(df.head())
else:
    st.write("CSV 파일을 업로드해주세요.")
