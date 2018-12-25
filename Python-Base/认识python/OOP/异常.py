try:
    num=int(input("输入整数")) #不确定正确的代码
except:
    print("请输入正确的整数")# 错误的处理代码

print("-"*50)

###############最后一行的第一个单词是错误类型
try:
    num1=int(input("输入正确的整数："))
    result=8/num1
    print(result)
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("尝试成功")
finally:
    print("都会执行")

print("-"*50)

