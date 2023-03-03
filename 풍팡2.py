T= int(input())
for tc in range(1,T+1):
    N,M= map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #상하좌우
    mmax = 0
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for row in range(N):
        for col in range(M):
            fsum = arr[row][col]
            for i in range(4):
                newr= row+dr[i]
                newc= col+dc[i]
                if 0<=newr<N and 0<=newc<M:
                    fsum += arr[newr][newc]
            if mmax < fsum:
                mmax = fsum

    print(fsum)


T= int(input())
for tc in range(1,T+1):
    N,M= map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #상하좌우
    mmax = 0
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for row in range(N):
        for col in range(M):
            sump = arr[row][col]
            for i in range(4):
                newr = row+dr[i]
                newc =col+dc[i]
                if 0<= newr<N and 0<= newc<M:
                    sump+= arr[newr][newc]
            if mmax < sump: #
                mmax = sump
    print(f'#{tc} {mmax}')