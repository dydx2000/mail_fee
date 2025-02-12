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
    f"--{boundary}--"
)

url_joya = "https://joyabuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

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

# 目标 URL
url_joya = "https://joyabuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

# 伪造 Headers
# headers_joya = {
#     # ":method": "POST",
#     # ":authority": "joyabuy.com",
#     # ":scheme": "https",
#     # ":path": "/wp-admin/admin-ajax.php?action=get_estimation_query_prices",
#     # "content-length": str(len(data)),
#     "pragma": "no-cache",
#     "cache-control": "no-cache",
#     "sec-ch-ua-platform": '"Windows"',
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
#     "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133")',
#     "content-type": f"multipart/form-data; boundary={boundary}",
#     # "content-type": multipart_data.content_type,
#     "sec-ch-ua-mobile": "?0",
#     "Accept": "*/*",
#     "origin": "https://joyabuy.com",
#     "sec-fetch-site": "same-origin",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-dest": "empty",
#     "Referer": "https://joyabuy.com/estimation/",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
#     "priority": "u=1, i",
#     # "Cookie": "wmc_current_currency=USD; wmc_current_currency_old=USD; pll_language=en; _ss_s_uid=9eb6242c0bcb35c9de9555eb2b9c731b; _ga=GA1.1.1778277922.1739259791; __ukey=81sml3atx5; PHPSESSID=jmfohumqqujm5v4qkfvpqcreqo; _ga_LLNZ3BEEWR=GS1.1.1739324439.5.0.1739324439.0.0.0"
# }

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

    # print("request body:", request.content.decode())

# print(response.status_code)
# print(response.text)


fee_datas = response.json()

# print(fee_datas)
my_feedata = {}
my_feedata["国家"] = "美国"
my_feedata["重量"] = "501g"
my_feedata["网站"] = {"siteName": "joyabuy", "venders": []}

for fee in fee_datas['data']:
    if fee['available']:
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
