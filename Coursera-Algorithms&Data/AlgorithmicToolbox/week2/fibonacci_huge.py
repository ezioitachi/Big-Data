# Uses python3
import sys

def Fibo_huge(n,m): 
	
	R = [0%m, 1%m]	
	if n <=1:
		return R[n]
	else:
		for i in range(2,n+1):
			R.append(i)
			R[i] = (R[i-2]%m + R[i-1]%m)%m	
			
			if (R[i] == 0 and R[i-1] == 1):
				r = R[n%i]
				return r
		                		
		return R[n]

if __name__ =='__main__':
	input = sys.stdin.read()
	n,m = map(int, input.split())
	print(Fibo_huge(n,m))

