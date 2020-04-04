import random
import statistics as stat
# 隨機模組
# 隨機選取
data = random.choice([1, 5, 6, 8, 9, 20])
print(data)
data2 = random.sample([1, 5, 6, 8, 9, 20], 3)
print(data2)
# 洗牌的概念
d = [1, 5, 8, 20]
random.shuffle(d)
print(d)
# 隨機取得亂術
d1 = random.random()  # 0~1之間的隨機亂術
print(d1)
d2 = random.uniform(60, 100)  # 指定在區間的隨機亂術
print(d2)
d3 = random.normalvariate(100, 10)  # 平均數100，標準差10，得到的資料多在90～110之間
print(d3)

# 統計模組
s = stat.mean([1, 2, 3, 4, 5, 8, 100])  # 平均數
print(s)
s1 = stat.median([1, 2, 3, 4, 5, 8, 100])  # 中位數
print(s1)
s2 = stat.stdev([1, 2, 3, 4, 5, 8, 10])  # 標準差
print(s2)
