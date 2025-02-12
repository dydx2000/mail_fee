# 导入库
import requests, httpx, uuid, json
from openpyxl import Workbook

# 公共变量 my_feedata 存储全部获取的邮费信息
from openpyxl.styles import Alignment, Font

country = "US"
weight = 600

my_feedata = {}
my_feedata["国家"] = country
my_feedata["重量"] = weight
my_feedata["网站"] = []

# 输出excel数据
sheetData = []

# 1. mule 邮费查询
url_mule = "https://mulebuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

headers = {
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryLxGfRixPC0oRahOb",
    "Origin": "https://mulebuy.com",
    "Referer": "https://mulebuy.com/zh/estimation/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Cookie": "PHPSESSID=k8d8da2crlctau78h1qlb3cdvl; wmc_current_currency=USD; wmc_current_currency_old=USD; pll_language=zh; user_temp_intercom=d80184f3df9ff13bb88ed11367c56fe1; name_temp_intercom=TempUser_d80184f3df9ff13bb88ed11367c56fe1; _ga=GA1.1.1728349236.1739253174; _tt_enable_cookie=1; _ttp=-TuUqijACLA3NnN_yK14b5ot-Ls.tt.1; __ukey=81sgb4t9x903; intercom-id-tj75osrf=e445c5c6-8929-40ef-8b42-8e8a824b5e22; intercom-session-tj75osrf=; intercom-device-id-tj75osrf=5626b778-73c8-4564-94aa-8e8ca26b36b2; _ga_QFC95GJ39P=GS1.1.1739254996.2.0.1739254996.60.0.1542245267",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    "accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd"
}

data = {
    "destination": country,
    "weight": weight,
    "features": None,
    "length": None,
    "width": None,
    "height": None,
    "username": None,
    "password": None,
    "terms": 1

}
# response = requests.post(url=url_mule, data=data,headers=headers, params=params_mule)
response = requests.post(url=url_mule, data=data)
# print(response.status_code)
# print(response.json())

# 接口返回jsonu数据
fee_datas = response.json()

curSiteInfo = {"siteName": "mulebuy", "venders": []}
# 将 mule 数据存入 my_feedata
for fee in fee_datas['data']:
    if fee['available']:
        # print(fee)
        curSiteInfo['venders'].append(
            {"venderName": fee['name'],
             '总价': fee['feeDetail']['total'],
             '首重价格': fee['feeDetail']['feeFirst'],
             "额外重量价格": fee['feeDetail']["feeContinue"],
             "操作费": fee['feeDetail']["operationFee"],
             "服务费": fee['feeDetail']["serviceFee"],
             "最低重量限制": fee['restrictions']["minWeight"],
             "最高重量限制": fee['restrictions']["maxWeight"],
             "尺寸限制": fee['restrictions']["dimensionRestriction"],
             "体积重量计费规则": fee['restrictions']["volumeWeightRule"],
             "运输时间": fee["transitTime"]},
        )

for item in curSiteInfo['venders']:
    print(item)
    sheetData.append(
        (country,
         weight,
         curSiteInfo['siteName'],
         item['venderName'],
         item['总价'],
         item['首重价格'],
         item['额外重量价格'],
         item['操作费'],
         item['服务费'],
         item['最低重量限制'],
         item['最高重量限制'],
         item['尺寸限制'],
         item['体积重量计费规则'],
         item['运输时间'],
         )
    )

my_feedata["网站"].append(curSiteInfo)
print("mule 查询完毕")

# 2 获取orientdig 邮费信息
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
    "destination": country,
    "weight": weight,
    "terms": 1

}

response = requests.post(url=url_orientdig, data=data)
fee_datas = response.json()
# 提取邮费信息

curSiteInfo = {"siteName": "orientDig", "venders": []}
for fee in fee_datas['data']:
    if fee['available']:
        curSiteInfo['venders'].append(
            {"venderName": fee['name'],
             '总价': fee['feeDetail']['total'],
             '首重价格': fee['feeDetail']['feeFirst'],
             "额外重量价格": fee['feeDetail']["feeContinue"],
             "操作费": fee['feeDetail']["operationFee"],
             "服务费": fee['feeDetail']["serviceFee"],
             "最低重量限制": fee['restrictions']["minWeight"],
             "最高重量限制": fee['restrictions']["maxWeight"],
             "尺寸限制": fee['restrictions']["dimensionRestriction"],
             "体积重量计费规则": fee['restrictions']["volumeWeightRule"],
             "运输时间": fee["transitTime"]},
        )

for item in curSiteInfo['venders']:
    print(item)
    sheetData.append(
        (country,
         weight,
         curSiteInfo['siteName'],
         item['venderName'],
         item['总价'],
         item['首重价格'],
         item['额外重量价格'],
         item['操作费'],
         item['服务费'],
         item['最低重量限制'],
         item['最高重量限制'],
         item['尺寸限制'],
         item['体积重量计费规则'],
         item['运输时间'],
         )
    )
