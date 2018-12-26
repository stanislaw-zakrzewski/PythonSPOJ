def transform(e):
	if(e[0] == '('):
		e = e[1:-1]
	counter = 0;
	for c in range(len(e)):
		if(e[c] == '('): counter+=1
		elif(e[c] == ')'): counter-=1
		elif(e[c] == '+' and counter == 0):
			return (transform(e[:c]) + transform(e[c+1:]) + '+')
		elif(e[c] == '-' and counter == 0):
			return (transform(e[:c]) + transform(e[c+1:]) + '-')
		elif(e[c] == '/' and counter == 0):
			return (transform(e[:c]) + transform(e[c+1:]) + '/')
		elif(e[c] == '*' and counter == 0): 
			return (transform(e[:c]) + transform(e[c+1:]) + '*')
		elif(e[c] == '^' and counter == 0):
			return (transform(e[:c]) + transform(e[c+1:]) + '^')
	return e


t = int(raw_input())
output = ''
for i in range(t):
	e = raw_input()
	output += transform(e)
	output += '\n'
print(output)
