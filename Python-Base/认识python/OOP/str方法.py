
class Cat:
    def __init__(self,new_name):

        self.name=new_name

        print("%s 爱吃鱼" %self.name)

    def __del__(self):
        print("%s 走了" %self.name)

    def __str__(self):  #必须返回字符串

        return "我是[%s]" %self.name

tom=Cat("Tom")
print(tom)
