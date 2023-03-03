T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    # #가로
    # for row in range(N):
    #     cnt = 0
    #     for col in range(N):
    #         if arr[row][col] == 'o':
    #             cnt += 1
    #         else:
    #             cnt = 0
    #     if cnt == 5:
    #         ans = "YES"
    # #세로
    # for col in range(N):
    #     for row in range(N):
    #         if arr[row][col] == 'o':
    #             cnt += 1
    #         else:
    #             cnt = 0
    #     if cnt == 5:
    #         ans = "YES"

    # #대각1
    # cnt = 0
    # for i in range(N):
    #     if arr[i][i]== 'o':
    #         cnt += 1
    #     else:
    #         cnt = 0
    # if cnt == 5:
    #     ans = "YES"
    #
    # #대각2
    # cnt = 0
    # for i in range(N):
    #     if arr[i][i]== 'o':
    #         cnt += 1
    #     else:
    #         cnt = 0
    # if cnt == 5:
    #     ans = "YES"

    #대각선
    def omok(arr):
    #가로
    for row in range(N):
        cnt = 0
        for col in range(N):
            if arr[row][col] == 'o':
                cnt += 1
            else:
                cnt = 0
        if cnt == 5:
            ans = "YES"
    #세로
    for col in range(N):
        for row in range(N):
            if arr[row][col] == 'o':
                cnt += 1
            else:
                cnt = 0
        if cnt == 5:
            ans = "YES"