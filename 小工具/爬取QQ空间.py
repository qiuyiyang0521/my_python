import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def login(login_qq, password, business_qq):
    '''
    登陆
    :param login_qq: 登陆用的QQ
    :param password: 登陆的QQ密码
    :param business_qq: 业务QQ
    :return: driver
    '''
    service = Service(executable_path='./chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    browser.get('https://user.qzone.qq.com/{}/311'.format(business_qq))  # URL
    browser.implicitly_wait(10)  # 隐示等待，为了等待充分加载好网址
    browser.find_element(By.ID, 'login_div')
    browser.switch_to.frame('login_frame')  # 切到输入账号密码的frame
    browser.find_element(By.ID, 'switcher_plogin').click()  # 点击‘账号密码登录’
    browser.find_element(By.ID, 'u').clear()  # 清空账号栏
    browser.find_element(By.ID, 'u').send_keys(login_qq)  # 输入账号
    browser.find_element(By.ID, 'p').clear()  # 清空密码栏
    browser.find_element(By.ID, 'p').send_keys(password)  # 输入密码
    browser.find_element(By.ID, 'login_button').click()  # 点击‘登录’
    browser.switch_to.default_content()

    browser.implicitly_wait(10)
    time.sleep(5)

    try:
        browser.find_element(By.ID, 'QM_OwnerInfo_Icon')
        return browser
    except:
        print('不能访问' + business_qq)
        return None


def get_shuoshuo(driver):
    driver.get('https://user.qzone.qq.com/1875508275/311')
    while True:
        # 下拉滚动条
        for j in range(1, 5):
            driver.execute_script("window.scrollBy(0,5000)")
            time.sleep(2)

        # 切换 frame
        driver.switch_to.frame('app_canvas_frame')
        # 构建 BeautifulSoup 对象
        bs = BeautifulSoup(driver.page_source.encode(
            'GBK', 'ignore').decode('gbk'))
        # 找到页面上的所有说说
        pres = bs.find_all('pre', class_='content')
        with open(r'F:\GitHub\shuoshuo.txt','w',encoding='utf-8') as fp:
            for pre in pres:
                shuoshuo = pre.text
                tx = pre.parent.parent.find(
                    'a', class_="c_tx c_tx3 goDetail")['title']
                fp.write(tx + ":" + shuoshuo + '\n')
        break

def get_photo(driver):
    
    # 照片下载路径
    photo_path = "C:/Users/一阳/Desktop/photo/{}/{}.jpg"
    
    # 相册索引
    photoIndex = 1

    while True:
        driver.get('https://user.qzone.qq.com/1875508275/4')
        #等待加载
        driver.implicitly_wait(10)
        time.sleep(3)
        # 切换 frame
        driver.switch_to.frame('app_canvas_frame')
        # 各个相册的超链接
        a = driver.find_elements(By.CLASS_NAME,'album-cover')
        # 单个相册
        a[photoIndex].click()

        driver.implicitly_wait(10)
        time.sleep(3)
        # 相册的第一张图
        p = driver.find_elements(By.CLASS_NAME,'item-cover')[0]
        p.click()
        time.sleep(3)

        # 相册大图在父frame，切换到父frame
        driver.switch_to.parent_frame()
        # 循环相册中的照片
        while True:
            # 照片url地址和名称
            img = driver.find_element(By.ID,'js-img-disp')
            src = img.get_attribute('src').replace('&t=5', '')
            name = driver.find_element(By.ID,"js-photo-name").text

            # 下载
            urlretrieve(src, photo_path.format('qq', name))

            # 取下面的 当前照片张数/总照片数量
            counts = driver.find_element(By.XPATH,'//*[@id="js-ctn-infoBar"]/div/div[1]/span').text

            counts = counts.split('/')
            # 最后一张的时候退出照片浏览
            if int(counts[0]) == int(counts[1]):
                # 右上角的 X 按钮
                driver.find_element(By.XPATH,'//*[@id="js-viewer-main"]/div[1]/a').click()
                break
            # 点击 下一张，网页加载慢，所以10次加载
            for i in (1, 10):
                if driver.find_element(By.ID,'js-btn-nextPhoto'):
                    n = driver.find_element(By.ID,'js-btn-nextPhoto')
                    webdriver.ActionChains(driver).click(n).perform()
                    break
                else:
                    time.sleep(5)

        # 相册数量比较，是否下载了全部的相册
        photoIndex = photoIndex + 1
        if len(a) <= photoIndex:
            break



driver = login('2213090041', '214910mm', '2213090041')
get_photo(driver)

