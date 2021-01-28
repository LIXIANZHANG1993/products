import os #operating system 

#讀取檔案
products = []
if os.path.isfile('products.csv'): #檢查檔案在不在
    print('歷史紀錄檔已讀取')
    with open('products.csv', 'r') as f: # encoding= 'utf-8'
        for line in f:
            if '商品,價格' in line:
                continue  #跳到下一回
            name, price= line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('搜尋不到歷史紀錄檔')

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    price = int(price)
    products.append([name, price]) 
print(products) 

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w') as f: # encoding= 'utf-8'
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')   