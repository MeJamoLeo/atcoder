A, B, C = map(int, input().split())

if A == B and A == C:
	print("No")
	exit()

if A != B and A != C and B != C:
	print("No")
	exit()
print("Yes")