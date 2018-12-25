row = 1

while row <= 9:
    col = 1

    while col <=row:
        #print("*", end="")
        print("%d*%d=%d" %(col,row, col*row), end="\t")  #\t 制表符 垂直方向保持对齐
        col+=1

    #print("%d" %row)
    print("")

    row+=1

print("hello\nhello")# \n换行
print("hello\"hello")# \" 输出引号