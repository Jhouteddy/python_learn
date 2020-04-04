# 載入內建的sys模組並取得資訊
import sys
sys.path.append("modules")
import geometry
print(sys.platform)
print(sys.maxsize)

# 建立geometry模組，載入使用
result = geometry.distance(1, 1, 5, 5)
print(result)
result = geometry.slope(1, 2, 5, 6)
print(result)

# 調整搜尋模組的路徑
print(sys.path)
