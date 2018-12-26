def smallest_palindrome(n):
	mustBeRaised = False
	wasRaised = False
	L = []
	R = []
	while(len(n) > 2):
		a = n[0]
		b = n[len(n)-1]
		if(int(a) > int(b)):
			b = a
			mustBeRaised = False
			wasRaised = True
		elif(int(a) < int(b)):
			b = a
			mustBeRaised = True
		L.append(str(a))
		R.append(str(b))
		n = n[1:-1]

	if(len(n) == 2):
		a = n[0]
		b = n[1]
		if(int(a) > int(b)):
			b = a
		elif(int(a) < int(b) or mustBeRaised or wasRaised == False):
			a = int(a)+1
			b = a
		L.append(str(a))
		R.append(str(b))
	elif(mustBeRaised or wasRaised == False):
		L.append(str(int(n[0]) + 1))

	n = L + R[::-1]

	return ''.join(n)

T = int(raw_input())
O = ''
for t in range(T):
	n = raw_input()
	O += smallest_palindrome(n)
	O += '\n'
print(O)
