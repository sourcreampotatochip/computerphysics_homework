import numpy as np

def trap1(f, a, b, n=100):
    x = a # x를 구간 왼쪽 a로 설정
    h = (b - a)/n # 간격 계산
    sm = 0 # 적분 합을 0으로 설정
    integral_values = [0] # 초기 적분값을 0으로 시작

    for i in range(n-1): # 면적을 누적하여 합하기 위한 for loop
        ar = (f(x) + f(x+h)) / 2 *h # 현재 간격에서의 면적
        sm += ar #면적의 누적 합
        integral_values.append(sm) # 누적된 적분 값을 리스트에 추가
        x += h # 다음 간격으로 x를 진행
        
    return np.linspace(a, b, n), integral_values # 적분값을 반환

def trap2 (f, a, b, n=100):
    x = a # x를 구간 왼쪽 a로 설정
    h = (b - a)/n # 간격 계산
    sm = 0 # 적분 합을 0으로 설정
    for i in range (n-1): # 면적을 누적하여 합하기 위한 for looop
        ar = (f(x) + f(x+h)) / 2*h #현재 간격에서의 면적
        sm = sm + ar # 면적 누적의 합
        x = x + h # 다음 간격으로 x를 진행
    return sm # 전체 면적 반환
        