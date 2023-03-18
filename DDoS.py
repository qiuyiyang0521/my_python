from email import header
import threading
import requests


def run(url):
    while True:
        try:
            response = requests.get(url, header={
                                    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})
            print("状态码:", requests.status_codes)
        except:
            pass


for i in range(50000):
    threading.Thread(target=run, args=(
        "https://qiuyiyang0521.github.io")).start()
