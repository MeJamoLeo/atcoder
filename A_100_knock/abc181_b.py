N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

res = 0
for nums in l:
	sum_array = (nums[1] - nums[0] + 1) * (nums[0] + nums[1]) / 2
		# mからnの総和を求める (https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1381227848)
	res += sum_array
print(int(res))