my_feedata["网站"].append(curSiteInfo)
print("orientdig 查询完毕")

# 3 oopbuy 邮费信息
url_oopbuy = "https://webapi.oopbuy.com/logistics/estimate/international2"
headers = {
    # "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarywQkmSLhKNWpKOJ9u",
    # "Origin": "https://cnfans.com",
    # "Referer": "https://cnfans.com/zh/estimation/",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    # "Cookie": "PHPSESSID=ohp6s0j3vqfcnrbrr1vatq527u; wmc_current_currency=USD; wmc_current_currency_old=USD",
    "accept-language": "zh-CN,zh;q=0.9"
}
data = {"categoryList": [], "country": country, "high": "", "length": "", "weight": weight, "width": ""}

response = requests.post(url=url_oopbuy, json=data, headers=headers)

fee_datas = response.json()

curSiteInfo = {"siteName": "oopbuy", "venders": []}
for fee in fee_datas['result']:
    start_date = fee["minDeliveredDays"]
    end_date = fee["maxDeliveredDays"]
    duration = str(start_date) + "-" + str(end_date)

    curSiteInfo['venders'].append(
        {"venderName": fee['name'],
         '总价': fee['totalFee'],
         '首重价格': None,
         "额外重量价格": None,
         "操作费": None,
         "服务费": None,
         "最低重量限制": None,
         "最高重量限制": None,
         "尺寸限制": fee["sizeLimitExp"],
         "体积重量计费规则": None,
         "运输时间": duration},
    )

for item in curSiteInfo['venders']:
    print(item)
    sheetData.append(
        (country,
         weight,
         curSiteInfo['siteName'],
         item['venderName'],
         item['总价'],
         item['首重价格'],
         item['额外重量价格'],
         item['操作费'],
         item['服务费'],
         item['最低重量限制'],
         item['最高重量限制'],
         item['尺寸限制'],
         item['体积重量计费规则'],
         item['运输时间'],
         )
    )

my_feedata["网站"].append(curSiteInfo)
print("oopbuy 查询完毕")

# 4 joyabuy 邮费信息
boundary = f"----WebKitFormBoundary{uuid.uuid4().hex[:16]}"
multipart_data = (
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="destination"\r\n\r\n'
    f"{country}\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="weight"\r\n\r\n'
    f"{weight}\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="features"\r\n\r\n'
    f"\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="length"\r\n\r\n'
    f"\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="width"\r\n\r\n'
    f"\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="height"\r\n\r\n'
    f"\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="username"\r\n\r\n'
    f"\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="password"\r\n\r\n'
    f"\r\n"
    f"--{boundary}--"
)

url_joya = "https://joyabuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

params = {
    "action": "get_estimation_query_prices"
}

# 目标 URL
url_joya = "https://joyabuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

headers_joya = {
    # ":method": "POST",
    # ":authority": "joyabuy.com",
    # ":scheme": "https",
    # ":path": "/wp-admin/admin-ajax.php?action=get_estimation_query_prices",
    # "content-length": str(len(data)),
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    # "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133")',
    "content-type": f"multipart/form-data; boundary={boundary}",
    # "content-type": multipart_data.content_type,
    # "sec-ch-ua-mobile": "?0",
    "Accept": "*/*",
    "origin": "https://joyabuy.com",
    "Referer": "https://joyabuy.com/estimation/",
    # "sec-fetch-site": "same-origin",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-dest": "empty",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    # "priority": "u=1, i",
    # "Cookie": "wmc_current_currency=USD; wmc_current_currency_old=USD; pll_language=en; _ss_s_uid=9eb6242c0bcb35c9de9555eb2b9c731b; _ga=GA1.1.1778277922.1739259791; __ukey=81sml3atx5; PHPSESSID=jmfohumqqujm5v4qkfvpqcreqo; _ga_LLNZ3BEEWR=GS1.1.1739324439.5.0.1739324439.0.0.0"
}

with httpx.Client(http2=True) as client:
    client.headers.update(headers_joya)
    response = client.post(url=url_joya, content=multipart_data.encode())
    request = response.request
    # 打印请求体
    # print("request body:", request.content.decode())

fee_datas = response.json()

curSiteInfo = {"siteName": "joyabuy", "venders": []}

for fee in fee_datas['data']:
    if fee['available']:
        curSiteInfo['venders'].append(
            {"venderName": fee['name'],
             '总价': fee['feeDetail']['total'],
             '首重价格': fee['feeDetail']['feeFirst'],
             "额外重量价格": fee['feeDetail']["feeContinue"],
             "操作费": fee['feeDetail']["operationFee"],
             "服务费": fee['feeDetail']["serviceFee"],
             "最低重量限制": fee['restrictions']["minWeight"],
             "最高重量限制": fee['restrictions']["maxWeight"],
             "尺寸限制": fee['restrictions']["dimensionRestriction"],
             "体积重量计费规则": fee['restrictions']["volumeWeightRule"],
             "运输时间": fee["transitTime"]},
        )

# 打印所以有邮费信息

