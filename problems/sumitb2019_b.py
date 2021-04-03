# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

N = int(input())
X = []

for i in range(46298):
    res = int(i * 1.08)
    X.append(res)

for i in range(len(X)):
    if N == X[i]:
        print(i)
        exit()

print(":(")
