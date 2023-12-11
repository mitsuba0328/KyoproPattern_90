H, W = map(int, input().split())

row = H % 2 + H // 2
col = W % 2 + W // 2
#print(row * col)


'''
基本的にはこの実装で問題ないがコーナーケースが全落ちする

解説を読むと、H=1 or W=1で落ちるらしい たしかに
#.#.#
.....
#.#.#
.....
#.#.#
'''

if H == 1:
    print(W)
elif W == 1:
    print(H)
else:
    print(row * col)
