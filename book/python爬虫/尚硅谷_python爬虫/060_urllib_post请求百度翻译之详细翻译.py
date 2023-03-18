import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': 'f32dff1212d40b0d37b00dfdb1cf9c62',
    'domain': 'common'
}

headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6',
    'Acs-Token': '1673251572751_1673333601105_g/6mSzLifSgrvS9aigTiHaa2mNJp+F23zS0kMgG5BwbwLxklz590COkqt0AaTh0pFrRKS20nlFrtMa7AUxDAs/c76shAFC11er9gnra0ZzVAjUQ0pU4biyFKghryElAP/itqTt9JyLq2oekR1hUW9uRiqWbn1kgvkVh5nN9CUGbuLqoj9srrLMCyy1fbb6j65nrfi9EBySoHg1xYSTfpmxRDGZGdPpHXQp3VPPUYAlcKFGGT/H9RRasDf60tuMHR6kVdRQkGEthWE6Kf8t8xYd0nGXxzMN2TUHcJ2/GsSQ4AGUh9OIN93tipkHdhNgHAusuK+XMOm5dJSG0nWycEfg==',
    'Connection': 'keep-alive',
    'Content-Length': '135',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=9FC4DC3967203D5975D8ED2690E7D5B3:FG=1; PSTM=1664007516; BIDUPSID=9FC4DC3967203D59D639D0755669F2AF; ZFY=WCXoFoVgXlQUBeY:A3q:A3phc:Btuoy60qOubnDZjYGC1w:C; BDUSS_BFESS=mQwTzlmOW9NcDdmaUY0cTZHbVRrM0hTMlRaZVY4ajl4UjJ0Zy1uZlB5NE4tMlJqSVFBQUFBJCQAAAAAAAAAAAEAAAAxUjU60rvR9NH0xNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1uPWMNbj1jU; BDUSS=mQwTzlmOW9NcDdmaUY0cTZHbVRrM0hTMlRaZVY4ajl4UjJ0Zy1uZlB5NE4tMlJqSVFBQUFBJCQAAAAAAAAAAAEAAAAxUjU60rvR9NH0xNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1uPWMNbj1jU; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221379827690%22%2C%22first_id%22%3A%22183a7f5d9b332a-070b6a69d5b9e6-9156d2c-2073600-183a7f5d9b412a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22183a7f5d9b332a-070b6a69d5b9e6-9156d2c-2073600-183a7f5d9b412a%22%7D; __bid_n=1846142ed8bfa9fc124207; FEID=v10-f3e1d33e5f2f794ed586b9a02ec19c8211f92e6b; BAIDU_WISE_UID=wapp_1671249712222_349; BAIDUID_BFESS=9FC4DC3967203D5975D8ED2690E7D5B3:FG=1; __xaf_fpstarttimer__=1672235256298; __xaf_thstime__=1672235257389; __xaf_fptokentimer__=1672235257437; FPTOKEN=X1ss3DD3NU1AKL1GcZ3QUlhMi3GBk7BL6QyopjRqDsZ42EVTatIjyE8ruSA4hj/bDuqnbiAtgeZa4aClHzHPiuObAwOBFaZbYq8LIys+6ClL3ESLW+Om3pydX0DQO5FgHy5UjXF219okNEXlLc0DKLhGFhwQ+evVd7p6U3Jq+1RR7pYhJbC8KAHH8P2ZdE2gcdFN6za5AjfMhppucQkU7o3mgv7Qb2zIX6snAzw/I5TwpZiwg6Y5ptXhbCR1a7j9jNqMkvoGXXU+vX5eGdZPoJKpti8iY64DKVJRnejq1WH8n7L+zN+Yl5Y5fP6VUxbNeVxP318u5gOhf3TFh1lMeW4SAbt5/7QAznMqQc7trFPuWl0ZQ0nPvdS+azTQbRgSK7A23WEApbqc/5pZBioSys7zM4Iuk6o9fB0eo/Q8Wul4qFWoFSqECIeg1xjk6UzY|jY9eRrsBZ/+sfRNGroUEOIMpaF8LcrPxzsbR+T0WnIw=|10|d6f832ec671fc1a090a6265dfc436cb8; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1673331467,1673333569; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1673333569; ab_sr=1.0.1_ZjVmNmFhZTQyMGY3YWQ5MzBkN2ZlMWQ3ODAyMWM5YWExOWYzZjI4YTEyOThmYzBjNDQ0MjA5MWY3ZGJlODgyYTNlMjBkMTA3NzA4ZGYzZjUwZmNiNTg5ZDE0Zjg3OTAyOWEyM2MzOTBmZWE5OTY0Mzg3OTdmZGFmM2IzOGI4MDMyYTY3NTg2ZmY0YjBhMzE0MWEyMzE3NWEwN2M0MTVhYzhlMzczOTk3ZDE5Y2IwYWVjYmQ1MzQ0NTExZGEzNDYw',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
    'X-Requested-With': 'XMLHttpRequest',
}

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

obj = json.loads(content)
print(obj)
