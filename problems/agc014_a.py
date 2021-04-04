# https://atcoder.jp/contests/agc014/tasks/agc014_a
import random

# sample test
# A = random.randint(1, 10**2)
# B = random.randint(1, 10**2)
# C = random.randint(1, 10**2)
# print(A, B, C)

A,B,C = map(int, input().split())
count = 0

while A%2==0 and B%2==0 and C%2==0:
    tmp_a = (B + C) // 2
    tmp_b = (A + C) // 2
    tmp_c = (B + A) // 2
    # print(str(count) + ": ",tmp_a,tmp_b,tmp_c)
    A = tmp_a
    B = tmp_b
    C = tmp_c
    count += 1
    if A == B == C:
        count = -1
        break
print(count)
