from multiprocessing import Pool
import os
import random
import time

def worker():
	for i in range(5):
		print("pid=%d" %os.getpid())
		time.sleep(1)
pool = Pool(3)

for i in range(10):
	print("%d" %i)
	pool.apply_async(worker)

pool.close()
pool.join()
