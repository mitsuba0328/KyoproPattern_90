N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = list(map(lambda a, b : b - a, A, B))
n = 0
for i in range(N):
  if C[i] >= 0:
    n += C[i]
  else:
    n += -C[i]

if n > K:
  print("No")
elif n == K:
  print("Yes")
else:
  if (K - n) % 2 == 0:
    print("Yes")
  else:
    print("No")
