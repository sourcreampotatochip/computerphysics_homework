import numpy as np

def heun (f, y0, t0, tf, h, ea=1.e-7):
    n = int ((tf-t0)/h) # 간격의 수 계산
    t = np.zeros (n) # t와 y에 빈 열 (array) 생성
    y = np.zeros (n)
    for i in range (n): # 열(array) 채우기
        t[i] = i*h
    if t[n-1] < tf: #고려해야할 간격이 남았는지 확인
        t = np.append (t, tf)
        t[0] = t0
        y = np.append (y, 0)
        y[0] = y0
    for i in range (n):
        h = t[i+1] - t[i] # 이번 간격에서의 h
        y1 = y[i] + f(t[i], y[i]*h) # 예측기 단계
        while True: # 반복 loop
            fbar = (f(t[i], y[i]) + f(t[i+1], y1))/2 # 평균 기울기
            y2 = y[i] + fbar * h # 수정기 단계
            if abs((y1 - y2)/y2) < ea: break # 수렴 확인
            y1 = y2 # 아직 수렴 안되었으면 반복
        y[i+1] = y2 # 수렴되었으면, y 값 설정
    return t, y