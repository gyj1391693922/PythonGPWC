import requests

def getAction():
    url = "http://192.168.23.44:8080/"
    response = requests.get(url = url)
    response.encoding = "utf-8"
    content = response.text
    print(content)


def resTest():
    url = "http://www.baidu.com"
    response = requests.get(url=url)
    response.encoding ="utf-8"
    print(response.text)
    print(response.encoding)
    print(response.url)
    print(response.content)
    print(response.status_code)
    print(response.headers)


if __name__ == '__main__':
    getAction()