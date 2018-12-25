import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as m
if __name__=="__main__":
	mpl.rcParams['font.sans-serif'] = [u'SimHei']
	mpl.rcParams['axes.unicode_minus'] = False


	x = np.random.rand(10000)
	t = np.arange(len(x))
	#plt.hist(x,30,color='m',alpha=0.5,label=u'均匀分布')
	plt.plot(t,x,'g.',label=u'均匀分布')
	plt.legend(loc='upper right')
	plt.grid()
	plt.show()
