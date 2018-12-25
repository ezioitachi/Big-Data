
import numpy as np
import math as m
import matplotlib.pyplot as plt

if __name__=="__main__":

	mu = 0
	sigma = 1
	x = np.linspace(mu-3*sigma,mu+3*sigma,51)
	y = np.exp(-(x-mu)**2/(2*sigma**2))/(m.sqrt(2*m.pi)*sigma)
	print(x.shape)
	print(y.shape)
	plt.figure(facecolor='w')
	plt.plot(x,y,'r-',x,y,'go',linewidth=2, markersize=8)
	plt.xlabel('x',fontsize=15)
	plt.ylabel('y',fontsize=15)
	plt.title('Gauss Distribution',fontsize=18)
	plt.grid(True) #画虚线格子
	plt.show() 

	