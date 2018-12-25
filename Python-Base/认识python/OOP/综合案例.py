class Game(object):

    top_score=0
    def __init__(self,player_name):
        self.name=player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" %cls.top_score)

    def start_game(self):
        print("%s 开始游戏。。。" %self.name)

Game.show_help()#静态方法
Game.show_top_score()#类方法

game=Game("小明")#对象的实例方法
game.start_game()
