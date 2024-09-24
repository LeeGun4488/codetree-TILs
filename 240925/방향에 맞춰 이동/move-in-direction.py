n = int(input())
x, y = 0, 0
for _ in range(n):
    drc, cnt = input().split()
    cnt = int(cnt)
    if drc == 'N':
        y += cnt
    elif drc == 'E':
        x += cnt
    elif drc == 'S':
        y -= cnt
    elif drc == 'W':
        x -= cnt

print(x,y)