for item in curSiteInfo['venders']:
    print(item)
    sheetData.append(
        (country,
         weight,
         curSiteInfo['siteName'],
         item['venderName'],
         item['总价'],
         item['首重价格'],
         item['额外重量价格'],
         item['操作费'],
         item['服务费'],
         item['最低重量限制'],
         item['最高重量限制'],
         item['尺寸限制'],
         item['体积重量计费规则'],
         item['运输时间'],
         )
    )

my_feedata['网站'].append(curSiteInfo)
print("joyabuy 查询完毕")

# 5 acbuy
url_acbuy = "https://acbuy.com/prefix-api/store-logistics/estimate/route"

headers = {
    "accept-language": "zh-CN,zh;q=0.9"
}
data = {"countryCode": country, "weight": weight, "length": "", "width": "", "height": "", "itemLimitList": [],
        "sortBy": "price", "sort": "asc"}

response = requests.post(url=url_acbuy, json=data)

# print(response.status_code)
# print(response.json())

fee_datas = response.json()

curSiteInfo = {"siteName": "acbuy", "venders": []}

for fee in fee_datas['data']:
    feeMap = fee['feeDetail']['feeCompositions']['feeMap']
    # print(type(feeMap))
    # print(feeMap['A1'])
    try:
        feeMap_dict = json.loads(feeMap['A1'])
        continuedPrice = feeMap_dict[0]['continuedPrice']
        firstPrice = feeMap_dict[0]['firstPrice']
        weightRangeStart = feeMap_dict[0]['weightRangeStart']
        weightRangeEnd = feeMap_dict[0]['weightRangeEnd']
    except:
        continuedPrice = None
        firstPrice = None
        weightRangeStart = None
        weightRangeEnd = None

    # firstPrice = feeMap_dict[0]['firstPrice']
    # print(fee['feeDetail']["feeDTOList"][1]["feeAmount"],"操作费")

    start_date = fee["carrierProductLineInfo"]["fastestDuration"]
    end_date = fee["carrierProductLineInfo"]["slowestDuration"]
    duration = str(start_date) + "-" + str(end_date)

    curSiteInfo['venders'].append(
        {"venderName": fee['carrierProductCode'],
         '总价': fee['feeDetail']['totalAmount'],
         '首重价格': firstPrice,
         "额外重量价格": continuedPrice,
         "操作费": fee['feeDetail']["feeDTOList"][1]["feeAmount"],
         "服务费": 0,
         "最低重量限制": weightRangeStart,
         "最高重量限制": weightRangeEnd,
         "尺寸限制": None,
         "体积重量计费规则": None,
         "运输时间": duration},

    )

for item in curSiteInfo['venders']:
    print(item)
    sheetData.append(
        (country,
         weight,
         curSiteInfo['siteName'],
         item['venderName'],
         item['总价'],
         item['首重价格'],
         item['额外重量价格'],
         item['操作费'],
         item['服务费'],
         item['最低重量限制'],
         item['最高重量限制'],
         item['尺寸限制'],
         item['体积重量计费规则'],
         item['运输时间'],
         )
    )

my_feedata['网站'].append(curSiteInfo)
print("acbuy 查询完毕")

print(sheetData)

from openpyxl import Workbook

# 创建一个新的工作簿
wb = Workbook()

# 获取活动工作表
ws = wb.active

# 设置工作表标题
ws.title = f"{country}-运费表"

# 写入数据到单元格
# 写入数据到单元格
ws['A1'] = '目的国家'
ws['B1'] = '重量'
ws['C1'] = '网站'
ws['D1'] = '承运公司'
ws['E1'] = '总价'
ws['F1'] = '首重价格'
ws['G1'] = '额外重量价格'
ws['H1'] = '操作费'
ws['I1'] = '服务费'
ws['J1'] = '最低重量限制'
ws['K1'] = '最高重量限制'
ws['L1'] = '尺寸限制'
ws['M1'] = '体积重量计费规则'
ws['N1'] = '运输时间'

# 写入多行数据

for row in sheetData:
    ws.append(row)

max_rows = ws.max_row  # 获取最大行
max_columns = ws.max_column
align=Alignment(horizontal='center',vertical='center')
ws.column_dimensions['C'].width = 15
ws.column_dimensions['D'].width = 35
ws.column_dimensions['G'].width = 15
ws.column_dimensions['J'].width = 15
ws.column_dimensions['K'].width = 15
ws.column_dimensions['L'].width = 15
ws.column_dimensions['M'].width = 24

for i in range(1, max_rows + 1):
    for j in range(1, max_columns + 1):
        if i>1 and (j==4 or j==12 or j==13):
            continue
        ws.cell(i, j).alignment = align

# 创建一个粗体字体样式
bold_font = Font(bold=True)
# 将粗体字体样式应用到 B1 单元格

for i in range(1,max_rows+1):
    ws.cell(1,i).font=bold_font

# for j in range(1,max_columns+1):
#     ws.column_dimensions[j].width = 15

# 保存工作簿
wb.save('mailFee.xlsx')
