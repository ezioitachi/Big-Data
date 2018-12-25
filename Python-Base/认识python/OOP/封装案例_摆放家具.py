#户型，总面积，家具名称列表
#席梦思4，衣柜2，餐桌1.5

class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __del__(self):

        return "%s 的占地 %.2f 平米" %(self.name,self.area)


class House:
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area

        self.free_area=area
        self.item_list=[]

    def __str__(self):
        return ("户型 %s\n 总面积：%.2f[剩余面积：%.2f]\n家具：%s"
                %(self.house_type,
                  self.area,
                  self.free_area,
                  self.item_list))

    def add_item(self,item):
        print("要添加 %s" %item.name)

        if item.area> self.free_area:
            print("过大，无法添加")
            return

        self.item_list.append(item.name)

        self.free_area-=item.area



bed=HouseItem("席梦思",4)
chest=HouseItem("衣柜",2)
table=HouseItem("餐桌",1.5)

my_home=House("两室一厅",100)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)


print(my_home)