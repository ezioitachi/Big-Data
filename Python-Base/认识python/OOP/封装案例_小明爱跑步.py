#小明75kg, 跑步-0.5kg,吃饭+1kg
#小美45kg,

class Person:
    def __init__(self,name,weight):

        self.name=name
        self.weight=weight

    def __str__(self):

        return "我的名字叫 %s， 体重是%.2fkg" %(self.name,self.weight)

    def run(self):
        print("%s 爱跑步" %self.name)
        self.weight-=0.5
    def eat(self):
        print("%s 是吃货" %self.name)
        self.weight+=1

xiaoming=Person("小明",75)
xiaomei=Person("小美",45)

xiaoming.eat()
xiaoming.run()

xiaomei.run()
xiaomei.eat()


print(xiaoming)
print(xiaomei)