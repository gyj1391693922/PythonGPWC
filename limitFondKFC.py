import urllib.parse
import urllib.request

def create_request(cName=None,
                   pageIndex=None,
                   pageSize=None
                   ):
    if(not cName):
        cname="北京"
    if(not pageIndex):
        pageIndex = "1"
    if(not pageSize):
        pageSize = "10"

    base_url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?"
    url_data = {"op":"cname"}
    url = base_url + urllib.parse.urlencode(url_data)
    base_data = {"cname":cname,"pid":"","pageIndex":pageIndex,"pageSize":pageSize}
    data = urllib.parse.urlencode(base_data).encode("utf-8")
    return urllib.request.Request(url,data)

def get_connect(request):
    response = urllib.request.urlopen(request)
    return response.read().decode("utf-8")

def to_json(content):
    import json
    object = json.loads(content)
    return object

def download_json(content):
    fp = open("kfc.json","w",encoding="utf-8")
    fp.write(content)

if __name__ == '__main__':
    request = create_request()
    contennt = get_connect(request)
    download_json(contennt)
