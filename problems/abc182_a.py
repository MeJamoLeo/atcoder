A_follower, B_follow = map(int, input().split())
max = 2 * A_follower + 100
res = max - B_follow
print(res)
print()