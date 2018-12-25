age = int(input("请输入年龄"))

if age >= 18:
    print("已经成年")  #四个空格 或 一个tab, 缩进部分属于if判断块
    print("欢迎")
else:
    print("未成年")

#elif语法 不同条件 不同执行 必须在if之下

holiday_name=input("什么节日")

if holiday_name=="情人节":
    print("买玫瑰")
    print("看电影")
elif holiday_name=="平安夜":
    print("买苹果，吃大餐")
elif holiday_name=="声日":
    print("买蛋糕")

else:
    print("每天都是节日啊")
