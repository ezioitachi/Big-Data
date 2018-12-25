import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as m
from  scipy import stats

from mpl_toolkits.mplot3d import Axes3D

if __name__=="__main__":
	mpl.rcParams['font.sans-serif'] = [u'SimHei']
	mpl.rcParams['axes.unicode_minus'] = False

	x,y = np.mgrid[-3:3:101j, -3:3:101j]
	z = x*y*np.exp(-(x**2+y**2)/2)/m.sqrt(2*m.pi)
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	ax.plot_surface(x,y,z,rstride=3,cstride=3,cmap=plt.cm.Blues,linewidth=0.5)
	plt.show()
