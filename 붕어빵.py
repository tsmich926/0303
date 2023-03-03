#반드시 리스트를 오름차순으로 정렬해줄것
T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    lst = list(map(int,input().split()))
    cnt = 0
    ans = 'Possible'
    for t in sorted(lst):
        cnt += 1
        if cnt > (t//M)*K:
            ans = 'Impossible' #도착한 사람수보다 만들어진 붕어빵이 작은경우
            break
    print(f'#{tc} {ans}')