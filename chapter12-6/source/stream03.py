import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 차트 한글깨짐 방지
plt.rcParams['font.family'] = "Malgun Gothic"  # Windows (맑은 고딕)
plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 기호 깨짐 방지

st.title("Streamlit 시각화 적용 📊")
number = st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, value=10)

st.write(f"입력한 숫자의 제곱: {number**2}")

x=np.linspace(0, number, 100)
y=x**2

fig, ax=plt.subplots()
ax.plot(x,y, label="y=x^2", color="blue")
ax.set_xlabel("X 값")
ax.set_ylabel("Y 값")
ax.legend()

st.pyplot(fig)