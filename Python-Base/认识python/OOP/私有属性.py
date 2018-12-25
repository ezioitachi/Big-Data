class Women:
    def __init__(self,name):

        self.name=name
        self.__age=18#私有属性,加两个下划线

    def __secret(self):#私有方法，加两个下划线
        print("%s 的年龄是 %d" %(self.name,self.__age))

xiaofang=Women("小芳")


#访问方法：私有属性

print(xiaofang._Women__age)

xiaofang._Women__secret()

