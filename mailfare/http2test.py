import requests
import httpx

# 目标 URL
url = "https://joyabuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"
# 伪造 Headers
headers3 = {
    ":method": "POST",
    ":authority": "joyabuy.com",
    ":scheme": "https",
    ":path": "/wp-admin/admin-ajax.php?action=get_estimation_query_prices",
    # "Content-length": "803",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133")',
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryScZrRerJ5PtBeaKw",
    "sec-ch-ua-mobile": "?0",
    "accept": "*/*",
    "Origin": "https://joyabuy.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "Referer": "https://joyabuy.com/estimation/",
    "Accept-encoding": "gzip, deflate, br, zstd",
    "Accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    "priority": "u=1, i"
}

# 伪造 Cookie
cookies = {
    "wmc_current_currency": "USD",
    "wmc_current_currency_old": "USD",
    "pll_language": "en",
    "_ss_s_uid": "9eb6242c0bcb35c9de9555eb2" }

class HTTPAdapterWithHTTP2(requests.adapters.HTTPAdapter):
    def __init__(self):
        self.httpx_client = httpx.Client(http2=True)
        super().__init__()

    def send(self, request, **kwargs):
        response = self.httpx_client.request(
            method=request.method,
            url=request.url,
            headers=request.headers,
            data=request.body,
        )
        return response

# 创建 session 并使用 HTTP/2 适配器
session = requests.Session()
session.mount("https://", HTTPAdapterWithHTTP2())

response = session.post(url)
print(response.status_code)
print(response.text)
