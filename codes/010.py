# TLEしてしまったので書き直す
'''
N = int(input())

points = []
for i in range(N):
    c, p = map(int, input().split())
    points.append([c, p])

Q = int(input())

for i in range(Q):
    first, last = map(int, input().split())
    sum1 = 0
    sum2 = 0
    for j in range(first-1, last):
        if points[j][0] == 1:
            sum1 += points[j][1]
        else:
            sum2 += points[j][1]
    print(sum1, sum2)
'''
    
# だめだった
# 解説(notコード)を読んだ上で書いてみる

N = int(input())

sum1 = [0]
c1 = 0
sum2 = [0]
c2 = 0
for i in range(N):
    c, p = map(int, input().split())
    if c == 1:
        c1 += p
    else:
        c2 += p
    sum1.append(c1)
    sum2.append(c2)

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(sum1[r] - sum1[l-1], sum2[r] - sum2[l-1])
        