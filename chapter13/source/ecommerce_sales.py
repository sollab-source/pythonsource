import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('ecommerce_sales_data.csv')

# 데이터 살펴보기
print(df.head())

# 데이터 전처리 (결측값 제거 및 형 변환)
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
df['Sales'] = df['Quantity Ordered'] * df['Price Each']

# 월별 매출 분석
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Sales Trend')
plt.grid()
plt.show()

# 가장 많이 팔린 제품 찾기
top_products = df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False)
print("가장 많이 팔린 제품:")
print(top_products.head(10))

# 고객별 구매 패턴 분석
customer_sales = df.groupby('Purchase Address')['Sales'].sum().sort_values(ascending=False)
print("가장 높은 매출을 기록한 고객 주소:")
print(customer_sales.head(10))