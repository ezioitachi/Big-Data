import os
import time
ret = os.fork()
g_num=100
if ret ==0:
	print("process-1")
	g_num += 1
	print("process-1 g_num=%d" %g_num)
else:
	time.sleep(3)
	print("process-2")
	print("process-2 g_num=%d" %g_num)
