import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/sungguchoi/Desktop/전산물리/모듈, 그래프/OBS_ASOS_DD_20260922144459.csv', encoding='cp949')

date = pd.to_datetime(df.iloc[:, 2]).dt.day
temp = df.iloc[:, 3]

plt.rc('font', family='AppleGothic')
plt.grid()
plt.plot(date, temp)
plt.xlabel('Date(일)')
plt.ylabel('Temperature(℃)')
plt.xticks(rotation=45)
plt.title('2026년도 9월 서울 평균 기온')

plt.tight_layout()
plt.show()


