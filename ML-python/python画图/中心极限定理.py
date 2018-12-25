import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as m
from  scipy import stats

if __name__=="__main__":
	mpl.rcParams['font.sans-serif'] = [u'SimHei']
	mpl.rcParams['axes.unicode_minus'] = False

	#t = 1000
	#a = np.zeros(10000)
	#for i in range(t):
	#	a += np.random.uniform(-5,5,10000)
	#a /= t
	#plt.hist(a,30,color='g',alpha=0.5,normed=True,label=u'均匀分布叠加')
	#plt.legend(loc='upper left')
	#plt.grid()
	#plt.show()

	lamda = 5
	p = stats.poisson(lamda)
	y = p.rvs(size=1000)
	mx = 30
	r = (0,mx)
	bins = r[1] - r[0]
	plt.figure(figsize=(15,8),facecolor='w')
	plt.subplot(121)
	plt.hist(y,bins=bins,range=r,color='g',alpha=0.8,normed=True)
	t = np.arange(0,mx+1)
	plt.plot(t,p.pmf(t),'ro-',lw=2)
	plt.grid(True)

	N = 1000
	M= 10000
	plt.subplot(122)
	a = np.zeros(M,dtype=np.float)
	p = stats.poisson(lamda)
	for i in np.arange(N):
		a += p.rvs(size=M)
	a /= N
	plt.hist(a,20,color='g',alpha=0.8,normed=True)
	plt.grid(b=True)
	plt.show()











