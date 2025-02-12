import requests, json

url_hippo = "https://api-jiyun-v3.haiouoms.com/api/client/express/price-query"


headers = {
    "Host": "api-jiyun-v3.haiouoms.com",
    "Connection": "keep-alive",
    "Content-Length": "150",
    "language": "zh_CN",
    "sec-ch-ua-platform": "\"Windows\"",
    "Authorization": "null",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "currency": "USD",
    "sec-ch-ua-mobile": "?0",
    "App-key": "arIM1n8tmcrHgD1jHz0Zt8H1XPxUjVen",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "X-Uuid": "dd70dbad-9df5-4813-b17d-910a60dd54ef",
    "Origin": "https://hippoobuy.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://hippoobuy.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

data = {"warehouse_id":1250,"country_id":12072,"area_id":"","sub_area_id":"","weight":5000,"length":"","width":"","height":"","prop_ids":[],"postcode":""}

response = requests.post(url=url_hippo,  headers=headers, json=data, verify=False)

# print(response)
# print(response.json())
# print(response.json())

fee_datas = response.json()


my_feedata = {}
my_feedata["国家"] = "美国"
my_feedata["重量"] = "501g"
my_feedata["网站"] = {"siteName": "mulebuy", "venders": []}


for fee in fee_datas['data']:
    my_feedata["网站"]['venders'].append([
        {"venderName": fee['name']},
        # {'总价': fee['feeDetail']['total']},
        # {'首重价格': fee['first_money']},
        # {"额外重量价格": fee['feeDetail']["feeContinue"]},
        # {"操作费": fee['feeDetail']["operationFee"]},
        # {"服务费": fee['feeDetail']["serviceFee"]},
        # {"最低重量限制": fee['min_weight']},
        # {"最高重量限制": fee['max_weight'],
        # {"尺寸限制": fee['restrictions']["dimensionRestriction"]},
        # {"体积重量计费规则": fee['restrictions']["volumeWeightRule"]},
        # {"运输时间": fee["reference_time"]}
        ])
    print(fee)



