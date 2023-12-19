#載入LineBot所需要的套件
'''
pip install flask
pip install line-bot-sdk
pip install twstock
pip install twder
pip install lxml
pip install requests
pip install beautifulsoup4
pip install matplotlib
pip install pandas
pip install schedule
pip install imgurpython
pip install pandas-datareader
pip install yfinance
'''
from flask import Flask, request, abort
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from bs4 import BeautifulSoup
import requests
import twstock
import twder
import datetime
import re

from events import *
from line_bot import * 
import EXRate
import Msg_Template
import mongodb
import stockprice

app = Flask(__name__)


def Usage(event):
    push_msg(event,"    🌟🌟 查詢方法 🌟🌟   \
                    \n\
                    \n☢本機器人可查詢油價及匯率☢\
                    \n\
                    \n⑥ 油價通知 ➦➦➦ 輸入油價報你知\
                    \n⑥ 匯率通知 ➦➦➦ 輸入查詢匯率\
                    \n⑦ 匯率兌換 ➦➦➦ 換匯USD/TWD\
                    \n⑦ 自動推播 ➦➦➦ 自動推播")

def push_msg(event,msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id,TextSendMessage(text=msg))
    except:
        room_id = event.source.room_id
        line_bot_api.push_message(room_id,TextSendMessage(text=msg))

# def oil_price():
#     target_url = 'https://gas.goodlife.tw/'
#     rs = requests.session()
#     res = rs.get(target_url, verify=False)
#     res.encoding = 'uft-8'
#     soup = BeautifulSoup(res.text, 'html.parser')
#     title = soup.select('#main')[0].text.replace('\n', '').split('(')[0]
#     gas_price = soup.select('#gas-price')[0].text.replace('\n\n\n', '').replace(' ', '')
#     cpc = soup.select('#cpc')[0].text.replace(' ', '')
#     content = '{}\n{}{}'.format(title, gas_price, cpc)
#     return content

# 抓使用者設定它關心的股票
def cache_users_stock():
    db=mongodb.constructor_stock()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({"tag": 'stock'}))
        users.append(cel)
    return users

# 抓使用者設定它關心的股票
def cache_users_currency():
    db=mongodb.constructor_currency()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({"tag": 'currency'}))
        users.append(cel)
    return users

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

