import tls_client
import httpx, uuid

# 创建会话，模拟 Chrome
session = tls_client.Session(
    client_identifier="chrome_133",  # 伪装 Chrome 120
    random_tls_extension_order=True  # 让 TLS 扩展字段顺序随机化
)

params = {
    "action": "get_estimation_query_prices"
}
# url = "https://example.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# boundary = f"----WebKitFormBoundary{uuid.uuid4().hex[:16]}"
boundary = f"----WebKitFormBoundary{uuid.uuid4().hex}"
boundary = f"----WebKitFormBoundaryaNvkSlFQP7boiXKp"
multipart_data = (
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="destination"\r\n\r\n'
    f"US\r\n"
    f"--{boundary}\r\n"
    f'Content-Disposition: form-data; name="weight"\r\n\r\n'
    f"650\r\n"
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
    f"--{boundary}--\r\n"
)

# 目标 URL
url_cfans = "https://cnfans.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"
url_cfans = "https://cnfans.com/wp-admin/admin-ajax.php"

headers_cfans = {
    # ":method": "POST",
    # ":scheme": "https",
    # ":path": "/wp-admin/admin-ajax.php?action=get_estimation_query_prices",
    # ":authority": "cnfans.com",
    # "content-length": str(len(data)),
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133")',
    "Content-Type": f"multipart/form-data; boundary={boundary}",
    # "content-type": multipart_data.content_type,
    "sec-ch-ua-mobile": "?0",
    "accept": "*/*",
    "origin": "https://cnfans.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://cnfans.com/zh/estimation/",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    # "connection":"keep-alive",
    "priority": "u=1, i",
    "cookie": "_gcl_au=1.1.663297501.1739267717; __ukey=81su6uvgx411; lf_session_id=855014af-26a8-4273-95b8-58c4303cf339; lf_first_visit=1739267718320; _ss_s_uid=9eb6242c0bcb35c9de9555eb2b9c731b; _gid=GA1.2.1713319632.1739267723; wmc_current_currency=CNY; wmc_current_currency_old=CNY; _hjSessionUser_3640651=eyJpZCI6ImE0NDYzMzU5LWQyNjEtNTY2MC1iYjEyLWJmMGFhNDU5MDE5ZCIsImNyZWF0ZWQiOjE3MzkyNjc3MTg2MDMsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=aAvWa7iRdGoSTGo0yuifOZzhjrr.tt.1; pll_language=zh; _hjSession_3640651=eyJpZCI6ImUxZTY5M2QzLWM3YmUtNDI1My05MTU2LTMyMDBjYjllMGYyZSIsImMiOjE3MzkzNDc3MDk5MjEsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; lf_prev_visit=1739347707464; lf_this_visit=1739350664147; lf_session_count=3; cf_clearance=tF_AQYcFlgdfY8Zc4PWWoLBTShHb.yaSbkEg2f9Wdxo-1739350664-1.2.1.1-a5u5MhvAQvAd1rIaL5Ax3CIZV32rf_Jbf27nz65.tZjBQgWSfNTPMQPO6w05vPx0TH6zIa6Zayp1Vx5KUwjFEaBE9wUWqV21J5gt25Mvagv_2DTzle.DoGfN_CgczAjwDVKRGoLIL0mYGUSLzM9h5eWYQ2qFHi9Xwa4bfB8HVK_MKoDHWFehjVNzJNuEOR7Ya3sty8ZYqWqqhNUx.vmQBJOZZxorNt.K813Gxk_fQAEWRWhW1Wexfni3W_z0zZfcLKuJJc76KHae2SnDF5qZj90Riplk.F4MmiTj3Nl_s_s; alg_wc_ev_my_account_referer_url=https%3A%2F%2Fcnfans.com%2Fzh%2Festimation%2F; _ga=GA1.2.1119239401.1739267717; _ga_GVNMMZMPG4=GS1.1.1739350664.4.1.1739351012.56.0.0; lf_prev_send_time=1739351054538"
}

response = session.post(url_cfans, headers=headers_cfans,params=params, data=multipart_data.encode())


# response = session.send(url_cfans, headers=headers_cfans,params=params)


# with httpx.Client(http2=True) as client:
#     client.headers.update(headers_cfans)
#     response = client.post(url=url_cfans, content=multipart_data.encode(),params=params)
#     request = response.request


# print(response.content.decode())

for item in response.json()["data"]:
    print(item)
