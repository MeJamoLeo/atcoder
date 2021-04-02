from typing import List
import math

def Manhattan(nums: List[int]) -> int:
	len_nums = len(nums)
	for i in range(len_nums):
		if nums[i] < 0:
			nums[i] = -1 * nums[i]
	return sum(nums)

def Euclid(nums: List[int]) -> int:
	len_nums = len(nums)
	ans_l = []
	for i in range(len_nums):
		ans_l.append(nums[i] * nums[i])
	return math.sqrt(sum(ans_l))

def Chebichef(nums: List[int]) -> int:
	return max(nums)

N = int(input())
list_x = list(map(int, input().split()))

n_man = Manhattan(list_x)
n_euc = Euclid(list_x)
n_che = Chebichef(list_x)

print(n_man)
print('{:.100}'.format(n_euc))
print(n_che)
