def func(funcNew):
	def func_in(*args,**kwargs):
		ret=funcNew(*args,**kwargs)
		return ret
	return func_in

@func
def test(a,b):
	print("--%d%d--" %(a,b))
	return a,b
test(1,2)
