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
    f"--{boundary}--\r\n"
)

# 目标 URL
url_cfans = "https://cnfans.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

headers_cfans = {
    # ":method": "POST",
    # ":authority": "joyabuy.com",
    # ":scheme": "https",
    # ":path": "/wp-admin/admin-ajax.php?action=get_estimation_query_prices",
    # "content-length": str(len(data)),
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    # "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133")',
    "content-type": f"multipart/form-data; boundary={boundary}",
    # "content-type": multipart_data.content_type,
    "sec-ch-ua-mobile": "?0",
    "Accept": "*/*",
    "origin": "https://cnfans.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "Referer": "https://cnfans.com/zh/estimation/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    "connection":"keep-alive",
    "priority": "u=1, i",
    "Cookie": "wmc_current_currency=USD; wmc_current_currency_old=USD"
}

response = session.post(url_cfans, headers=headers_cfans)



print(response.content.decode())
