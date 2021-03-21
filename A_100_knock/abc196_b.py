import string
# 文字列として受け取って，ドット以下を削る
X = input()
if X.split('.'):
	res = X.split('.')[0]
	print(res)
else:
	print(X)
