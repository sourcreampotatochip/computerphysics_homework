#libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#create data
size=100000
df=pd.DataFrame({
    'x': np.random.normal(size=size),
    'y': np.random.normal(size=size)
})
print (df.head())

# df에서 x와 y를 가져옵니다.
x = df['x']
y = df['y']

# 2D 히스토그램을 axs[0,0]에 그리기
plt.hist2d(x,y,bins=(100,100), cmap=plt.cm.jet)
plt.title('2D Histogram')

plt.show()