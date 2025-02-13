import httpx, uuid

boundary = f"----WebKitFormBoundary{uuid.uuid4().hex[:16]}"
multipart_data = (
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="destination"\r\n\r\n'
    f"CA\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="weight"\r\n\r\n'
    f"500\r\n"
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
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="terms"\r\n\r\n'
    f"1\r\n"
    f"--{boundary}--"
)

# 目标 URL
url_cfans = "https://cnfans.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"
# url_cfans = "https://cnfans.com/wp-admin/admin-ajax.php"

params = {
    "action": "get_estimation_query_prices"
}

data = {
    "destination": "CA",
    "weight": 500,
    "features": None,
    "length": None,
    "width": None,
    "height": None,
    "username": None,
    "password": None,
}



# 伪造 Headers
headers_cfans = {
    # ":method": "POST",
    # ":authority": "joyabuy.com",
    # ":scheme": "https",
    # ":path": "/wp-admin/admin-ajax.php?action=get_estimation_query_prices",
    # "content-length": str(len(data)),
    # "pragma": "no-cache",
    # "cache-control": "no-cache",
    # "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    # "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133")',
    "content-type": f"multipart/form-data; boundary={boundary}",
    # "content-type": multipart_data.content_type,
    # "sec-ch-ua-mobile": "?0",
    "Accept": "*/*",
    "origin": "https://cnfans.com",
    # "sec-fetch-site": "same-origin",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-dest": "empty",
    "Referer": "https://cnfans.com/zh/estimation/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    # "priority": "u=1, i",
    "Cookie": "wmc_current_currency=USD; wmc_current_currency_old=USD"
}

with httpx.Client(http2=True) as client:
    client.headers.update(headers_cfans)
    response = client.post(url=url_cfans, content=multipart_data.encode(),params=params)
    request = response.request


    print("request body:", request.content.decode())
    print("request header:", request.headers)

# print(response.status_code)
# print(response.text)


# fee_datas = response.json()

print(response)

# print(fee_datas)
my_feedata = {}
my_feedata["国家"] = "美国"
my_feedata["重量"] = "501g"
my_feedata["网站"] = {"siteName": "mulebuy", "venders": []}

# feefor fee in fee_datas['data']:
#     print(fee)
#     if fee['available']:
#         my_feedata["网站"]['venders'].append([
#             {"venderName": fee['name']},
#             {'总价': fee['feeDetail']['total']},
#             {'首重价格': fee['feeDetail']['feeFirst']},
#             {"额外重量价格": fee['feeDetail']["feeContinue"]},
#             {"操作费": fee['feeDetail']["operationFee"]},
#             {"服务费": fee['feeDetail']["serviceFee"]},
#             {"最低重量限制": fee['restrictions']["minWeight"]},
#             {"最高重量限制": fee['restrictions']["maxWeight"]},
#             {"尺寸限制": fee['restrictions']["dimensionRestriction"]},
#             {"体积重量计费规则": fee['restrictions']["volumeWeightRule"]},
#             {"运输时间": fee["transitTime"]},
#         ])
#
# print(my_feedata)
# for item in my_feedata['网站']['venders']:
#     print(item)
