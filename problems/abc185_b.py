import sys

N, M, T = map(int, input().split())
l = [list(map(int, input().split())) for l in range(M)]

# 0になった時点でNoを出力