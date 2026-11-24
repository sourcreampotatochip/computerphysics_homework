import os
import matplotlib.pyplot as plt

os.chdir(os.path.abspath(os.path.dirname(__file__)))

# 한글 폰트 설정
plt.rc("font", family="AppleGothic")

# 1. 데이터 직접 입력 
countries = [
    "중국","미국","독일","인도","스페인","영국","프랑스","브라질","캐나다","이태리",
]
GW = [221.0, 96.4, 59.3, 35.0, 23.0, 21.7, 15.3, 14.5, 12.8, 10.0]

# 2. 막대 차트 그리기
plt.figure(figsize=(10, 5))
plt.bar(countries, GW, color="skyblue", edgecolor="k")

# 3. 차트 라벨 및 스타일 설정
plt.title("2021년 국가별 풍력발전 용량 순위")
plt.xlabel("국가")
plt.ylabel("발전 용량(GW)")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()