import jsonpath
import json

#所有电影
obj = json.load(open("douban.json","r",encoding="utf-8"))


title_list = jsonpath.jsonpath(obj,"$..title")
print(title_list)