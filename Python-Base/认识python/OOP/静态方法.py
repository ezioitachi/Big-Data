class Dog(object):

    @staticmethod#不访问实力属性和类属性
    def run():
        print("跑。。。")

Dog.run()#类即对象
