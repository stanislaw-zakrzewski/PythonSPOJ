def function_z(n):

	return n

T = int(raw_input())
O = ''
for t in range(T):
	O += function_z(int(raw_input()))
	O += '\n'
print(O)
