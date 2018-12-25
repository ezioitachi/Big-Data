# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
m = 0
l = 0

for i in range(0,n):
	if a[i] >=  m:
		m = a[i]
		index = i
	
for j in range(0,n):
	if (a[j] >= l and j != index):
		l = a[j]		

result = m*l
print(result)
