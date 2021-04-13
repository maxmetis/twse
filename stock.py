Created on Mon May 11 21:56:35 2020

@author: Johnny Tsai
"""
import requests

tse_ids = ['']

otc_ids = [''] 

#['c','n','z','tv','v','o','h','l','y']
#['股票代號','公司簡稱','當盤成交價','當盤成交量','累積成交量','開盤價','最高價','最低價','昨收價']


#---------------大盤-----------------
twse_url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_t00.tw'

twse_res = requests.get(twse_url)
twse_data = twse_res.json()

twse_index = twse_data['msgArray'][0]['z']
twse_index_y = twse_data['msgArray'][0]['y']
twse_change = float(twse_index) - float(twse_index_y)
twse_rate = twse_change / float(twse_index_y) * 100
twse_date = twse_data['queryTime']['sysDate']
twse_time = twse_data['queryTime']['sysTime']

if twse_change > 0:
    twse_emoji = ' 😻'
elif twse_change < 0:
    twse_emoji = ' 😿'
else:
    twse_emoji = ' ⚠️' 

twse_message = '加權指數' + twse_emoji + '\n' + str(twse_index) + ' ; '  \
+ str(round(twse_rate, 2)) + '%' + '\n\n'  + '📲 ' + twse_date + '\n' + '      ' + twse_time

def tonyStock():
    message = '\n'
    #---------------上櫃-----------------
    for tse_id in tse_ids:
        tse_stock_list = 'tse_{}.tw'.format(tse_id)
        tse_query_url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch="+ tse_stock_list
        tse_res = requests.get(tse_query_url)
        tse_data = tse_res.json()

        tse_code = tse_data['msgArray'][0]['c']
        tse_name = tse_data['msgArray'][0]['n']
        
        tse_price_z = tse_data['msgArray'][0]['z']
        tse_price_b = tse_data['msgArray'][0]['b'].split('_')[0]
        if tse_price_z != '-':
            tse_price = round(float(tse_price_z),2)
        else:
            tse_price = round(float(tse_price_b),2)        
        
        tse_price_y = tse_data['msgArray'][0]['y']
        tse_change = float(tse_price) - float(tse_price_y)
        tes_rate = tse_change / float(tse_price_y) * 100
        if tse_change > 0:
            tse_emoji = ' 😻'
        elif tse_change < 0:
            tse_emoji = ' 😿'
        else:
            tse_emoji = ' ⚠️'        
        
        message += tse_code + ' ' + tse_name + tse_emoji + '\n' + str(tse_price) + ' ; ' + str(round(tes_rate, 1))+ '%' + '\n\n'
    
    #---------------上櫃-----------------
    for otc_id in otc_ids:
        otc_stock_list = 'otc_{}.tw'.format(otc_id)
        otc_query_url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch="+ otc_stock_list
        otc_res = requests.get(otc_query_url)
        otc_data = otc_res.json()
        otc_code = otc_data['msgArray'][0]['c']
        otc_name = otc_data['msgArray'][0]['n']
        otc_price = round(float(otc_data['msgArray'][0]['b'].split('_')[0]),2)
        otc_price_y = otc_data['msgArray'][0]['y']
        otc_change = float(otc_price) - float(otc_price_y)
        otc_rate = otc_change / float(otc_price_y) * 100
        if otc_change > 0:
            otc_emoji = ' 😻'
        elif otc_change < 0:
            otc_emoji = ' 😿'
        else:
            otc_emoji = ' ⚠️'

        message += otc_code + ' ' + otc_name + otc_emoji + '\n' + str(otc_price) + ' ; ' + str(round(otc_rate, 1))+ '%' + '\n\n'
    message = message + twse_message
    return message
    
#LINE NOTIFY-------------------------------------

def lineNotifyMessage(token, msg):
   headers = {
       "Authorization": "Bearer " + token, 
   }
	
   payload = {'message': msg}
   r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
   return r.status_code
	
token = ''

lineNotifyMessage(token, tonyStock()) 
