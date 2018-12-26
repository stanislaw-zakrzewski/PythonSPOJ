def pairsCount(fc, pc, mff):
	count = 0
	for i in range(fc-1):
		for j in range(i+1, fc):
			if(mff[i]+mff[j] == pc):
				count +=1
	print count

testCases = int(raw_input())
friendsCount = []
pizzaCosts = []
moneyForFriend = []
for i in range(testCases):
	s = (raw_input()).split(' ')
	friendsCount.append(int(s[0]))
	pizzaCosts.append(int(s[1]))
	moneyForFriend.append(map(int,(raw_input()).split(' ')))
print('')
for i in range(testCases):
	pairsCount(friendsCount[i], pizzaCosts[i], moneyForFriend[i])