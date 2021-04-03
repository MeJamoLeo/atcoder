# https://atcoder.jp/contests/abc088/tasks/abc088_b
N = int(input())
cards =sorted(list(map(int, input().split())), reverse=True) 
A,B = [],[]

for i in range(N):
    if i % 2 == 0:
        A.append(cards[i])
    else:
        B.append(cards[i]) 
res = sum(A) - sum(B)
print(res)
