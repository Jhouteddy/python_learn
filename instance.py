# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self):
        self.x = 3
        self.y = 4
    # 定義實體方法

    def show(self):
        print(self.x, self.y)

    def distance(self, targetX, targetY):
        return(((self.x-targetX)**2+(self.y-targetY)**2))**0.5


p1 = Point()
print(p1.x, p1.y)
p1.show()
result = p1.distance(0, 0)
print(result)
# FullName 實體物件的設計：分開紀錄姓,名資料的全名


class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last


name1 = FullName("c.w.", "peng")
print(name1.first, name1.last)


# File 實體物件的設計：包裝檔案讀取的程式
class File:
    def __init__(self, name):
        self.name = name
        self.file = None  # 尚未開啟檔案

    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")

    def read(self):
        return self.file.read()


f1 = File("data.txt")
f1.open()
data = f1.read()
print(data)
