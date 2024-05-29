import urllib.request
import urllib.parse

def proxyPool():
    proxy_pool = [
        {"http": "xxx.xxx.xxx.xxx:xx"},
        {"http": "yyy.yyy.yyy.yyy:yy"},
        {"http": "zzz.zzz.zzz.zzz:zz"},
        {"http": "aaa.aaa.aaa.aaa:aa"},
        {"http": "bbb.bbb.bbb.bbb:bb"}
    ]
    import random
    proxies = random.choice(proxy_pool)
    print(proxies)


def proxyObject():
    # 代理使用 ： 快代理
    url = "http://www.baidu.com/s?"
    data = {"wd":"我的ip"}
    url = url + urllib.parse.urlencode(data)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"}
    request = urllib.request.Request(url,headers=headers)
    #代理
    # 模拟浏览器访问服务器
    proxies = {
        "http":"218.87.205.18:16906"
    }
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode("utf-8")
    with open("bd.html","w",encoding="utf-8") as fp:
        fp.write(content)
    print(content)




def handler():
    url = 'http://www.baidu.com'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"}
    request = urllib.request.Request(url=url,headers=headers)
    # 获取handler对象
    handler = urllib.request.HTTPHandler()
    # 获取opener对象
    opener = urllib.request.build_opener(handler)
    # 调用open方法
    response = opener.open(request)
    content = response.read().decode("utf-8")
    print(content)


def doubanTop10():
    url = "https://movie.douban.com/j/search_subjects?"
    data = {
        "type":"movie",
        "tag":"热门",
        "page_limit":"50",
        "page_start":"0"
    }
    data = urllib.parse.urlencode(data)
    url = url + data
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"}
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")

    pf = open("douban.json","w",encoding="utf-8")
    pf.write(content)




def postHeaders():
    url = "https://fanyi.baidu.com/v2transapi"
    headers = {"Cookie":'BAIDUID=CB17014A1A9651257CCFEB06E1039122:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1710329918,1710489438,1710895926,1711357039; PSTM=1713229779; BDUSS=WhtVmgzdzNJTU9ZcnRCajE4ekZMdlUybjQ3MTk5T29-MkhCblpENUZpdWtsbGhtSVFBQUFBJCQAAAAAAAAAAAEAAAAlL45A1ru74c7KzsrM4jMzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKQJMWakCTFmb; BDUSS_BFESS=WhtVmgzdzNJTU9ZcnRCajE4ekZMdlUybjQ3MTk5T29-MkhCblpENUZpdWtsbGhtSVFBQUFBJCQAAAAAAAAAAAEAAAAlL45A1ru74c7KzsrM4jMzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKQJMWakCTFmb; H_PS_PSSID=60270_60279_60287_60297; BIDUPSID=8EF94B833B9030FACB77FFBD4C042BA9; BAIDUID_BFESS=CB17014A1A9651257CCFEB06E1039122:FG=1; H_WISE_SIDS=60270_60279_60287_60297; delPer=0; PSINO=7; BA_HECTOR=ag8la5848085ahala1a184a46o76hr1j5af0h1v; ZFY=Uaw3dGvcOr6hr24of0NlpMDLAr6LMBJSnB6QKcDizSw:C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_OWY2Nzc2OTc4N2FlNzA1NjBhM2RmNDlhYTFkNmE3MmRmZjZmZGQxZjAzZDUyNzhhOGNhZDQ0OWYyOWIzZDUyYWU4YjczZWZiMGJjMzQ4YTJiMzU3MTdkZTAwOWQ4YzgxYWViMzM1YmY0NmY5YzMwYzI2MjI5NTc0NGFiMzBiMjkzODE3YjM5OTg4OGM0OWMzNjc2OTY4OWU3OTMxZTBkOA==; RT="z=1&dm=baidu.com&si=4a7af1db-dd5b-4b90-ac0c-98283db45eb8&ss=lwps6pls&sl=2&tt=2rd&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=tel"'}
    data = {
        "from":"en",
        "to":"zh",
        "query":"love",
        "transtype":"realtime",
        "simple_means_flag":"3",
        "sign":"198772.518981",
        "token":"5483bfa652979b41f9c90d91f3de875d",
        "domain":"common"
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    request = urllib.request.Request(url=url,data=data,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    import json
    js = json.loads(content)
    print(js)

def posturl():
    url = "https://fanyi.baidu.com/sug"
    data = {"kw":"spider"}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    data = urllib.parse.urlencode(data).encode("utf-8")
    request = urllib.request.Request(url=url,data=data,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")

    import json
    obj = json.loads(content)
    print(obj)

def urlcodes():
    url = "https://www.baidu.com/s?"
    data = {
        "wd":"周杰伦",
        "sex":"男"
    }

    value = urllib.parse.urlencode(data)
    url = url + value
    print(url)


def unicodes():
    url = "https://www.baidu.com/s?wd="
    UA = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}

    name = urllib.parse.quote("周杰伦")
    url = url+name
    request = urllib.request.Request(url=url,headers=UA)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    print(content)

def ua():
    UA = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"}
    url="https://www.baidu.com"
    req = urllib.request.Request(url=url,headers=UA)
    response = urllib.request.urlopen(req)
    content = response.read().decode("utf-8")
    print(content)



def download():
    url_page = "http://www.baidu.com"
    # url代表的是下载的路径,filename代表的是文件名
    urllib.request.urlretrieve(url = url_page,filename="baidu.html")




def getContent():
    # 定义URL
    url = "http://www.baidu.com"
    # 模拟浏览器向服务器发送请求
    response = urllib.request.urlopen(url)
    # 获取响应的源码
    content = response.read().decode("utf-8")
    print(content)


if __name__ == '__main__':
    proxyPool()