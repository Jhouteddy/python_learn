import sys

# 列印有幾個參數

print('Number of arguments:', len(sys.argv), 'arguments.')

# 列印參數List

print('Argument List:', str(sys.argv))

# 檢查參數的數量,argv 的長度 注意檔名 test.py or test.exe 都等於一個參數

print(len(sys.argv))

# 如果長度不等於2 的話,則列印請輸入參數 test.exe hello 長度數量應該等於2

if len(sys.argv) != 2:
    print("Usage請輸入參數")
    sys.exit(1)

print(sys.argv[1])

# 執行完應該會列印 hello


def main():
    # intValue = int(sys.argv[1])#如果要將變數搞成數字的話可以使用 int()來轉
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
    print("===============")
    print(len(sys.argv))  # 參數一共有幾個
    print("===============")
    for x in sys.argv:
        print(x)


if __name__ == "__main__":
    main()
