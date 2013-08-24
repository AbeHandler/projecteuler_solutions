def hay3d(n):
	n=int(n)
	import math
	sqt=int(math.sqrt(int (n)))
	while (sqt>100):
		if ((n%sqt==0) and sqt>100 and sqt<999):
			if ((n/sqt)<1001):
				print sqt
				return True
		sqt=sqt-1
	return False