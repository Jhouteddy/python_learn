# 網路連線
import json
import urllib.request as request
src = "https://www.ntu.edu.tw"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8")  # 取得台大網站的原始碼(HTML,CSS,JS)
print(data)

# 串接截取公開資料
src = "http://117.56.59.17/OpenData/API/Rain/Get?stationNo=&loginId=open_rain&dataKey=85452C1D"
with request.urlopen(src) as response:
    data = json.load(response)  # 利用json模組處理 json 模組處理 json資料格式
print(data)


src = "http://117.56.59.17/OpenData/API/Rain/Get?stationNo=&loginId=open_rain&dataKey=85452C1D"
with request.urlopen(src) as response:
    data = json.load(response)  # 利用json模組讀取資料
#取得觀測站名稱, 並寫入檔案(weather.txt)
slist = data["data"]
with open("weather.txt", "w", encoding="utf=8") as file:
    for name in slist:
        file.write(name["stationName"]+"\n")
