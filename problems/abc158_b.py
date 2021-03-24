N, A, B = map(int, input().split())
unit = A + B
count_u = 0
count_all = 0

if A == 0 or B == 0:
	print(0)
	exit()

while N > count_all:
	count_u += 1
	count_all += unit

# Nが青色の部分で終わる場合
if N <= unit * (count_u - 1) + A:
	ans = N - ((count_u - 1) * B)
# Nが赤色の部分で終わる場合
else:
	ans = A * (count_u)

print(ans)
