import requests
url = 'https://play.qiqiuyun.net/sdk_api/video/hls_stream/shd.m3u8?resNo=474e53d854b6449880cf24ea132f5cde&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsZXZlbCI6InNoZCIsInByZXZpZXciOm51bGwsInBsYXlBdWRpbyI6MCwiaGVhZCI6bnVsbCwic2tpcCI6bnVsbCwibm8iOiI0NzRlNTNkODU0YjY0NDk4ODBjZjI0ZWExMzJmNWNkZSIsImp0aSI6IjYxNWQ0ZjMwLWJjZWYtNDkiLCJ0aW1lcyI6MSwiZXhwIjoxNjc2MTE1NTM1LCJlbmNyeXB0IjoyLCJuYXRpdmUiOjAsImhsc0NsZWZFbmNyeXB0VmVyc2lvbiI6Mn0.0lMwBt3-bsk-sVc03IpytcHMv7Ayeywrjy7AnrDS-Ws&ssl=1'
headers = {
    ':authority': 'play.qiqiuyun.net',
    ':method': 'GET',
    ':path': '/sdk_api/video/hls_stream/shd.m3u8?resNo=474e53d854b6449880cf24ea132f5cde&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsZXZlbCI6InNoZCIsInByZXZpZXciOm51bGwsInBsYXlBdWRpbyI6MCwiaGVhZCI6bnVsbCwic2tpcCI6bnVsbCwibm8iOiI0NzRlNTNkODU0YjY0NDk4ODBjZjI0ZWExMzJmNWNkZSIsImp0aSI6IjYxNWQ0ZjMwLWJjZWYtNDkiLCJ0aW1lcyI6MSwiZXhwIjoxNjc2MTE1NTM1LCJlbmNyeXB0IjoyLCJuYXRpdmUiOjAsImhsc0NsZWZFbmNyeXB0VmVyc2lvbiI6Mn0.0lMwBt3-bsk-sVc03IpytcHMv7Ayeywrjy7AnrDS-Ws&ssl=1',
    ':scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6',
    'origin': 'https://service-cdn.qiqiuyun.net',
    'referer': 'https://service-cdn.qiqiuyun.net/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
}
response = requests.get(url,headers)
response.encoding='utf-8'
print(response.text)
