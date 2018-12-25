from multiprocessing import Pool, Manager
import os

def copyFileTask(name,oldFolderName,newFodlerName):
	
	fr = open(oldFolderName+'/'+name)
	fw = open(newFolderName+'/'+name,"w")
	
	content = fr.read()
	fw.write(content)
	
	fr.close()
	fw.close()	


def main(): 
	oldFoldernName = input("请输入文件夹的名字:")
	newFolderName = oldFolderName + '复件'
	os.mkdir(newFolderName）
	fileNames = os.listdir(oldFolderName)
	
	pool = Pool(5)
	queue = Manager().Queue()
	
	for name in fileNames:
		pool.apply_async(copyFileTask, args=(name,newFolderName,oldFodlerName))

	num = 0
	allNum = len(fileNames)
	while num < allNum:
		queue.get()
		num += 1
		copyRate = num/allNum
		print("\r copy的进度是：%.2f%%" %(copyRate*100), end="")	
	print("\n已完成copy")

if __name__ == "__main__":
	main()
