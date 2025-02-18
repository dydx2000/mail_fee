import hashlib
import random
import time
import uuid

import requests

def genXs():
    x_nonce = str(uuid.uuid4())  # 生成随机 UUID
    # print("x_nonce:", x_nonce)

    signKey = "980683EF-46C6-47D5-80C1-7B2CB6B2D0BF"

    str_tohash = str(x_nonce) + signKey

    # 生成 x_signature 的方法
    def md5_hash_str(str_tohash):
        # 创建一个 MD5 对象
        md5 = hashlib.md5()
        # 将输入字符串编码为字节类型，因为 update 方法需要字节类型的参数
        input_bytes = str_tohash.encode('utf-8')
        # 使用 update 方法更新 MD5 对象的状态，传入要计算哈希值的字节数据
        md5.update(input_bytes)
        # 获取计算得到的 MD5 哈希值，并以十六进制字符串的形式返回
        return md5.hexdigest()

    # 调用自定义的 md5_hash_str 函数进行哈希计算
    x_signature = str(md5_hash_str(str_tohash))
    # print("hash_result:",x_signature)

    return (x_nonce, x_signature)




# 生成类似长度的整数部分
integer_part = random.randint(171446900, 171447000)
# 生成类似长度的小数部分，这里控制小数部分为 9 位
decimal_part = random.randint(100000000, 999999999) / 1e9
# 组合整数部分和小数部分
x_client_id = str(integer_part + decimal_part)
print("x-client-id:", x_client_id)

url_hoobuy = "https://api.hoobuy.com/hoobuy_express/express/pub/postage"


x_nonce, x_signature = genXs();

headers = {
    "x-client-id": x_client_id,
    "x-nonce": x_nonce,
    "x-signature": x_signature,
    "x-platform": "web",
    "x-version": "hoobuy-production-web-1.0",
    "Origin": "https://hoobuy.com",
    # "Referer":"https://cnfans.com/zh/estimation/",
    # "priority":"u=1, i",
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    # "Cookie": "pll_language=zh; lf_session_id=bcc81373-fc65-40d1-ad49-2e5389a55736; lf_first_visit=1739070628072; lf_prev_visit=1739070628072; __ukey=81n288jdx800; _gcl_au=1.1.997165745.1739070628; _tt_enable_cookie=1; _ttp=9ZfJV76oBGK2r66PT-bk81I6gAS.tt.1; _gid=GA1.2.95782528.1739070629; _ss_s_uid=794d38360ed3b348b16b30f5ba05689f; _hjSessionUser_3640651=eyJpZCI6ImMyMTM2OTdkLWM3YWQtNWVhMi1hNjQ4LTcwZmI0YWRkYjRiZSIsImNyZWF0ZWQiOjE3MzkwNzA2Mjg0ODUsImV4aXN0aW5nIjp0cnVlfQ==; wmc_current_currency=USD; wmc_current_currency_old=USD; cf_clearance=0RyHZJKQqkCkf.6lgMzYGOP4ICl_sW7DSVUWJE4SbKA-1739081585-1.2.1.1-yy4UsEorkA9CYi1taG3wfrsgtcpLkRpgUbhZJfgIMSueiYIadPVbCQg0dWnx8p8kDwnTGBSI.ZdvPGnuck8N8TT4xLcmqRwBcnyCwcPUISB6Mkkzm65lTt7gJN2my56VKkq60HTuP8_hCuBMwEUOD6VL6Y9pdK_iz3i.oKTZHmp64ZKyulIuS3jkSEDpP6V0IU5iPSxLBmVZRHA5Chdv6s1QoSouaVjjWfcaa9vf_Bdt3ijlhyLIQxQvwmhQujg.ZxLaGyoohbeOJ7YdZ3kNg5Rb5qW.s4F1te1npEBHoEM; lf_this_visit=1739081657585; lf_session_count=2; _hjSession_3640651=eyJpZCI6IjljOTEzZjRjLTY1YTctNDUwNy1hZDQzLTEyOWQ2MWYwNzFlNSIsImMiOjE3MzkwODE2NTc2MzIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=;"
    #           " _ga=GA1.2.1556063410.1739070628; _gat_gtag_UA_257386089_1=1; lf_prev_send_time=1739082046994; _ga_GVNMMZMPG4=GS1.1.1739081657.2.1.1739082052.51.0.0",
    "Accept": "*application/json",
    # "Accept-encoding":"gzip, deflate, br, zstd",
    # # "accept-language": "zh-CN,zh;q=0.9"
    # "Connection":"keep-alive"

}
data = {"country": "US", "requestType": 1,
        "arr": [{"weight": 850, "long": 0, "width": 0, "height": 0, "count": 1, "coefficient": 1}]}

response = requests.post(url=url_hoobuy, json=data, headers=headers, verify=False)

my_feedata = {}
my_feedata["国家"] = 'US'
my_feedata["重量"] = "600"
my_feedata["网站"] = []

fee_datas = response.json()

# print("response:", fee_datas)

