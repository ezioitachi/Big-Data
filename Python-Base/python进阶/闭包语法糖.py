def wi(func):
	def inner():
		print("---checking---")
		func()
	return inner
#f1=wi(f1)
@wi
def f1():
	print("---f1---")
@wi
def f2():
	print("---f2---")
 
f1()
f2()
