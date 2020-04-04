# 集合的運算
s1 = {3, 4, 5}
print(10 not in s1)
s2 = {4, 5, 6, 7}
# 交集：取兩個集合中,相同的資料
s3 = s1 & s2
print(s3)
# 聯集：取兩個集合中的所有資料,但不重複取
s4 = s1 | s2
print(s4)
# 差集：從s1中,減去和s2重疊的部份
s5 = s1-s2
print(s5)
# 反交集：取兩個集合中,不重疊的部份
s6 = s1 ^ s2
print(s6)
# 把字串拆解成集合set(字串)
s = set("hello")
print(s)
print("o" in s)

# 字典的運算
dic = {"apple": "蘋果", "bug": "蟲蟲"}
print(dic["apple"])
# 判斷key是否存在
print("test" in dic)
# 刪除字典中的鍵值對
del dic["apple"]
print(dic)
# 從列表的資料產生字典
dic2 = {x: x*2 for x in [3, 4, 5]}
print(dic2)
