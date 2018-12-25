def input_password():

    pwd=input("请输入密码：")

    if len(pwd)>=8:
        return pwd

    print("主动抛出异常")

    raise Exception("密码长度不够")



try:
    print(input_password())
except Exception as result:
    print(result)
