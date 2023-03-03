import sys
sys.stdin = open("input.txt","r")
T = 10
for tc in range(1,T+1):
    N = int(input())
    arr= [map(int,input().split()) for _ in range(N)]
    arr_t= list(zip(*arr))
    print(arr_t)
    ans = 0
    for lst in arr_t:
        prev = 0
        for n in lst:
            if n!= 0:
                if n==2 and prev==1:
                    ans += 1
                prev = n

    print(f'#{tc} {ans}')