from urllib.parse import parse_qsl
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    msg = str(event.message.text).upper().strip() # 使用者輸入的內容
    profile = line_bot_api.get_profile(event.source.user_id)
   
    usespeak=str(event.message.text) #使用者講的話
    uid = profile.user_id #使用者ID
    user_name = profile.display_name #使用者名稱
    ######################## 使用說明 選單 油價查詢################################
    
    if event.message.text == "油價報你知":
        oil_price(event)

    elif event.message.text == "使用說明":
        Usage(event)
        print(user_name)

    ################################ 匯率區 ##########################################
    if re.match('匯率大小事', msg):
        btn_msg = Msg_Template.stock_reply_rate()
        line_bot_api.reply_message(event.reply_token, btn_msg)

    if re.match('換匯[A-Z]{3}/[A-Z{3}]', msg):
        # line_bot_api.reply_message(event.reply_token, TextSendMessage('將為您做外匯運算'))
        content = EXRate.getExchangeRate(msg)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(content)
            )

    if re.match('幣別種類', msg):
        message = Msg_Template.show_Button()
        line_bot_api.reply_message(event.reply_token, message)

    if re.match('CT[A-Z]{3}', msg):
        currency = msg[2:5] # 外幣代號
        if EXRate.getCurrencyName(currency) == '無可支援外幣':
            line_bot_api.reply_message(event.reply_token, TextSendMessage("無可支援外幣"))
            return
        # line_bot_api.reply_message(event.reply_token, TextSendMessage("稍等一下，將會給您匯率走勢圖"))
        text = TextSendMessage("稍等一下，將會給您匯率走勢圖")
        cash_imgurl = EXRate.cash_exrate_sixMonth(currency)
        if cash_imgurl == '現金匯率無資料可分析':
            # line_bot_api.reply_message(event.reply_token, TextSendMessage("現金匯率1無資料可分析"))
            image = TextSendMessage("現金匯率1無資料可分析")
        else:
            # line_bot_api.reply_message(event.reply_token, ImageSendMessage(
            #     original_content_url=cash_imgurl,
            #     preview_image_url=cash_imgurl
            # ))
            image = ImageSendMessage(
                original_content_url=cash_imgurl,
                preview_image_url=cash_imgurl
            )
        
        spot_imgurl = EXRate.spot_exrate_sixMonth(currency)
        if spot_imgurl == "即期匯率無資料可分析":
            # line_bot_api.reply_message(event.reply_token, TextSendMessage("即期匯率無資料可分析"))
            image2 = TextSendMessage("即期匯率無資料可分析")
        else:
            # line_bot_api.reply_message(event.reply_token, ImageSendMessage(
            #     original_content_url=spot_imgurl,
            #     preview_image_url=spot_imgurl
            # ))
            image2 = ImageSendMessage(
                original_content_url=spot_imgurl,
                preview_image_url=spot_imgurl
            )
        
        btn_msg = Msg_Template.realtime_currency_other(currency)
        line_bot_api.reply_message(event.reply_token, [text, image, image2, btn_msg])

    if re.match('外幣[A-Z]{3}', msg):
        currency = msg[4:7]
        currency_name = EXRate.getCurrencyName(currency)
        if currency_name == "無可支援外幣": content = "無可支援外幣"
        # USD>30 (設定USD條件是大於30塊)
        elif re.match('新增外幣[A-Z]{3}[<>][0-9]', msg):
            content = mongodb.write_my_currency(uid, user_name, currency, msg[7:8], msg[8:])
        else:
            content = mongodb.write_my_currency(uid, user_name, currency, "未設定", "未設定")
        
        # line_bot_api.p
        # sh_message(uid, TextSendMessage(content))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))
    
    if re.match('我的外幣', msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下，匯率查詢中...'))
        content = mongodb.show_my_currency(uid, user_name)
        # line_bot_api.push_message(uid, TextSendMessage(content))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    if re.match('刪除外幣[A-Z]{3}', msg):
        content = mongodb.delete_my_currency(user_name, msg[4:7])
        # line_bot_api.push_message(uid, TextSendMessage(content))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    if re.match('清空外幣', msg):
        content = mongodb.delete_my_allcurrency(user_name, uid)
        # line_bot_api.push_message(uid, TextSendMessage(content))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    ################################ 股票區 ##########################################
    if re.match('P[0-9]{4}', msg):
        stockNumber = msg[1:]
        text = TextSendMessage('稍等一下，股價走勢繪製中...')
        trend_imgurl = stockprice.stock_trend(stockNumber, msg)
        image = ImageSendMessage(
                original_content_url=trend_imgurl,
                preview_image_url=trend_imgurl
            )
        btn_msg = Msg_Template.stock_reply_other(stockNumber)
        line_bot_api.reply_message(event.reply_token, [text, image, btn_msg])

    if event.message.text == "股票大小事":
        # line_bot_api.push_message(uid, TextSendMessage("請輸入#股票代號......"))
        line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入#股票代號......"))
    
    # 關注0050>130 (大於130)
    #新增使用者關注的股票到mongodb EX:關注2330>xxx
    if re.match('關注[0-9]{4}[<>][0-9]', msg):
        stockNumber = msg[2:6]
        content = mongodb.write_my_stock(uid, user_name, stockNumber, msg[6:7], msg[7:])
        # line_bot_api.push_message(uid, TextSendMessage(content))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # 查詢股票篩選條件清單
    if re.match('股票清單', msg):
        text = TextSendMessage('稍等一下，股票查詢中...')
        content = mongodb.show_stock_setting(user_name, uid)
        # line_bot_api.push_message(uid, TextSendMessage(content))
        line_bot_api.reply_message(event.reply_token, [text, TextSendMessage(content)])

    if re.match('刪除股票[0-9]{4}', msg):
        content = mongodb.delete_my_stock(user_name, msg[4:])
        # line_bot_api.push_message(uid, TextSendMessage(content))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    if re.match('清空股票', msg):
        content = mongodb.delete_my_allstock(user_name, uid)
        # line_bot_api.push_message(uid, TextSendMessage(content))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(content))

    # 0050
    if (msg.startswith('#')):
        text = msg[1:]
        content = ''

        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp'] + 8*60*60)
        my_time = my_datetime.strftime('%H:%M:%S')

        content += '%s (%s) %s\n' %(stock_rt['info']['name'], stock_rt['info']['code'], my_time)
        content += '現價: %s / 開盤: %s\n' %(stock_rt['realtime']['latest_trade_price'], stock_rt['realtime']['open'])
        content += '最高: %s / 最低: %s\n' %(stock_rt['realtime']['high'], stock_rt['realtime']['low'])
        content += '量: %s\n' %(stock_rt['realtime']['accumulate_trade_volume'])

        stock = twstock.Stock(text)
        content += '------\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s\n' %(date5[i].strftime('%Y-%m-%d'), price5[i])
        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
    
    ################################ 目錄區 ##########################################
    if event.message.text == "開始玩":
        buttons_template = TemplateSendMessage(
        alt_text='目錄選項',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/JWZwNT0.jpg',
                        title='請選擇服務',
                        text='請選擇',
                        actions=[
                            MessageAction(
                                label='油價報你知',
                                text='油價報你知'
                            ),
                            MessageAction(
                                label='股價查詢',
                                text='股價查詢'
                            ),
                            MessageAction(
                                label='使用說明',
                                text='使用說明'
                            )
                        ]
                    ),
                CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/9VN2hO4.jpg',
                        title='選擇服務',
                        text='請選擇',
                        actions=[
                            MessageAction(
                                label='other bot',
                                text='imgur bot'
                            ),
                            MessageAction(
                                label='股票大小事',
                                text='股票大小事'
                            ),
                            URIAction(
                                label='奇摩股市',
                                uri='https://tw.stock.yahoo.com/us/?s=NVS&tt=1'
                            )
                        ]
                    ),
                CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/AnhYPmN.jpg',
                        title='選擇服務',
                        text='請選擇',
                        actions=[
                            MessageAction(
                                label='自動推播',
                                text='自動推播'
                            ),
                            URIAction(
                                label='財經PTT',
                                uri='https://www.ptt.cc/bbs/Finance/index.html'
                            ),
                            URIAction(
                                label='google搜尋引擎',
                                uri='https://www.google.com'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

    if re.match("股價提醒", msg):
        import schedule
        import time
        # 查看當前股價
        def look_stock_price(stock, condition, price, userID):
            print(userID)
            url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
            list_req = requests.get(url)
            soup = BeautifulSoup(list_req.content, "html.parser")
            getstock = soup.find('span', class_='Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)').string
            content = stock + "當前股市價格為: " +  getstock
            if condition == '<':
                content += "\n篩選條件為: < "+ price
                if float(getstock) < float(price):
                    content += "\n符合" + getstock + " < " + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == '>':
                content += "\n篩選條件為: > "+ price
                if float(getstock) > float(price):
                    content += "\n符合" + getstock + " > " + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == "=":
                content += "\n篩選條件為: = "+ price
                if float(getstock) == float(price):
                    content += "\n符合" + getstock + " = " + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
        # look_stock_price(stock='2002', condition='>', price=31)
        def job():
            print('HH')
            dataList = cache_users_stock()
            # print(dataList)
            for i in range(len(dataList)):
                for k in range(len(dataList[i])):
                    print(dataList[i][k])
                    look_stock_price(dataList[i][k]['favorite_stock'], dataList[i][k]['condition'], dataList[i][k]['price'], dataList[i][k]['userID'])
        schedule.every(30).seconds.do(job).tag('daily-tasks-stock'+uid,'second') #每10秒執行一次
        #schedule.every().hour.do(job) #每小時執行一次
        #schedule.every().day.at("17:19").do(job) #每天9點30執行一次
        #schedule.every().monday.do(job) #每週一執行一次
        #schedule.every().wednesday.at("14:45").do(job) #每週三14點45執行一次

        # 無窮迴圈
        while True: 
            schedule.run_pending()
            time.sleep(1)

    ################################ 目錄區 ##########################################
    if re.match("匯率推播", msg):
        import schedule
        import time
        # 查看當前股價
        def look_currency_price(currency, condition, price, userID):
            realtime_currency = (twder.now(currency))[4]
            currency_name = mongodb.currenct_list[currency]
            content = currency_name + '當前即期賣出價格為: ' + str(realtime_currency)
            if condition == '<':
                content += "\n篩選條件為: < "+ price
                if float(realtime_currency) < float(price):
                    content += "\n符合" + realtime_currency + " < " + price + "的篩選條件"
                    # line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == '>':
                content += "\n篩選條件為: > "+ price
                if float(realtime_currency) > float(price):
                    content += "\n符合" + realtime_currency + " > " + price + "的篩選條件"
                    # line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == "=":
                content += "\n篩選條件為: = "+ price
            elif condition == "未設定":
                content += "\n尚未設置篩選條件,請設定您想要的目標價格條件，如: 新增外幣"+ currency + ">10"
            else:
                content += "\n無法判定此外幣設定的篩選條件"
            
            line_bot_api.push_message(userID, TextSendMessage(text=content))

        def job_currency():
            print('HH')
            dataList = cache_users_currency()
            # print(dataList)
            for i in range(len(dataList)):
                for k in range(len(dataList[i])):
                    look_currency_price(dataList[i][k]['favorite_currency'], dataList[i][k]['condition'],
                                        dataList[i][k]['price'], dataList[i][k]['userID'])
        schedule.every(30).seconds.do(job_currency) #每10秒執行一次

        while True:
            schedule.run_pending()
            time.sleep(1)

@handler.add(PostbackEvent)
def handle_postback(event):
    #把傳進來的event儲存在postback.data中再利用parse_qsl解析data中的資料然後轉換成dict
    data = dict(parse_qsl(event.postback.data))

    if data.get('action') == 'select_currency':
        print(data.get('currency'))
        line_bot_api.reply_message(event.reply_token, TextSendMessage('請選擇匯率判斷條件'))
        bubble = []
if __name__ == "__main__":
    app.run()