curSiteInfo = {"siteName": "hoobuy", "venders": []}

ids = []
for fee in fee_datas['data']['lines']:
    if fee['state'] == "available":
        ids.append(fee['id'])

for fee in fee_datas['data']['lines']:
    if fee['state'] == "available":
        curSiteInfo['venders'].append(
            {"id": fee['id'],
             "venderName": fee['lineName'],
             '总价': str(float(fee['operationFee']) + float(fee['price'])),
             '首重价格': 0, #
             "额外重量价格": 0, #
             "操作费": fee["operationFee"],
             "服务费": 0, #
             "最低重量限制": None, #
             "最高重量限制": None, #
             "尺寸限制": None, #
             "体积重量计费规则": None, #
             "运输时间": fee["timeRequired"]},
        )


print("ids: ",ids)
details = []
for line_id in ids:
    x_nonce, x_signature = genXs();

    headers = {
        "x-client-id": x_client_id,
        "x-nonce": x_nonce,
        "x-signature": x_signature,
        "x-platform": "web",
        "x-version": "hoobuy-production-web-1.0",
        "Origin": "https://hoobuy.com",
        # "Referer":"https://cnfans.com/zh/estimation/",
        # "priority":"u=1, i",
        # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        # "Cookie": "pll_language=zh; lf_session_id=bcc81373-fc65-40d1-ad49-2e5389a55736; lf_first_visit=1739070628072; lf_prev_visit=1739070628072; __ukey=81n288jdx800; _gcl_au=1.1.997165745.1739070628; _tt_enable_cookie=1; _ttp=9ZfJV76oBGK2r66PT-bk81I6gAS.tt.1; _gid=GA1.2.95782528.1739070629; _ss_s_uid=794d38360ed3b348b16b30f5ba05689f; _hjSessionUser_3640651=eyJpZCI6ImMyMTM2OTdkLWM3YWQtNWVhMi1hNjQ4LTcwZmI0YWRkYjRiZSIsImNyZWF0ZWQiOjE3MzkwNzA2Mjg0ODUsImV4aXN0aW5nIjp0cnVlfQ==; wmc_current_currency=USD; wmc_current_currency_old=USD; cf_clearance=0RyHZJKQqkCkf.6lgMzYGOP4ICl_sW7DSVUWJE4SbKA-1739081585-1.2.1.1-yy4UsEorkA9CYi1taG3wfrsgtcpLkRpgUbhZJfgIMSueiYIadPVbCQg0dWnx8p8kDwnTGBSI.ZdvPGnuck8N8TT4xLcmqRwBcnyCwcPUISB6Mkkzm65lTt7gJN2my56VKkq60HTuP8_hCuBMwEUOD6VL6Y9pdK_iz3i.oKTZHmp64ZKyulIuS3jkSEDpP6V0IU5iPSxLBmVZRHA5Chdv6s1QoSouaVjjWfcaa9vf_Bdt3ijlhyLIQxQvwmhQujg.ZxLaGyoohbeOJ7YdZ3kNg5Rb5qW.s4F1te1npEBHoEM; lf_this_visit=1739081657585; lf_session_count=2; _hjSession_3640651=eyJpZCI6IjljOTEzZjRjLTY1YTctNDUwNy1hZDQzLTEyOWQ2MWYwNzFlNSIsImMiOjE3MzkwODE2NTc2MzIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=;"
        #           " _ga=GA1.2.1556063410.1739070628; _gat_gtag_UA_257386089_1=1; lf_prev_send_time=1739082046994; _ga_GVNMMZMPG4=GS1.1.1739081657.2.1.1739082052.51.0.0",
        "Accept": "*application/json",
        # "Accept-encoding":"gzip, deflate, br, zstd",
        # # "accept-language": "zh-CN,zh;q=0.9"
        # "Connection":"keep-alive"

    }
    data = {"lineId":line_id}

    url_detail='https://api.hoobuy.com/hoobuy_order/pub/v2/express/line/detail'

    response = requests.post(url=url_detail, json=data, headers=headers, verify=False)
    detail = response.json()
    details.append({'id':line_id ,
                    "最低重量限制":  detail['data']['weightLimit']['lowestWeight'],
                    "最高重量限制":  detail['data']['weightLimit']['highestWeight'],
                    "尺寸限制": detail['data']['sizeLimit']
                    })
    time.sleep(0.5)

merged_list =[]

for dic1,dic2 in zip(curSiteInfo['venders'],details):
    merged_dic = dic1.copy()
    merged_dic.update(dic2)
    merged_list.append(merged_dic)

curSiteInfo['venders'] =merged_list

print(merged_list)

my_feedata['网站'].append(curSiteInfo)

print(curSiteInfo)

# print(my_feedata)
# for item in my_feedata['网站']['venders']:
#     print(item)

# print(response.status_code)
# print(response.json())

# fee_datas = response.json()

# print(fee_datas)


# for fee in fee_datas['data']:
#     if fee['available']:
#         print(fee)
