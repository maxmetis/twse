Created on Mon May 11 21:56:35 2020

@author: Johnny Tsai


import requests

def tonyStock(catg, stock_id):
    try:
        query_url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={}_{}.tw'.format(catg, stock_id)
        res = requests.get(query_url)
        data = res.json()

        code = data['msgArray'][0]['c']
        name = data['msgArray'][0]['n']
        date = data['msgArray'][0]['d']
        time = data['msgArray'][0]['t']
        low = data['msgArray'][0]['l']
        high = data['msgArray'][0]['h']
        
        price_z = data['msgArray'][0]['z']  #成交價
        
        if 'b' in data['msgArray'][0]:
            price_b = data['msgArray'][0]['b']  #買價
        if 'a' in data['msgArray'][0]:
            price_a = data['msgArray'][0]['a']  #賣價
        if 'f' in data['msgArray'][0]:
            price_f = data['msgArray'][0]['f']  #賣量
        if 'g' in data['msgArray'][0]:
            price_g = data['msgArray'][0]['g']  #買量
        
        if price_z != '-':
            price = price_z
        elif price_a == '-' and price_f == '-':
            price = price_b.split('_')[1]
        elif price_b == '-' and price_g == '-':
            price = price_a.split('_')[1]
        elif int(price_f.split('_')[0]) > int(price_g.split('_')[0]):
            price = price_b.split('_')[0]
        elif int(price_f.split('_')[0]) < int(price_g.split('_')[0]):
            price = price_a.split('_')[0]
        else:
            price = '-'
        
        if price != '-':
            price = round(float(price),2)
            price_y = data['msgArray'][0]['y']
            change = float(price) - float(price_y)
            rate = change / float(price_y) * 100
            if change > 0:
                emoji = ' 😻'
            elif change < 0:
                emoji = ' 😿'
            else:
                emoji = ' ⚠️'
        else:
            change = '-'
            emoji = ''
        
        message = code + ' ' + name.replace('發行量加權股價指數','加權股價指數') + emoji + '\n' + '現價： ' + str(price) + '\n' + '漲跌： ' + str(round(rate, 1)) + '%' + '\n' + '最高： ' + str(round(float(high), 2)) + '\n' + '最低： ' + str(round(float(low), 2)) + '\n' + date + '  ' + time
        return message
    except:
        message = 'Error happend' + '\n\n' 
        return message
   
print(tonyStock('otc', '3105'))
