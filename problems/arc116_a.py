from typing import List
def divisors(nb: int) -> List[int]:
	lower_divisors, upper_divisors = [], []
	i = 1
	while i*i <= nb and i < 10r:
		if nb % i == 0:
			lower_divisors.append(i)
			if i != nb // i: # unexpexted nums like "3 * 3"
				upper_divisors.append(nb//i)
		i += 1
	return lower_divisors + upper_divisors[::-1]


T = int(input())
odd_count = 0
even_count = 0
for i in range(T):
	case: int = int(input())
	l = divisors(case)
	for i in range(len(l)):
		if l[i] % 2 == 0:
			even_count += 1
		else:
			odd_count += 1
	if even_count == odd_count:
		res = "Same"
	elif even_count > odd_count:
		res = "Even"
	else:
		res = "Odd"
	print(res)

# resorcas
# - https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56

# memo
# upper_divisors[::-1]
#	配列を逆順に変換する