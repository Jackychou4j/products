products = []
while True:
    name = input("請輸入商品名稱:")
    if name == "q": #quit
        break
    price = input("請輸入商品價格:")
    p = []
    p.append(name)
    p.append(price) #7~9行可以寫成 p = [name, price] 
    products.append(p) #上面更省略可以寫成 products.append([name, price])
print("您的商品名稱與價格為:",products)

print(products[0][0])