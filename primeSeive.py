import sys

def pullprimes(p):
	myRange=range (p,max(numbers))
	for n in myRange:	
		if (n*p in primes):
			primes.remove (n*p)

def newp (prevp):
	for a in primes:
		if (a>p): 
			return a
	return prevp
			
a=int(sys.argv[1])
b=int(sys.argv[2] )
print a
print b
	
numbers=range(a,b)
primes=range(a,b)
first=True

for n in numbers: 
	if (first):
		first=False
		p=2
		pullprimes (p)
	else:
		p=newp(p)
		pullprimes(p)

print primes