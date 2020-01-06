# python提供兩種序列結構：串列(list)、tuple

# 串列 用[]或list()建立
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print('weekdays=', weekdays)

another_empty_list = list()

# 用list()來江其他的資料類型轉換成串列
cat = list('cat')

a_tuple = ('ready', 'fire', 'aim')
aTuple = list(a_tuple)
print('aTuple=', aTuple)

birthday = '1/6/1952'
birth = birthday.split('/')
print('birth=', birth)

# 用[位移植]來取得一個項目並更改其值
items = ['apple', 'banana', 'cat', 'dog']
print("items=", items)
print("items[2]=", items[2])
print("items[-3]=", items[-3])
items[1] = 'baseketball'
print("change items[1], items=", items)


# 串列的串列
one = ['a', 'b', 'c']
two = ['d', 'e', 'f', 'g']
three = [3, 'h', 4, 'i']
all_num = [one, two, three]
print("all_num=", all_num)
print("all_num[1]=", all_num[1])
print("all_num[1][1]=", all_num[1][1])

# 用一個範圍的位移值來以slice取出項目
items = ['apple', 'banana', 'cat', 'dog']
print("items=", items)
print("items[0:2]=", items[0:2])
# 以2的間隔移動
print("items[::2]=", items[::2])
# 將串列反過來
print("將串列反過來 items[::-1]=", items[::-1])

# 用append()將項目附加結尾
items.append("egg")
print("add egg到items結尾 items=", items)
# 使用extend()或+=來結合串列
items = ['apple', 'banana', 'cat', 'dog']
print("items=", items)
others1 = ["egg", "fox"]
items.extend(others1)
print("新增others1後的items=", items)
others2 = ["gap", "hat"]
items += others2
print("新增others2後的items=", items)
# 用insert()與位移植來加入一個項目
items.insert(3, "three")
print("新增three在item的第三個位置 items=", items)
# 位移植超出串列結尾的位移植會將項目差至結尾
items.insert(10, "ten")
print("新增ten在item的第10個位置 將會新增至結尾 items=", items)

# 用del與位移植來刪除一個項目
# del是python陳述式
del items[3]
print("刪除item的第3個項目 items=", items)
# 用remove()與值來刪除項目
items.remove('ten')
print("刪除ten這個項目 items=", items)
# 用pop()與位移植來取得一個項目,並刪除它
# 若pop參數預設為-1
getPop = items.pop()
print("items.pop()=", getPop)
print("使用pop() items=", items)
getPop = items.pop(3)
print("items.pop(3)=", getPop)
print("使用pop(3) items=", items)
# 用index()與值來尋找某個項目的位移值
print("items.index('egg')=", items.index('egg'))
# 用in來測試值
print("'lion' in items =", 'lion' in items)
print("'fox' in items =", 'fox' in items)
# 用count()來算出某個值得出現次數
print("items.count('egg')=", items.count('egg'))

# 用join()來轉換成字串
# join()是split()的相反
joined = '*'.join(items)
print("用join來將items轉換程字串 joined=", joined)

# 用sort()來排序項目
# sort()會就地排序串列本身
# sorted()會排序串列,之後回傳副本
num = [2, 1, 4, 0, 6]
print("num=", num)
num.sort()
print("num.sort()=", num)

# 用len()來取得長度
print("len(items)=", len(items))

# 用＝來指派,用copy()來複製
# =指標的概念
a = [1, 2, 3]
print("a=", a)
b = a
print("b=", b)
a[0] = "hello"
print('a[0]="hello" a=', a)
print("b=", b)
# 可以使用以下方法,將串列的值複製到一個獨立、全新的串列
b = a.copy()
c = list(a)
d = a[:]

# Tuple
# tuple是不可變的,定義後無法添加或刪除或更改他的項目
# 用()來建立tuple
item_tuple = ("lion", "bike", "cat")
print("item_tuple=", item_tuple)

# tuple開箱(unpacking)
a, b, c = item_tuple
print("tuple開箱")
print("a=", a)
print("b=", b)
print("c=", c)

# tuple()轉換函是可將其他的東西做成tuple
items_tuple = tuple(items)
print("把items轉換程tuple items_tuple=", items_tuple)

# dictionary
# 字典(dictionary)
# 要建立dict,要用大括號包住以逗號分隔的 key:value
example_dict = {"day": "hello", "num": 50}
print("example_dict=", example_dict)

# 用dict()來轉換
tos = ("ab", "cd", "ef")
print(dict(tos))

# 可用[key]來添加或變更項目
item_dict = {"a": "apple"}
print("item_dict=", item_dict)
item_dict["b"] = "banana"
print("新增b:banana,item_dict=", item_dict)
item_dict["a"] = "ape"
print("修改a:ape,item_dict=", item_dict)

# 用update()來合併字典
# 若第二個dict與要合併的dict有相同key的時候,第二個dict的值會勝出
others_dict = {"c": "cat", "d": "duck"}
item_dict.update(others_dict)
print("合併others_dict,item_dict=", item_dict)

# 用del與key來刪除項目
del item_dict["d"]
print("刪除d,item_dict=", item_dict)
# 可用clear()或者重新指派一個空的dict來刪除所有項目

# 使用in來測試key
print("f in item_dict=", "f" in item_dict)
print("a in item_dict=", "a" in item_dict)

# 用[key]或者get()來取得一個項目
print("item_dict['a']=", item_dict["a"])
print("item_dict.get('f')=", item_dict.get('f'))
print("item_dict.get('b')=", item_dict.get('b'))

# 用keys()來取得所以key
item_keys = list(item_dict.keys())
print("all item_keys=", item_keys)
# 用values()來取得所有的值
item_values = list(item_dict.values())
print("all item_values=", item_values)
# 用items()來取得所有的key/values
item_items = list(item_dict.items())
print("all item_items=", item_items)

# 用＝來指派,用copy()來複製(與list相同)
# =指標的概念
