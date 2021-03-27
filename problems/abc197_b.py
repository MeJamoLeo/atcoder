H, W, X, Y = map(int, input().split())

array = []
for i in range(H):
	array_w = list(input())
	array.append(array_w)

row_YOKO = array[X-1]
row_TATE = []
for i in range(H):
	row_TATE.append(array[i][Y-1])

# 縦列 X = 4
# ['#', '.', '#', '.', '.']
#                  ↑
# 横列 Y = 2
# ['#', '.', '.', '#', '.']
#        ↑

# 縦列 X = 2
# ['#', '.', '.', '#']
#        ↑
# 横列 Y = 2
# ['.', '.', '.', '#']
#   ↑

### 戻る作業
while row_TATE[X-1] == "." and X != 0:
	X -= 1
while row_YOKO[Y-1] == "." and Y != 0:
	Y -= 1
	#スタート地点の確定

count = 0
while X < H and row_TATE[X] == ".":
	count += 1
	X += 1
while Y < W and row_YOKO[Y] == ".":
	count += 1
	Y += 1

print(count-1)