import numpy as np

def eulerm(f, y0, t0, tf, h):
    n = len(y0) # 방정식의 수
    m = int((tf-t0)/h) + 1 # 간격의 수
    t = np.zeros(m) # 빈 열 (array)
    y = np.zeros((m, n)) # 빈 2차원 열 (array)
    y[0,:] = y0 # y에 할당된 초기 조건 (y0) y[0,:]는 배열 y의 
    for i in range (1, m): # 단계별 해에 대한 loop
        t[i] = t0 + i*h # 현재 간격 끝에서 t
        if t[i] > tf: # tf를 초과하는지 확인
            t[i] = tf # 초과하면, t[i]를 tf로 설정
            h = t[i] - t[i-1] # 이후 h를 조정
        y[i] = y[i-1,:] + f(t[i-1], y[i-1, :])*h# 오일러 방정식
    return t, y