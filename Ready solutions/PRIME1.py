from math import sqrt

primes = [2]

for i in range(3,32000,2):
    isprime = True

    cap = sqrt(i)+1

    for j in primes:
        if (j >= cap):
            break
        if (i % j == 0):
            isprime = False
            break
    if (isprime):
        primes.append(i)

testCases = input()
output = ""
for t in range(testCases):

    if (t > 0):
        output += "\n"

    a,b = raw_input().split(' ')
    a = int(a)
    b = int(b)
    cap = sqrt(b)+1

    if (a < 2):
        a = 2

    isprime = [True]*100001

    for i in primes:
        if (i >= cap):
            break

        if (i >= a):
            start = i*2
        else:
            start = a + ((i - a % i)%i)

        # The two below, obscure lines create a continuous
        #  block of false elements in order to set all
        #  elements correspnding to numbers divisible by i
        #  in isprime to be false
        # In turns out that this runs substantially faster
        #  than setting the elements individually using loops
        falseblock = [False] * len(isprime[start-a:b+1-a:i]);
        isprime[start-a:b+1-a:i] = falseblock

    for i in range(a,b+1):
        if (isprime[i-a] == True):
            output += str(i) + "\n"

print output[:-1]