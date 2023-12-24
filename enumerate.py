seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons)) # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')] タプル型のオブジェクト #数字付きの関数で返してくれる

prices = [100,200,300]
quantities = [1,2,3]

menu = ['coffee', 'tea', 'cake']
for (item, price, quantity) in zip(menu,prices,quantities):
    print(item, price*quantity) #coffee 100 tea 400 cake 900