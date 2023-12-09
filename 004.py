from copy import deepcopy as c
H, W = map(int, input().split())

A = []
for i in range(H):
    A.append(list(map(int, input().split())))

B = c(A)
for i in range(H):
    sum = 0
    for j in range(W):
        sum += A[i][j]
    for j in range(W):
        B[i][j] = sum

for j in range(W):
    sum = 0
    for i in range(H):
        sum += A[i][j]
    for i in range(H):
        B[i][j] += sum
        B[i][j] -= A[i][j]

for i in range(H):
    for j in range(W-1):
        print(B[i][j], end="")
        print(" ", end="")
    print(B[i][W-1])
    
'''
最終的な考え方は悪くなかった
事前計算はもっと簡単に(計算量少なく)できる
yoko = [0] * H
tate = [0] * W
 for i in range(H):
    for j in range(W):
        yoko[i] += A[i][j]
        tate[j] += A[i][j]

Python なら
yoko = list(map(sum, A))
tate = list(map(sum, zip(*A)))
でいける
map(sum, A)は各行の合計 -> list()でリスト化
zip(*A)が行列Aの転置

出力についても
print(' '.join(map(lambda j: str(yoko[i] + tate[j] - A[i][j]), range(W))))
でいける
各range(W)の列について、{各列(j)に対して指定の計算をするラムダ関数}を実行
'''