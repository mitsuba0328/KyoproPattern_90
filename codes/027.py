N = int(input())

name = set()
for i in range(N):
  s = input()
  if s not in name:
    name.add(s)
    print(i+1)
    
'''
簡単。考え方もよい。
最初listでやったらTLEしたからSetにした。それが肝だったぽい。

※
解説によると一般的には10^8~10^9くらいの計算回数しか許されないらしく
N<=10^5ではO(N^2)がTLEするって話らしい
'''