import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 配置选项
options = Options()

# 设置使用无头浏览器
options.add_argument("--headless")
chromedriver_path = "./chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# 初始化浏览器


driver.get("https://joyabuy.com")

time.sleep(3)

# 通过执行 JavaScript 获取接口返回值
api_response = driver.execute_script('''
return fetch('https://joyabuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices',
             {
                 method: 'post',
                 headers: {
                     'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarysvDJMJtf1rSuuWAJ',
                     'Accept': '*/*',
                     'Origin': 'https://joyabuy.com',
                     'Referer': 'https://cnfans.com/zh/estimation/',
                     'Cookie': 'wmc_current_currency=USD; wmc_current_currency_old=USD; pll_language=en; _ss_s_uid=9eb6242c0bcb35c9de9555eb2b9c731b; _ga=GA1.1.1778277922.1739259791; __ukey=81sml3atx5; PHPSESSID=jmfohumqqujm5v4qkfvpqcreqo; _ga_LLNZ3BEEWR=GS1.1.1739320600.4.1.1739321258.0.0.0'
                 }
             }).then(response => response.json());
             ''')

print("API Response:", api_response)

# 访问网页
# driver.post('https://orientdig.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices')
#
# # 打印标题
# # print(driver.title)

# 关闭浏览器
driver.close()
