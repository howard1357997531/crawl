import requests
from bs4 import BeautifulSoup
from linebot.models import *
from line_bot import line_bot_api

def oil_price(event):
    url = 'https://gas.goodlife.tw/'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    time = soup.select('#main')[0].select('.update')[0].text.split('(')[0].strip()

    # 即時國際油價期貨
    national_oil_title = soup.select('#rate')[0].select('.alt')[0].text.strip()

    national_oil = []
    for i in range(3):
        oil = soup.select('#rate')[0].select('.alt')[i+1].text.replace('\n', '').strip().split("\xa0")
        national_oil.extend([oil[0].replace(':', ': '), oil[-1]])

    # 調整
    oil_adjust = []
    oil1 = soup.select('#gas-price')[0].select('.alt')[0].text.strip().replace('\n', ' ')
    oil = soup.select('#gas-price')[0].select('.alt')[1].text.strip().replace('\xa0', '').split('中油吸收')
    oil2 = '原應調整:' + oil[0].replace('原應調整', '')
    oil3 = '中油吸收:' + oil[1]
    oil_adjust.extend([oil1, oil2, oil3])

    # 中油油價已公告: 明日汽油每公升
    oil_change = []
    oil = soup.select('#gas-price')[0].select('.main')[0]
    oil1 = oil.select('p')[0].text.strip()
    oil2 = oil.select('h2')[0].text.strip()
    oil_change.extend([oil1, oil2])

    # 今日中油油價
    today_oil_price1 = []
    for i in range(4):
        oil = soup.select('#cpc')[0].select('li')[i].text.split('\n')[-1]
        today_oil_price1.append(oil)

    # 今日台塑油價
    today_oil_price2 = []
    for i in range(4):
        oil = soup.select('#main')[0].select('ul')[-1].select('li')[i].text.split('\n')[-1]
        today_oil_price2.append(oil)

    bubble = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "油價公告",
        "weight": "bold",
        "color": "#616161",
        "size": "xxl",
        "align": "center"
      },
      {
        "type": "text",
        "text": time,
        "size": "xs",
        "color": "#e0e0e0",
        "wrap": True,
        "align": "center",
        "margin": "xs"
      },
      {
        "type": "separator",
        "margin": "xs"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "md",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": national_oil_title,
            "size": "sm",
            "color": "#5c6bc0",
            "weight": "bold",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": national_oil[0],
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": national_oil[1],
                "size": "xxs",
                "color": "#e0e0e0",
                "align": "end"
              }
            ],
            "alignItems": "center"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": national_oil[2],
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": national_oil[3],
                "size": "xxs",
                "color": "#e0e0e0",
                "align": "end"
              }
            ],
            "alignItems": "center"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": national_oil[4],
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": national_oil[5],
                "size": "xxs",
                "color": "#e0e0e0",
                "align": "end"
              }
            ],
            "alignItems": "center"
          },
          {
            "type": "separator",
            "margin": "sm"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": oil_adjust[0],
                "size": "sm",
                "color": "#555555",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": oil_adjust[1],
                "size": "sm",
                "color": "#555555",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": oil_adjust[2],
                "size": "sm",
                "color": "#555555",
                "flex": 0
              }
            ]
          },
          {
            "type": "separator",
            "margin": "sm"
          },
          {
            "type": "text",
            "text": oil_change[0],
            "align": "center",
            "margin": "md",
            "size": "sm",
            "color": "#5c6bc0",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": oil_change[1],
            "size": "3xl",
            "align": "center",
            "color": "#33691e"
          },
          {
            "type": "separator",
            "margin": "md"
          },
          {
            "type": "text",
            "text": "今日中油油價",
            "size": "sm",
            "color": "#5c6bc0",
            "weight": "bold",
            "margin": "md",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "92",
                    "align": "center",
                    "color": "#a1887f",
                    "weight": "bold"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs",
                "backgroundColor": "#e0e0e0"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "95",
                    "align": "center",
                    "color": "#a1887f",
                    "weight": "bold"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs",
                "backgroundColor": "#e0e0e0"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "98",
                    "align": "center",
                    "color": "#a1887f",
                    "weight": "bold"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs",
                "backgroundColor": "#e0e0e0"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "柴油",
                    "align": "center",
                    "color": "#a1887f",
                    "weight": "bold"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs",
                "backgroundColor": "#e0e0e0"
              }
            ],
            "spacing": "xs",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": today_oil_price1[0],
                    "align": "center",
                    "color": "#555555"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": today_oil_price1[1],
                    "align": "center",
                    "color": "#555555"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": today_oil_price1[2],
                    "align": "center",
                    "color": "#555555"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": today_oil_price1[3],
                    "align": "center",
                    "color": "#555555"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs"
              }
            ],
            "spacing": "xs"
          },
          {
            "type": "separator",
            "margin": "sm"
          },
          {
            "type": "text",
            "text": "今日台塑油價",
            "size": "sm",
            "color": "#5c6bc0",
            "weight": "bold",
            "margin": "md",
            "align": "center"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "92",
                    "align": "center",
                    "color": "#a1887f",
                    "weight": "bold"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs",
                "backgroundColor": "#e0e0e0"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "95",
                    "align": "center",
                    "color": "#a1887f",
                    "weight": "bold"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs",
                "backgroundColor": "#e0e0e0"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "98",
                    "align": "center",
                    "color": "#a1887f",
                    "weight": "bold"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs",
                "backgroundColor": "#e0e0e0"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "柴油",
                    "align": "center",
                    "color": "#a1887f",
                    "weight": "bold"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs",
                "backgroundColor": "#e0e0e0"
              }
            ],
            "spacing": "xs",
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": today_oil_price2[0],
                    "align": "center",
                    "color": "#555555"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": today_oil_price2[1],
                    "align": "center",
                    "color": "#555555"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": today_oil_price2[2],
                    "align": "center",
                    "color": "#555555"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": today_oil_price2[3],
                    "align": "center",
                    "color": "#555555"
                  }
                ],
                "paddingTop": "xs",
                "paddingBottom": "xs"
              }
            ],
            "spacing": "xs"
          }
        ]
      }
    ],
    "backgroundColor": "#bcaaa4"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "網址: https://gas.goodlife.tw/",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "https://gas.goodlife.tw/"
        },
        "align": "center",
        "color": "#e0e0e0"
      }
    ],
    "backgroundColor": "#616161"
  },
  "styles": {
    "footer": {
      "separator": True
    }
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
    
    content = FlexSendMessage(
        alt_text='油價公告',
        contents=bubble
    )

    line_bot_api.reply_message(
        event.reply_token,
        content
    ) 