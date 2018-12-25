from threading import Thread
from socket import *

def recvData():
	while True:
		recvInfo = udpSocket.recvfrom(1024)
		print("\r>>%s:%s" %(str(recvInfo[1]),recvInfo[0]))
def sendData():
	while True:
		sendInfo = input("<<")
		udpSocket.sendto(sendInfo.encode("gb2312"),(destIp,destPort ))

udpSocket = None
destIp = ""
destPort = 0

def main():
	global udpSocket
	global destIp
	global destPort

	destIp = input("对方的ip：")
	destPort = int(input("对方的port："))

	udpSocket = socket(AF_INET, SOCK_DGRAM)
	udpSocket.bind(("",4567))

	tr = Thread(target=recvData)
	ts = Thread(target=sendData)
	
	tr.start()
	ts.start()

	tr.join()
	ts.join()

if __name__ == "__main__":
	main()
