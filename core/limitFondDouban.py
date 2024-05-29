import urllib.request
import urllib.parse

def create_request(pageIndex = None,pageLength = None,tagtype = None):
    if not pageIndex:
        pageIndex = 0
    if not pageLength:
        pageLength = 20
    if not tagtype:
        tagtype = "热门"
    url = "https://movie.douban.com/j/search_subjects?"
    data = {
        "type": "movie",
        "tag": tagtype,
        "page_limit": pageLength,
        "page_start": pageIndex
    }
    data = urllib.parse.urlencode(data)
    url = url + data
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"}
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_connect(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content

def downloadMovies(content):
    with open("douban.json","w",encoding="utf-8") as fp:
        fp.write(content)

def toJson(content):
    import json
    return json.loads(content)

if __name__ == '__main__':
    re = create_request()
    con = get_connect(re)
    downloadMovies(con)