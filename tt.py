for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    dr1 = [-1, 0, 1, 0]  # 델타 값을 준다.
    dc1 = [0, 1, 0, -1]  # 위, 우, 하, 좌 순으로

    for i in range(N):
        for j in range(N):  # 모든 값에 대해 접근할 것이기 때문에 일단 행과 열에 대해 반복문을 돌린다.
            sums = 0        # 임시의 더한 값을 저장해줄 변수를 만든다.
            sums += arr[i][j]         # 델타의 접근은 1부터 할 것이기 때문에 일단 해당 위치의 값을 더한다.
            for k in range(4):        # 델타의 접근 방향 설정
                for l in range(1, M): # 델타 접근이 어디까지 갈 것인가, 1부터 M까지 간다.
                    lr, lc = i + dr1[k] * l, j + dc1[k] * l  # 첫 델타는 현재 위치 중심으로 l번 곱해준다.
                    if lc < 0 or lc >= N or lr < 0 or lr >= N:  # 델타가 원래의 배열을 벗어나면
                        break                                   # 브레이크 걸어줌
                    sums += arr[lr][lc]  # 델타 접근 값을 더해준다.
            if sums > result:            # 최종 반환할 값인 result와의 임시 더해준 값을 비교해서
                result = sums            # 임시의 sums가 result보다 크면 result는 sums가 된다.
                sums = 0

    dr2 = [1, -1, -1, 1]   # 위 과정과 똑같다.
    dc2 = [1, 1, -1, -1]   # 다만, 델타를 4방향의 대각선으로 준 것.

    for i in range(N):
        for j in range(N):
            sums = 0
            sums += arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    lr, lc = i + dr2[k]*l, j + dc2[k]*l
                    if lc < 0 or lc >= N or lr < 0 or lr >= N:
                        break
                    sums += arr[lr][lc]
            if sums > result:
                result = sums
    print(f'#{tc+1} {result}')
