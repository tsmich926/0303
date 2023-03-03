# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     #가로 탐색
#     for row in range(N):
#         cnt = 0
#         for col in range(N):
#             if arr[row][col] == 'o':
#
#     #세로 탐색
#
#
#
#     #대각1
#
#
#     #대각2

def solve(arr):
    for si in range(1, N + 1):
        for sj in range(1, N + 1):
            for di, dj in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                for mul in range(5):
                    ni, nj = si + di * mul, sj + dj * mul
                    if arr[ni][nj] != 'o':
                        break
                else:
                    return 'YES'
    return 'NO'


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = ['.' * (N + 2)] + ['.' + input() + '.' for _ in range(N)] + ['.' * (N + 2)]

    ans = solve(arr)
    print(f'#{test_case} {ans}')