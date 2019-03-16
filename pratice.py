class HouseItem:
    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s], 面积为 %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.area = area
        self.free_area = area
        self.house_type = house_type
        self.item_list = []

    def __str__(self):

        return ("户型 %s \n总面积%.2f \n 剩余面积%.2f\n 家具 %s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加%s" % item)

        if self.free_area < item.area:
            return None
        self.item_list.append(item.name)
        self.free_area -= item.area


chest = HouseItem('衣柜', 5)
table = HouseItem('桌子', 10)
# print(chest)
# print(table)
my_house = House('三室一厅', 70)
my_house.add_item(chest)
print(my_house)


