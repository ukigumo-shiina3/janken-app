import csv

# data = '''11,12,13,14
# 21,22,23,24
# 31,32,33,34
# '''

data = [41,42,43,44]

# with open('sample.csv', mode='w') as f:
#     f.write(data)

# with open('sample.csv', mode='r') as f: #as f→ファイルオブジェクトに名前をつける
#     reader = csv.reader(f) #reader→CSVファイル内の行を一つずつ読み取る
#     for row in reader:
#             print(row)

# with open('sample.csv', mode='r') as f:
#     reader = csv.reader(f, delimiter=' ') #delimiter→指定した箇所にカンマを入れる
#     for row in reader:
#             print(row)

with open('sample.csv', mode='a+', newline='') as f: #'a+'→追記の読み書き両用モード newline→余計な改行が入らないようにする
    writer = csv.writer(f)
    writer.writerow(data) #writerow→末尾までいく

    f.seek(0) #先頭に戻す
    print(f.read())