class Tool(object): #记录母板特征

    count=0 #类属性

    @classmethod#类方法
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)


    def __init__(self,name):
        self.name=name

        Tool.count+=1

tool1=Tool("斧头")
tool2=Tool("榔头")
tool3=Tool("水桶")

tool3.count=99 #不会改变类属性的值

Tool.show_tool_count()
