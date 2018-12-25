class MusicPlyer(object):
    instance=None# 类属性

    init_flag=False

    def __new__(cls, *args, **kwargs):#分配空间
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance

    def __init__(self):

        if MusicPlyer.init_flag:
            return
        print("初始化播放器")

        MusicPlyer.init_flag=True


player1=MusicPlyer()
print(player1)

player2=MusicPlyer()
print(player2)