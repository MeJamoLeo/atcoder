# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b
N, A, B = map(int, input().split())
S = list(input())
path_count = 0
b_count = 1
for i in range(len(S)):
	if S[i] == 'a':
		if path_count < A + B:
			ans = "Yes"
			path_count += 1
		else:
			ans = "No"
	elif S[i] == 'b':
		if (path_count < A + B) and (b_count <= B):
			ans = "Yes"
			path_count += 1
			b_count += 1
		else:
			ans = "No"
	else:
		ans = "No"

	print(ans)
