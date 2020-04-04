import json
# 儲存檔案
file = open("data.txt", mode="w", encoding="utf8")  # 開啟
file.write("hello file\nSecond line\n中文測試")
file.close()
# 最佳實務寫法
with open("data2.txt", mode="w", encoding="utf8") as file:
    file.write("456\n123")

# 檔案讀取
sum = 0
with open("data2.txt", mode="r", encoding="utf8") as file:
    for line in file:
        sum += int(line)
print(sum)

# 使用json格式讀取，複寫檔案
with open("config.json", mode="r") as file:
    data = json.load(file)
print("name", data["name"])
print("version", data["version"])
# 把最新的資料複寫回檔案中
data["name"] = "New Name"
with open("config.json", mode="w") as file:
    json.dump(data, file)
