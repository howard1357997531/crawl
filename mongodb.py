from pymongo import MongoClient
import urllib.parse
import datetime
import EXRate
from EXRate import currenct_list

password = "VFGMLSRhMnLVTcFI"
url = f"mongodb://gary821121:{password}@ac-b69jo4m-shard-00-00.a3yt3v4.mongodb.net:27017,ac-b69jo4m-shard-00-01.a3yt3v4.mongodb.net:27017,ac-b69jo4m-shard-00-02.a3yt3v4.mongodb.net:27017/?ssl=true&replicaSet=atlas-npkx3m-shard-0&authSource=admin&retryWrites=true&w=majority"
Authdb = "test-good1"
stockDB = "mydb"
currencyDB = "users"
dbname = "test-good1"

def constructor_stock():
    client = MongoClient(url)
    db = client[stockDB]
    return db

def constructor_currency():
    client = MongoClient(url)
    db = client[currencyDB]
    return db

def write_my_currency(userID, user_name, currency, condition, target_price):
    db = constructor_currency()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_currency": currency})
    content = ""
    if is_exit != None: return update_my_currency(user_name, currency, condition, target_price)
    else:
        collect.insert_one({
            "userID": userID,
            "favorite_currency": currency,
            "condition": condition,
            "price": target_price,
            "tag": "currency",
            "date_info": datetime.datetime.now()
        })
        return f"{currenct_list[currency]}已新增至您的外幣清單"

def update_my_currency(user_name, currency, condition, target_price):
    db=constructor_currency()
    collect = db[user_name]
    collect.update_many({"favorite_currency": currency}, {'$set': {'condition': condition, 'price': target_price}})
    return f'{currenct_list[currency]}更新成功'

def show_my_currency(userID ,user_name):
    db = constructor_currency()
    collect = db[user_name]
    dataList = list(collect.find({'userID': userID}))
    if dataList == []: return "您的外幣清單為空，請透過指令新增外幣至清單中"
    content=""
    for i in range(len(dataList)):
        content += EXRate.showCurrency(dataList[i]["favorite_currency"])
    return content

def delete_my_currency(user_name, currency):
    db = constructor_currency()
    collect = db[user_name]
    collect.delete_one({'favorite_currency': currency})
    return currenct_list[currency] + '刪除成功'

def delete_my_allcurrency(user_name, userID):
    db = constructor_currency()
    collect = db[user_name]
    collect.delete_many({'userID': userID})
    return '外幣清單已清空'

# ----------------------新增使用者股票-------------------------
def write_my_stock(userID ,user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collect = db[user_name]
    is_exist = collect.find_one({"favorite_stock": stockNumber})
    if is_exist != None:
        content = update_my_currency(user_name, stockNumber, condition, target_price)
        return content
    else:
        collect.insert_one({
            "userID": userID,
            "favorite_stock": stockNumber,
            "condition": condition,
            "price": target_price,
            "tag": "stock",
            "date_info": datetime.datetime.now()
        })
    return f"{stockNumber}已新增至您的股票清單"

def update_my_stock(user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collect = db[user_name]
    collect.update_many({"favorite_stock": stockNumber}, {'$set': {'condition': condition, 'price': target_price}})
    content = f'股票{stockNumber}更新成功'
    return content

def show_stock_setting(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    dataList = list(collect.find({'userID': userID}))
    if dataList == []: return "您的外幣清單為空，請透過指令新增外幣至清單中"
    content="您清單中的選股條件為: \n"
    for i in range(len(dataList)):
        content += f'{dataList[i]["favorite_stock"]} {dataList[i]["condition"]} {dataList[i]["price"]}\n'
    return content

def delete_my_stock(user_name, stockNumber):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_one({'favorite_stock': stockNumber})
    return stockNumber + '刪除成功'

def delete_my_allstock(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_many({'userID': userID})
    return '全部股票刪除成功'


