# -*- coding: utf-8 -*-
''' 
即時股價
'''
import requests
import datetime
import json
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from bs4 import BeautifulSoup
import imgur
from matplotlib.font_manager import FontProperties # 設定字體
from linebot.models import *
font_path = matplotlib.font_manager.FontProperties(fname='msjh.ttf')

emoji_upinfo = u'\U0001F447'
emoji_midinfo = u'\U0001F538'
emoji_downinfo = u'\U0001F60A'

def get_stock_name(stockNumber):
    try:
        url = f'https://tw.stock.yahoo.com/q/q?s={stockNumber}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find_all(text='成交')[0].parent.parent.parent
        stock_name = table.select('tr')[1].select('td')[0].text.strip('加到投資組合')
        return stock_name
    except:
        return "no"

def stock_trend(stockNumber, msg):
    stock_name = get_stock_name(stockNumber)
    end = datetime.datetime.now()
    date = end.strftime('%Y%m%d')
    year = str(int(date[0:4]) - 1)
    month = date[4:6]

    import pandas
    from pandas_datareader import data as pdr
    import yfinance as yfin
    yfin.pdr_override()
    stock = pdr.get_data_yahoo(stockNumber + '.TW', start='2023-12-12', end='2023-12-16')

    plt.figure(figsize=(12, 6))
    plt.plot(stock["Close"], '-', label='收盤價')
    plt.plot(stock["High"], '-', label='最高價')
    plt.plot(stock["Low"], '-', label='最低價')
    plt.title(stock_name + '收盤價年走勢', loc='center', fontsize=20, fontproperties=font_path)
    plt.xlabel('日期', fontsize=20, fontproperties=font_path)
    plt.ylabel('價格', fontsize=20, fontproperties=font_path)
    plt.grid(True, axis='y') # 網格線
    plt.legend(fontsize=14, prop=font_path)
    plt.savefig(msg + '.png')
    plt.show()
    plt.close()
    return imgur.showImgur(msg)

