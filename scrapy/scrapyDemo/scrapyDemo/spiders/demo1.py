import scrapy
import re

class Demo1Spider(scrapy.Spider):
    name = "demo1"
    allowed_domains = ["192.168.23.44:8080"]
    start_urls = ["http://192.168.23.44:8080"]

    def parse(self, response):
        # content = response.xpath("//img[contains(@class,'image')]/@src")
        # for c in content:
        #     print(c)

        html_content = response.text

        # 使用正则表达式匹配分页链接
        pattern = r'<a href="(.*?)">(\d+)</a>'  # 假设分页链接的 HTML 格式为 <a href="链接地址">页码</a>
        page_links = re.findall(pattern, html_content)

        # 输出匹配到的分页链接
        for link, page_num in page_links:
            print("====================================================")
            print(f"Page {page_num}: {link}")
