T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nsum = 0
    m = N//2
    arr = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(abs(m-i),N-abs(m-i)):
            nsum += arr[i][j]
    print(f'#{tc} {nsum}')