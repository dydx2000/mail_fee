import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# 目标 URL
url = "https://joyabuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

# 构造 MultipartEncoder
multipart_data = MultipartEncoder(
    fields={
        "destination": "CA",
        "weight": "600",
        "features": None,
        "length": None,
        "width": None,
        "height": None,
        "username": None,
        "password": None,
    }
)

# 设置 headers
headers3 = {
    "Content-Type": multipart_data.content_type,
    "Cookie": "wmc_current_currency=USD; wmc_current_currency_old=USD; pll_language=en; _ss_s_uid=9eb6242c0bcb35c9de9555eb2b9c731b; _ga=GA1.1.1778277922.1739259791; __ukey=81sml3atx5; PHPSESSID=jmfohumqqujm5v4qkfvpqcreqo; _ga_LLNZ3BEEWR=GS1.1.1739324439.5.0.1739324439.0.0.0",
    "Accept": "*/*",
    "Origin": "https://joyabuy.com",
    "Referer": "https://joyabuy.com/estimation/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

# 发送请求
session = requests.session()
session.headers.update(headers3)
response = session.post(url, content=multipart_data, )

# 打印响应
print("Response Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Body:", response.text)