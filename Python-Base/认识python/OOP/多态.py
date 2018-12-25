class Dog(object):
    def __init__(self,name):
        self.name=name

    def game(self):
        print("%s 蹦蹦跳跳。。。" %self.name)

class XiaoTianQuan(Dog):

    def game(self):
        print("%s 飞到天上。。。" %self.name)

class Person(object):

    def __init__(self,name):
        self.name=name

    def game_with_dog(self,dog):
        print("%s 和 %s 和快乐的玩耍。。。" %(self.name,dog.name))

        dog.game()

wangcai=XiaoTianQuan("飞天wangcai")


xiaoming=Person("xiaoming")

xiaoming.game_with_dog(wangcai)

