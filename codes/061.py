Q = int(input())

top = [] # まんなか -> 上
bottom = [] # まんなか -> 下
for i in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    top.append(x)
  elif t == 2:
    bottom.append(x)
  elif t == 3:
    n = len(top)
    N = len(bottom)
    if x > n:
      print(bottom[x - n - 1])
    else:
      print(top[n - x])

'''
やっぱりdequeを使う方がよさそう
使わなくても配列のN[10^3]を初期値として前後をとっていくという実装もあった

from collections import deque

Q = int(input())
d = deque()
for _ in range(Q):
  t, x = map(int, input().split())
  if t == 1:
    d.appendleft(x)
  elif t == 2:
    d.append(x)
  elif t == 3:
    print(d[x-1])
'''