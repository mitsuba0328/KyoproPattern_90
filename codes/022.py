import math

A, B, C = map(int, input().split())

num = int(math.gcd(A, B, C))

print(A//num + B//num + C//num -3)

'''
考え方もよかった
math.gcd()はずるかったね 無かったらユークリッドで
Pythonの割り算が'/'だとfloatになるのは知らなかった '//'で解決した
'''