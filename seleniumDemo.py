from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = Service("chromedriver.exe")

browser = webdriver.Chrome(service=path)

# 访问网站
url = "https://www.baidu.com"
browser.get(url)
input("等待中...")
