import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
leader, follwer = map(int, input().split())
cnt = n

for i in range(n):
    person = number[i]
    person -= leader
    if person > 0:
        res = person % follwer
        if res == 0:
            cnt += int(person / follwer)
        else:
            cnt += int(person / follwer) + 1

print(int(cnt))