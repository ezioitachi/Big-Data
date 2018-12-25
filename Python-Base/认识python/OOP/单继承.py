class Animal:
    def eat(self):
        print("eat...")
    def drink(self):
        print("drink...")
    def run(self):
        print("run...")
    def sleep(self):
        print("sleep...")




class Dog(Animal):#子类拥有父类的所有方法

    def bark(self):
        print("wang")

class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")
    def bark(self):
        print("神一样的叫唤。。。")
        super().bark()
        print("&^*#!*%$!*%@*#")





wangcai=Dog()
wangcai.eat()
wangcai.run()
wangcai.drink()
wangcai.bark()
wangcai.sleep()

xtq=XiaoTianQuan()
xtq.bark()


