import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 그리드 크기 설정
N = 150
ON = 275
OFF = 0
vals = [ON, OFF]

# 무작위로 그리드 초기화 (초기 생명체 배치)
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def update(frameNum, img, grid, N):
    # 그리드 복사본 생성
    newGrid = grid.copy()
    
    for i in range(N):
        for j in range(N):
            # 토러스(Torus) 구조로 주변 8개 이웃의 생명체 수 계산
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            
            # 라이프 게임 규칙 적용
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # 데이터 업데이트
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# 애니메이션 시각화 설정
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='gray')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                              frames=10, interval=100, save_count=50)

plt.show()
