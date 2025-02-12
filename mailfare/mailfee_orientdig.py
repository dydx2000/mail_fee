from lib2to3.fixes.fix_dict import iter_exempt
from operator import itemgetter

import requests, json

url_orientdig = "https://orientdig.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

headers = {
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarywQkmSLhKNWpKOJ9u",
    "accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    # "Origin": "https://cnfans.com",
    # "Referer": "https://cnfans.com/zh/estimation/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    # "Cookie": "PHPSESSID=ohp6s0j3vqfcnrbrr1vatq527u; wmc_current_currency=USD; wmc_current_currency_old=USD",
    "accept-language": "zh-CN,zh;q=0.9",

}
data = {
    "destination": "GB",
    "weight": 500,
    # "features": None,
    # "length": None,
    # "width": None,
    # "height": None,
    # "username": None,
    # "password": None,
    "terms": 1

}


response = requests.post(url=url_orientdig, data=data)

print(response.request.headers)
# response = requests.post(url=url_orientdig, data=data, headers=headers)

# response = requests.post(url=url_mule, data=data, params=params_mule)

print(response.status_code)
print(response.json())

fee_datas = response.json()

print(fee_datas)
my_feedata = {}
my_feedata["国家"] = "美国"
my_feedata["重量"] = "501g"
my_feedata["网站"] = {"siteName": "mulebuy", "venders": []}

for fee in fee_datas['data']:
    print(fee)
    print(fee['available'])
    if fee['available']:
        # print(fee)
        my_feedata["网站"]['venders'].append([
            {"venderName": fee['name']},
            {'总价': fee['feeDetail']['total']},
            {'首重价格': fee['feeDetail']['feeFirst']},
            {"额外重量价格": fee['feeDetail']["feeContinue"]},
            {"操作费": fee['feeDetail']["operationFee"]},
            {"服务费": fee['feeDetail']["serviceFee"]},
            {"最低重量限制": fee['restrictions']["minWeight"]},
            {"最高重量限制": fee['restrictions']["maxWeight"]},
            {"尺寸限制": fee['restrictions']["dimensionRestriction"]},
            {"体积重量计费规则": fee['restrictions']["volumeWeightRule"]},
            {"运输时间": fee["transitTime"]},

        ])

print(my_feedata)
for item in my_feedata['网站']['venders']:
    print(item)
