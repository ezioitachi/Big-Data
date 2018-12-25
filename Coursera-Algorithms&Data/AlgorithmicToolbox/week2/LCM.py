#Uses python3

import sys

def get_LCM(a,b):
	if a < b:
		m,n = b,a
	else:
		m,n = a,b
	
	while n != 0:
		m,n = n,m%n
	
	return int((a*b)//m)

if __name__ == "__main__":
	input = sys.stdin.read()
	a,b = map(int, input.split())
	print(get_LCM(a,b))







