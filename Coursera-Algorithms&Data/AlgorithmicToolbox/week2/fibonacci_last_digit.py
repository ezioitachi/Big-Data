# Uses python3
n = int(input())

def Fibo(n): 
	
	F = [None]*(n+2)
	F[0] = 0
	F[1] = 1

	if n <=1:
		return F[n]
	else:
		for i in range(2,n+1):
			F[i] = (F[i-1] + F[i-2]) % 10

		return F[n]

print(Fibo(n))

