

import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
	
	a = np.arange(0,60,10).reshape((-1,1))+np.arange(6)
	print(a)
	print(a.shape)
	
	L = [1,2,3,4,5,6]
	b = np.array(L)
	print(b)
	print(b.shape)

	c = a
	c.shape = (3,12)
	print(c)

	d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype=np.complex)
	print(d)

	e = np.arange(1,10,0.5)
	print(e)

	f = np.linspace(1,10,10, endpoint=True)
	print(f)

	g = np.logspace(1,2,9, endpoint=True, base=10)
	print(g)

	h = np.random.rand(10)
	print(h)
	print(a > 0.5)

	Aa = np.arange(1,10).reshape((3,3))
	Ab = np.arange(11,20).reshape((3,3))
	Ac = np.arange(21,30).reshape((3,3))
	print(np.stack((Aa,Ab,Ac), axis=0))
	print(np.stack((Aa,Ab,Ac), axis=1))
	print(np.stack((Aa,Ab,Ac), axis=2))
	print(np.dot(Aa,Ab))
	print(Aa*Ab)

	























