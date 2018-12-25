import os
from threading import Thread

def test():
	print("---abc---")
	time.sleep(1)

for i in range(5):
	t = Thread(target=test)
	t.start()
	
