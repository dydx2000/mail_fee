import requests

url_cnfans = "https://cnfans.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

params_cnfans = {
    "action": "get_estimation_query_prices"
}

headers = {
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryi8CXlapEX7BIAYV1",
    "Origin": "https://cnfans.com",
    "Referer": "https://cnfans.com/zh/estimation/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Cookie": "_gcl_au=1.1.663297501.1739267717; __ukey=81su6uvgx411; "
              "lf_session_id=855014af-26a8-4273-95b8-58c4303cf339; lf_first_visit=1739267718320; lf_prev_visit=1739267718320; "
              "lf_this_visit=1739267718320; lf_session_count=1;"
              " _hjSession_3640651=eyJpZCI6IjQ4MGRlZmNiLTNjNDAtNGU3YS04MzE0LWUyZDA0ZjNiYjNjZCIsImMiOjE3MzkyNjc3MTg2MDQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=;"
              " _ss_s_uid=9eb6242c0bcb35c9de9555eb2b9c731b; _gid=GA1.2.1713319632.1739267723; wmc_current_currency=CNY; wmc_current_currency_old=CNY;"
              " cf_clearance=Yd63sPt5GdK9s5A_ouWogqOGnyi6mbl471vibQTN_xo-1739267783-1.2.1.1-g_2Rpp.GmitbyNUP7HnQ6zUQmckuQUlHq_T_DL1E3DGUpYsy1OEkPRyVZkAXj"
              "EPr_nn_ehhZMpQjQu_KpvOut7ygUKTBrMYfNhsrwtpOIJn96JhtDTrIsqqKrsSHBmvyMWCbrpA8oN0a5SW_D9fBgoEA_gMSmQ2PlJ_h_5BfphMs62TmlhcnapVvarsQsgBw7m9lv"
              "revOL9unmoPNdVK40yOtgeslsOhzkSxHCIxBW9u2mwjp4xi.1.Tie8EVfV8vL13N_FbnP3aqUrnDqoQe2biI7DPtvSRmP7PUgNcpbM; _hjSessionUser_3640651=eyJpZCI6ImE"
              "0NDYzMzU5LWQyNjEtNTY2MC1iYjEyLWJmMGFhNDU5MDE5ZCIsImNyZWF0ZWQiOjE3MzkyNjc3MTg2MDMsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=aAvWa7i"
              "RdGoSTGo0yuifOZzhjrr.tt.1; pll_language=zh; _ga=GA1.2.1119239401.1739267717; _gat_gtag_UA_257386089_1=1; lf_prev_send_time=1739267863896; _ga_GVNMMZMPG4=GS1.1.1739267716.1.1.1739267869.49.0.0",
    "Accept": "*/*",
    "Accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
    "Connection": "keep-alive"

}

data = {
    "destination": "US",
    "weight": 500,
    # "features": None,
    # "length": None,
    # "width": None,
    # "height": None,
    # "username": None,
    # "password": None,
    "terms": 1

}

# response = requests.post(url=url_cnfans, data=data,headers=params_cnfans)
response = requests.post(url=url_cnfans, data=data, headers=headers, params= params_cnfans)

print(response.status_code)
# print(response.status_code)
# print(response.json())

# fee_datas = response.json()

# print(fee_datas)


# for fee in fee_datas['data']:
#     if fee['available']:
#         print(fee)
