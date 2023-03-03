T = int(input())
for tc in range(1,T+1):
    arr = [input() for _ in range(5)]
    eq = ''
    for i in range(15):
        for j in range(5):
            if i < len(arr[j]):
                eq += arr[j][i]

    print(f'#{tc} {eq}')