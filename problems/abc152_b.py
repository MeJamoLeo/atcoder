a, b = input().split()

A: str = a * int(b)
B: str = b * int(a)

if A == B:
	print(A)
	exit()
if b < a:
	print(B)
else:
	print(A)
