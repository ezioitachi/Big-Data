
file_read=open("README","r+") #打开
file_write=open("README_1","w")

file_read.write("\nhello")

while True:
    text=file_read.readline() #一行一行的读写

    if not text:
        break

    file_write.write(text)



file_read.close() #关闭