#士兵 开火
#枪 发射，填装子弹

class Gun:
    def __init__(self,model):

        self.model=model
        self.bullet_count=0

    def add_bullet(self,count):

        self.bullet_count+=count

    def shoot(self):

        if self.bullet_count<=0:
            print("没有子弹")
            return

        self.bullet_count-=1
        print("piu piu piu...[%d]" %self.bullet_count)

class Soldier:
    def __init__(self,name):

        self.name=name
        self.gun=None#新兵没有枪

    def fire(self):
        if self.gun==None:
            print("%s 还没有枪" %self.name)
            return
        print("[%s]:冲啊。。。" %self.name)

        self.gun.add_bullet(50)

        self.gun.shoot()


ak47=Gun("ak47")

xusanduo=Soldier("许三多")
xusanduo.gun=ak47
xusanduo.fire()
print(xusanduo.gun)

