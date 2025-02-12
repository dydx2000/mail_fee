from lib2to3.fixes.fix_dict import iter_exempt
from operator import itemgetter

import requests

url_mule = "https://mulebuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"


params_mule = {
    "action": "get_estimation_query_prices"
}


headers = {
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryLxGfRixPC0oRahOb",
    "Origin": "https://mulebuy.com",
    "Referer": "https://mulebuy.com/zh/estimation/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Cookie": "PHPSESSID=k8d8da2crlctau78h1qlb3cdvl; wmc_current_currency=USD; wmc_current_currency_old=USD; pll_language=zh; user_temp_intercom=d80184f3df9ff13bb88ed11367c56fe1; name_temp_intercom=TempUser_d80184f3df9ff13bb88ed11367c56fe1; _ga=GA1.1.1728349236.1739253174; _tt_enable_cookie=1; _ttp=-TuUqijACLA3NnN_yK14b5ot-Ls.tt.1; __ukey=81sgb4t9x903; intercom-id-tj75osrf=e445c5c6-8929-40ef-8b42-8e8a824b5e22; intercom-session-tj75osrf=; intercom-device-id-tj75osrf=5626b778-73c8-4564-94aa-8e8ca26b36b2; _ga_QFC95GJ39P=GS1.1.1739254996.2.0.1739254996.60.0.1542245267",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    "accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br, zstd"
}

data = {
    "destination": "SG",
    "weight": 7,
    "features": None,
    "length": None,
    "width": None,
    "height": None,
    "username": None,
    "password": None,
    "terms": 1

}

# response = requests.post(url=url_mule, data=data,headers=headers, params=params_mule)
response = requests.post(url=url_mule, data=data, params=params_mule)

# print(response.status_code)
# print(response.json())

fee_datas = response.json()

# print(fee_datas)
my_feedata = {}
my_feedata["国家"] = "美国"
my_feedata["重量"] = "501g"
my_feedata["网站"] = {"siteName": "mulebuy", "venders": []}

for fee in fee_datas['data']:
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

# print(my_feedata)
for item in my_feedata['网站']['venders']:
    print(item)
