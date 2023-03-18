import urllib.request as r
headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
    'Cookie': 'online-uuid=0D97CBE9-629F-5F0B-40A8-9C684C388180; PHPSESSID=jn41a9t6rm1gjbra15djih2uo3; REMEMBERME=Qml6XFVzZXJcQ3VycmVudFVzZXI6ZFhObGNsOXphbWMzY1dvM04zcEFaV1IxYzI5b2J5NXVaWFE9OjE3MDQ5NjE2MTQ6M2YyOTA3OWQzZGYyYWY3YTUxMTVkOWJjZTkzOWFjZTdlYzQzMjc0MzA4M2M2NmQ2ODQxZTMyMTI1OTU1YzgwZA=='
}
url = 'https://www.gulixueyuan.com/course/455/task/20264/show'
request = r.Request(url, headers=headers)
response = r.urlopen(request)
content = response.read().decode('utf-8')

with open('./page.html', 'w', encoding='utf-8') as file:
    file.write(content)
