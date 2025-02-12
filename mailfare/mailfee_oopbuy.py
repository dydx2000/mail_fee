from lib2to3.fixes.fix_dict import iter_exempt
from operator import itemgetter

import requests, json

url_oopbuy = "https://webapi.oopbuy.com/logistics/estimate/international2"

headers = {
    # "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarywQkmSLhKNWpKOJ9u",
    # "Origin": "https://cnfans.com",
    # "Referer": "https://cnfans.com/zh/estimation/",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    # "Cookie": "PHPSESSID=ohp6s0j3vqfcnrbrr1vatq527u; wmc_current_currency=USD; wmc_current_currency_old=USD",
    "accept-language": "zh-CN,zh;q=0.9"
}
data = {"categoryList":[],"country":"US","high":"","length":"","weight":500,"width":""}

response = requests.post(url=url_oopbuy, json=data,headers=headers)

# print(response.status_code)
# print(response.json())

fee_datas = response.json()

print(fee_datas)
my_feedata = {}
my_feedata["国家"] = "美国"
my_feedata["重量"] = "501g"
my_feedata["网站"] = {"siteName": "mulebuy", "venders": []}
i = 0
for fee in fee_datas['result']:
    # print(fee)
    # print( fee['feeDetail']['feeCompositions']['feeMap']['A1'])
    # print(type( fee['feeDetail']['feeCompositions']['feeMap']['A1']))

    # feeMap =  fee['feeDetail']['feeCompositions']['feeMap']
    # # print(type(feeMap))
    # # print(feeMap['A1'])
    # try:
    #     feeMap_dict = json.loads(feeMap['A1'])
    #     # print(feeMap_dict)
    #
    #     continuedPrice= feeMap_dict[0]['continuedPrice']
    #     firstPrice = feeMap_dict[0]['firstPrice']
    #     weightRangeStart = feeMap_dict[0]['weightRangeStart']
    #     weightRangeEnd = feeMap_dict[0]['weightRangeEnd']
    #
    # except:
    #
    #     continuedPrice = None
    #     firstPrice = None
    #     weightRangeStart = None
    #     weightRangeEnd = None

    # firstPrice = feeMap_dict[0]['firstPrice']
    # print(fee['feeDetail']["feeDTOList"][1]["feeAmount"],"操作费")

    start_date = fee["minDeliveredDays"]
    end_date = fee["maxDeliveredDays"]
    duration = str(start_date)+"-"+str(end_date)

    # if fee['available']:
    # print(fee)
    my_feedata["网站"]['venders'].append([
        {"venderName": fee['name']},
        {'总价': fee['totalFee']},
        {'首重价格': None},
        {"额外重量价格": None},
        {"操作费": None},
        {"服务费": None},
        {"最低重量限制": None},
        {"最高重量限制": None},
        {"尺寸限制": fee["sizeLimitExp"]},
        {"体积重量计费规则": None},
        {"运输时间": duration},

    ])

    # print(i)
    # i+=1
    # print(my_feedata)




# print(my_feedata)
for item in my_feedata['网站']['venders']:
    print(item)
