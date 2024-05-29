from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def headlessAction():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    path = Service("chromedriver.exe")
    browser = webdriver.Chrome(service=path,options=chrome_options)
    url = "http://www.baidu.com"
    browser.get(url)
    print("end...")
    browser.save_screenshot('baidu.png')



def elementAction():
    path = Service("chromedriver.exe")
    browser = webdriver.Chrome(service=path)
    url = "https://www.baidu.com"
    browser.get(url)

    import time
#     获取文本框的对象
    input = browser.find_element("id","kw")
    input.send_keys("周杰伦")
#     获取百度一下的按钮
    button = browser.find_element("id","su")
    button.click()
#     滑倒底部
    js_button = "document.documentElement.scrollTop=100000"
    time.sleep(2)
    browser.execute_script(js_button)
    next = browser.find_element("xpath","//a[@class='n']")
    next.click()
    time.sleep(1)
    browser.back()
    browser.forward()
    time.sleep(5)
    browser.close()


def elementDetail():
    path = Service("chromedriver.exe")
    browser = webdriver.Chrome(service=path)
    url = "https://www.baidu.com"
    browser.get(url)
    input = browser.find_element("id","su")
    # 获取css样式
    print(input.get_attribute("class"))
    # 获取文本
    print(input.text)
    # 获取标签名
    print(input.tag_name)



def moniChrome():
    path = Service("chromedriver.exe")
    browser = webdriver.Chrome(service=path)
    url = "https://www.baidu.com"
    browser.get(url)
# 元素定位
    button = browser.find_element("id","su")
    print(button)
    namebutton = browser.find_element("name","wd")
    print(namebutton)
    xpathbutton = browser.find_element("xpath","//input[@id='su']")
    print(xpathbutton)
    tagbutton = browser.find_element("tag name","input")
    print(tagbutton)
    cssbutton = browser.find_element("css selector","#su")
    print(cssbutton)
    linkbutton = browser.find_element("link text","贴吧")
    print(linkbutton)



def testSelenium():
    path = Service("chromedriver.exe")

    browser = webdriver.Chrome(service=path)

    # 访问网站
    url = "https://www.baidu.com"
    browser.get(url)
    input("等待中...")


if __name__ == '__main__':
    headlessAction()