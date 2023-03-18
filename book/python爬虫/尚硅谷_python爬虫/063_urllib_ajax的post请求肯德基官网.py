import urllib.request as r
import urllib.parse as p
import headers


def create_request(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '南通',
        'pid': '',
        'pageIndex': str(page),
        'pageSize': '10'
    }
    data = p.urlencode(data).encode('utf-8')
    request = r.Request(url, data, headers.HEADERS)

    return request


def get_content(request):
    response = r.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content, page):
    with open(f'./file/kfc_{str(page)}.json', 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    start_page = int(input('起始页码'))
    end_page = int(input('结束页码'))
    for page in range(start_page, end_page + 1):
        down_load(get_content(create_request(page)), page)
