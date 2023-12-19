from linebot.models import *

def stock_reply_rate():
    content_text = "想知道匯率?"
    text_message = TextSendMessage(
        text = content_text,
        quick_reply = QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label="💜💜幣別種類",
                        text="幣別種類"
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="💜💜匯率兌換",
                        text="匯率兌換"
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label="💜💜我的外幣",
                        text="我的外幣"
                    )
                )
            ]
        )
    )

    return text_message

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "幣別種類",
        "weight": "bold",
        "size": "xl",
        "color": "#616161"
      }
    ],
    "backgroundColor": "#bcaaa4"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "美元",
              "data": "action=select_currency&currency=USD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#CC561E",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "日圓",
              "data": "action=select_currency&currency=JPY"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#CC561E",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "港幣",
              "text": "HKD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#CC561E",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md",
        "color": "#bcaaa4"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "英鎊",
              "text": "GBP"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#3f51b5",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "澳幣",
              "text": "AUD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#3f51b5",
            "margin": "sm"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "加拿大幣",
                "color": "#ffffff"
              }
            ],
            "backgroundColor": "#3f51b5",
            "margin": "sm",
            "cornerRadius": "md",
            "action": {
              "type": "message",
              "label": "加拿大幣",
              "text": "CAD"
            },
            "justifyContent": "center",
            "alignItems": "center"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md",
        "color": "#bcaaa4"
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
                "text": "瑞士法郎",
                "color": "#ffffff"
              }
            ],
            "backgroundColor": "#009688",
            "margin": "sm",
            "cornerRadius": "md",
            "action": {
              "type": "message",
              "label": "瑞士法郎",
              "text": "CHF"
            },
            "justifyContent": "center",
            "alignItems": "center"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "新加坡",
              "text": "SGD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009688",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "南非幣",
              "text": "ZAR"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#009688",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md",
        "color": "#bcaaa4"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "瑞典幣",
              "text": "SEK"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#ffb300",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "泰銖",
              "text": "THB"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#ffb300",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "菲比索",
              "text": "PHP"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#ffb300",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md",
        "color": "#bcaaa4"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "印尼幣",
              "text": "IDR"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#795548",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "韓元",
              "text": "KRW"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#795548",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "馬來幣",
              "text": "MYR"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#795548",
            "margin": "sm"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "md",
        "color": "#bcaaa4"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "越南盾",
              "text": "VND"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#607d8b",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "人民幣",
              "text": "CNY"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#607d8b",
            "margin": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "紐元",
              "text": "NZD"
            },
            "gravity": "center",
            "style": "primary",
            "color": "#607d8b",
            "margin": "sm"
          }
        ]
      }
    ],
    "backgroundColor": "#bcaaa4"
  }
}
                    
    )
    return flex_message

def youtube_channel():
    flex_message = FlexSendMessage(
            alt_text="youtube_channel",
            contents=
            {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/SJPH542.jpg",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "size": "full",
                        "backgroundColor": "#000000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "理財達人秀",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "最精彩最好懂",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/channel/UCQvsuaih5lE0n_Ne54nNezg"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/dPW0jcC.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#AA0000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CMoney理財寶",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "基本理財知識",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/CMoneySchool"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/zkUZrCj.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#444444"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "我要做富翁",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "平民化&分享形式",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/SyLingHim"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    }
                ]
            }
        )
    return flex_message

def realtime_currency_other(currency):
    content = "想知道更多?"
    text_message = TextSendMessage(
        text = content,
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                            action=MessageAction(
                                label="即時匯率", 
                                text="外幣"+currency,
                            )
                ),
                QuickReplyButton(
                            action=MessageAction(
                                label="加入清單", 
                                text="新增外幣"+currency,
                            )
                ),
                    QuickReplyButton(
                            action=MessageAction(
                                label="走勢圖", 
                                text="CT"+currency,
                            )
                ),
                    QuickReplyButton(
                            action=MessageAction(
                                label="新聞", 
                                text="N外匯"+currency,
                            )
                )
            ]
        ))
    return text_message

def stock_reply_other(stockNumber):
    content_text = "想知道更多?"
    text_message = TextSendMessage(
        text = content_text ,
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                        action=MessageAction(
                            label="即時股價", 
                            text="#"+stockNumber,
                        )
                ),
                QuickReplyButton(
                        action=MessageAction(
                            label="關注", 
                            text="關注"+stockNumber,
                        )
                ),
                QuickReplyButton(
                        action=MessageAction(
                            label="取消關注", 
                            text="刪除"+stockNumber,
                        )
                ),
                QuickReplyButton(
                        action=MessageAction(
                            label="走勢圖", 
                            text="P"+stockNumber,
                        )
                ),
                QuickReplyButton(
                        action=MessageAction(
                            label="K線圖", 
                            text="K"+stockNumber
                        )
                ),
                QuickReplyButton(
                        action=MessageAction(
                            label="法人", 
                            text="F"+stockNumber
                        )
                ),
                QuickReplyButton(
                        action=MessageAction(
                            label="三大面向分析", 
                            text= "三大面向分析"+stockNumber
                        )
                ),
                QuickReplyButton(
                        action=MessageAction(
                            label="新聞", 
                            text= "N"+stockNumber
                        )
                ),
                QuickReplyButton(
                        action=MessageAction(
                            label="年收益率", 
                            text= "收益率" + stockNumber
                        )
                ),
        ]
    ))
    return text_message
