'''
なんと愚直に書いて間に合うらしい
O(N^5)だけどNC5=1/120N^5なので回る らしい
'''

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      for l in range(k+1, N):
        for m in range(l+1, N):
          if A[i]*A[j]*A[k]*A[l]*A[m] % P == Q:
            count += 1

print(count)

'''
でもこの書き方で通ったのはぎり奇跡かも
計算がint(2^62-1)を超えると計算に時間がかかってTLEの原因になるので
A[i]*A[j]%P*A[k]%P*A[l]%P*A[m]%P
とするべきらしい
全然実行時間が違うみたい
'''