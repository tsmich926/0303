T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    ans = 0
    m= N//2
    for i in range(N):
        for j in range(abs(m-i),N-abs(m-i)):
            ans += arr[i][j]
    print(f'#{tc} {ans}')

#규칙성을 이용한 방법
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    ans = 0
    m= N//2
    s= e= m
    for i in range(N):
        for j in range(s,e+1):
            ans += arr[i][j]
        #s,e재조정
        if i<m:
            s-=1
            e+=1
        else:
            s+=1
            e-=1
    print(f'#{tc} {ans}')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    m = N // 2
    # [2] 범위
    s = e = m
    for i in range(N):
        for j in range(s, e + 1):
            ans += arr[i][j]
        # s, e 재조정
        if i < m:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    # [1] 규칙성
    # for i in range(N):
    #     for j in range(abs(m-i), N-abs(m-i)):
    #         ans += arr[i][j]
    print(f'#{test_case} {ans}')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    field = [list(map(int, list(input()))) for _ in range(N)]

    total = 0
    for i in range(N):
        blank = abs(N // 2 - i)
        total += sum(field[i][blank:N - blank])

    print(f'#{test_case} {total}')