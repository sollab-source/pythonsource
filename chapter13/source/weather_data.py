import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('weather_data.csv')

# 데이터 살펴보기
print(df.head())

# 데이터 전처리 (결측값 제거 및 형 변환)
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

# 월별 평균 기온, 습도, 강수량 계산
monthly_avg = df.groupby('Month')[['Temperature', 'Humidity', 'Precipitation']].mean()

# 월별 기온 변화 시각화
plt.figure(figsize=(10,5))
plt.plot(monthly_avg.index, monthly_avg['Temperature'], marker='o', linestyle='-', label='Temperature (°C)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Average Temperature')
plt.legend()
plt.grid()
plt.show()

# 가장 더웠던/추웠던 날 찾기
hottest_day = df.loc[df['Temperature'].idxmax()]
coldest_day = df.loc[df['Temperature'].idxmin()]
print(f"가장 더웠던 날: {hottest_day['Date']} ({hottest_day['Temperature']}°C)")
print(f"가장 추웠던 날: {coldest_day['Date']} ({coldest_day['Temperature']}°C)")

# 강수량이 가장 많았던 날 찾기
wettest_day = df.loc[df['Precipitation'].idxmax()]
print(f"강수량이 가장 많았던 날: {wettest_day['Date']} ({wettest_day['Precipitation']}mm)")

# 특정 기간 동안의 날씨 패턴 분석 (예: 6개월간 평균 기온 변화)
recent_trend = df[df['Date'] >= '2024-07-01'].groupby('Month')['Temperature'].mean()
plt.figure(figsize=(10,5))
plt.plot(recent_trend.index, recent_trend.values, marker='o', linestyle='-', label='Temperature (°C)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Recent 6 Months Temperature Trend')
plt.legend()
plt.grid()
plt.show()