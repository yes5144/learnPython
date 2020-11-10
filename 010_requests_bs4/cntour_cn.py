import re
import requests
from bs4 import BeautifulSoup
## http://c.biancheng.net/view/2011.html

headers = {
    'Accept':
    '*/*',
    'Accept-Encoding':
    'gzip, deflate, sdch',
    'Accept-Language':
    'zh-CN,zh;q=0.8',
    'Host':
    'www.cntour.cn',
    'Proxy-Connection':
    'keep-alive',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

proxies = {}


def get_html(url):
    strhtml = requests.get(url, headers=headers, proxies=proxies)
    print(type(strhtml))
    # print(strhtml)
    return strhtml


def bs4_parse(html):
    soup = BeautifulSoup(html.text, 'lxml')
    data = soup.select(
        '#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
    # print(data)

    for item in data:
        result = {
            'title': item.get_text(),
            'link': item.get('href'),
            'ID': re.findall('\d+', item.get('href'))
        }
        print('-' * 60)
        print(result)


if __name__ == "__main__":
    url = 'http://www.cntour.cn'
    html = get_html(url)
    bs4_parse(html)