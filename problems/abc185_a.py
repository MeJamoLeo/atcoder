from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
	len_numbers = len(numbers)
	for i in range(len_numbers):
		for j in range(len_numbers - 1 - i):
			if numbers[j] > numbers[j + 1]:
				numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
	return numbers

l = list(map(int, input().split()))
bubble_sort(l)
print(l[0])