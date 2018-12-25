#导入随机工具包 导入语句放在文件顶部
import random


player=int(input("请输入您要出的拳 石头1/剪刀2/布3"))

computer=random.randint(1,3)

print("玩家出的是 %d - 电脑出的是 %d" %(player,computer))

if ((player==1 and computer==2)
        or(player==2 and computer==3)  #8个缩进 两个tab
        or(player==3 and computer==1)):

    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")