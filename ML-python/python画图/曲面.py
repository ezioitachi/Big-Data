import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as m
from  scipy import stats

from mpl_toolkits.mplot3d import Axes3D

if __name__=="__main__":
	mpl.rcParams['font.sans-serif'] = [u'SimHei']
	mpl.rcParams['axes.unicode_minus'] = False

	x,y = np.mgrid[0:1:201j, 0:1:201j]
	z = x**2/100-y**2/100
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	ax.plot_surface(x,y,z,rstride=3,cstride=3,cmap=plt.cm.Blues,linewidth=2)
	plt.axis('off')
	ax = fig.add_subplot(1, 1, 1, projection='3d')
	p = ax.plot_wireframe(x, y, z, rstride=4, cstride=4)
