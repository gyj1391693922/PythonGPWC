from lxml import etree
import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
content = response.read().decode("utf-8")
tree = etree.HTML(content)
print(tree.xpath("//input[@id='su']/@value"))