def function_z(n):
	ret = 0
	f = 5
	while(f <= n):
		ret += n/f
		f *= 5
	return str(ret)

T = int(raw_input())
O = ''
for t in range(T):
	O += function_z(int(raw_input()))
	O += '\n'
print(O)
