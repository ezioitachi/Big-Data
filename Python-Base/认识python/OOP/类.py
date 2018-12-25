class Cat:
    def eat(self):
        print("%s 爱吃鱼" %self.name)

    def drink(self):
        print("%s 要喝水" %self.name)

tom=Cat()
tom.name="Tom" #不推荐

tom.eat()
tom.drink()



