def addReverse(s):
	s2 = s.split(" ")
	a = s2[0][::-1]
	b = s2[1][::-1]
	print(int(str((int(a) + int(b)))[::-1]))

casesCount = int(raw_input())
cases = []
for i in range(casesCount):
	cases.append(raw_input())
for c in cases:
	addReverse(c)
	