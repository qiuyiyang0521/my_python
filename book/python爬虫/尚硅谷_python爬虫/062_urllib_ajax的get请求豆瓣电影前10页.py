import urllib.request as r
import urllib.parse as p
import headers


# https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&
# start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&
# start=20&limit=20

# https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&
# start=40&limit=20

# https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&
# start=60&limit=20

# start=(page - 1) * 20

def create_request(url):
    request = r.Request(url, headers=headers.HEADERS)
    reponse = r.urlopen(request)
    return reponse

def create_content(response):
    content = response.read().decode('utf-8')
    return content

def down_load(page,content):
    with open(f'./file/douban_{page}.json','w',encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    start_page = int(input('起始页码\n'))
    end_page = int(input('结束页码\n'))
    for page in range(start_page,end_page+1):
        data = {
            'start' : str((page - 1) * 20),
            'limit' : '20'
        }
        data = p.urlencode(data)
        url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&' + data
        down_load(page,create_content(create_request(url)))
