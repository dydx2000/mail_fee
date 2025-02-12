import requests

url_cnfans = "https://cnfans.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

params_cnfans = {
    "action": "get_estimation_query_prices"
}

headers = {
    "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryf3hnzsPMsWNrBTvw",
    "Origin":"https://cnfans.com",
    "Referer":"https://cnfans.com/zh/estimation/",
    "priority":"u=1, i",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Cookie": "pll_language=zh; lf_session_id=bcc81373-fc65-40d1-ad49-2e5389a55736; lf_first_visit=1739070628072; lf_prev_visit=1739070628072; __ukey=81n288jdx800; _gcl_au=1.1.997165745.1739070628; _tt_enable_cookie=1; _ttp=9ZfJV76oBGK2r66PT-bk81I6gAS.tt.1; _gid=GA1.2.95782528.1739070629; _ss_s_uid=794d38360ed3b348b16b30f5ba05689f; _hjSessionUser_3640651=eyJpZCI6ImMyMTM2OTdkLWM3YWQtNWVhMi1hNjQ4LTcwZmI0YWRkYjRiZSIsImNyZWF0ZWQiOjE3MzkwNzA2Mjg0ODUsImV4aXN0aW5nIjp0cnVlfQ==; wmc_current_currency=USD; wmc_current_currency_old=USD; cf_clearance=0RyHZJKQqkCkf.6lgMzYGOP4ICl_sW7DSVUWJE4SbKA-1739081585-1.2.1.1-yy4UsEorkA9CYi1taG3wfrsgtcpLkRpgUbhZJfgIMSueiYIadPVbCQg0dWnx8p8kDwnTGBSI.ZdvPGnuck8N8TT4xLcmqRwBcnyCwcPUISB6Mkkzm65lTt7gJN2my56VKkq60HTuP8_hCuBMwEUOD6VL6Y9pdK_iz3i.oKTZHmp64ZKyulIuS3jkSEDpP6V0IU5iPSxLBmVZRHA5Chdv6s1QoSouaVjjWfcaa9vf_Bdt3ijlhyLIQxQvwmhQujg.ZxLaGyoohbeOJ7YdZ3kNg5Rb5qW.s4F1te1npEBHoEM; lf_this_visit=1739081657585; lf_session_count=2; _hjSession_3640651=eyJpZCI6IjljOTEzZjRjLTY1YTctNDUwNy1hZDQzLTEyOWQ2MWYwNzFlNSIsImMiOjE3MzkwODE2NTc2MzIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=;"
              " _ga=GA1.2.1556063410.1739070628; _gat_gtag_UA_257386089_1=1; lf_prev_send_time=1739082046994; _ga_GVNMMZMPG4=GS1.1.1739081657.2.1.1739082052.51.0.0",
    "Accept":"*/*",
    "Accept-encoding":"gzip, deflate, br, zstd",
    # "accept-language": "zh-CN,zh;q=0.9"
    "Connection":"keep-alive"

}
data = {
    "destination": "SG",
    "weight": 5,
    "features":None,
    "length":5,
    "width":3,
    "height":4,
    "username":None,
    "password":None,
    "terms":1

}

response = requests.post(url=url_cnfans, data=data, headers=headers,params=params_cnfans)

print(response)
# print(response.status_code)
# print(response.json())

# fee_datas = response.json()

# print(fee_datas)


# for fee in fee_datas['data']:
#     if fee['available']:
#         print(fee)

