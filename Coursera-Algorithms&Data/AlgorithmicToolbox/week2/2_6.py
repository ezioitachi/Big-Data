# Uses python3
import sys

def Fibo(n): 
	
	m=10
	
	R = [0%m, 1%m]	
	if n <=1:
		Sum = 0
		Sum += R[n]
		return Sum
	else:
		Sum = 1
		SumR = 0
		for i in range(2,n+1):
			R.append(i)
			R[i] = (R[i-2]%m + R[i-1]%m)%m	
			Sum = (Sum + R[i])%m
			
			if (R[i] == 0 and R[i-1] == 1):
				for j in range(n%i+1):
					SumR += R[j] 
				SumS = (Sum*(n//i) + SumR)%m
				return SumS
		return Sum

if __name__ =='__main__':
	n = int(input())
	print(Fibo(n))

