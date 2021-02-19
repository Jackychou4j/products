#先檢查檔案是否有在電腦裡面，因為沒有的話會造成程式當掉
import os #可以用os(作業系統)來檢查，因為普通的程式碼沒有權限做到
def read_file(filename):
    #讀取檔案
    products = []
    with open(filename, "r", encoding = "utf-8") as f:
        for line in f: #一行一行讀取，所以變數取line
            if "商品,價格" in line:
                continue #跟break一樣，continue的功能：直接跳到下一個迴圈，在這邊的意思就是不會把"商品,價格"這個字串存在清單
                name, price = line.strip().split(",") #strip：去掉換行符號 #split：切割，每行遇到逗點就切一刀，切割完的結果會變清單
            #上面這樣是把清單的名稱跟價格分別存到兩個變數
                products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
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
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], "的價格是", p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, "w", encoding="utf-8") as f: #程式語言只要open檔案，一定要有close，python的with可以幫忙節省掉close的步驟 #如果欄位有輸入到中文，需要使用編碼(utf-8)
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0] + "," +p[1] + "\n") #\n 是換行
            #在csv檔案裡面，如果有逗點就會分在右邊一格

def main():
    filename = "products.csv"
    if os.path.isfile(filename):
        print("檔案找到了")
        products = read_file(filename)
    else:
        print("檔案沒找到...")

    products = user_input(products)
    print_products(products)
    write_file(filename, products)
main()