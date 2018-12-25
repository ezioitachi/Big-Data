import numpy as np
import matplotlib.pyplot as plt
import math as m
if __name__=="__main__":

	x = np.arange(1,0,-0.001)
	y = (-3*x*np.log(x) + np.exp(-(40*(x-1/np.e))**4)/25)/2
	plt.figure(figsize=(5,7),facecolor='w')
	plt.plot(y,x,'r-',linewidth=2)
	plt.grid(True)
	plt.title(u'breast line',fontsize=20)
	plt.show()