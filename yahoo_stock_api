# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 09:32:35 2021

@author: Johnny Tsai
"""

import requests
import datetime

def stock_change(p, p_p):
    change = round(((float(p) - float(p_p)) / float(p_p) * 100),2)
    return change

def emoji_create(c):   
    if c > 0:
        emoji = ' 😻'
    elif c < 0:
        emoji = ' 😿'
    else:
        emoji = ' ⚠️'
    return emoji

ids = {'':''}

message = '\n'

for _id in ids:    
    s_id = ids[_id]
    url = f'https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22{s_id}.TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true'
    res = requests.get(url)
    data = res.json()['data']
    
    price = data[0]['chart']['indicators']['quote'][0]['close'][-1]
    p_price = data[0]['chart']['meta']['previousClose']
    change = stock_change(price, p_price)
    emoji = emoji_create(change)
    timestamp = int(data[0]['chart']['timestamp'][-1]) + 28800
    time = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M')
    
    message += s_id + ' ' + _id + emoji + '\n' + str(price) + ' ; ' + str(change) + '%' + '\n'+ time + '\n\n'
    


