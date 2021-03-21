import string
import sys
#桁数を数える
# 文字列を真ん中で分ける
# 左右を比べる．(数値変換)
# 値が小さい方を使う

N = list(input())
if len(N) % 2 == 1:
	print()
	sys.exit()
target_len = len(N) // 2

X = "".join(N[0:target_len:1])
Y = "".join(N[target_len::1])

if int(X) == 0:
	print(int(Y) - 1)
	sys.exit()

if int(Y) == 0:
	print(int(X) - 1)
	sys.exit()

if (X <= Y):
	print(X)
else:
	print(Y)