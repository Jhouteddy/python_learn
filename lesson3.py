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
