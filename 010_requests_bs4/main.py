import urllib.request
from bs4 import BeautifulSoup

html = """
"""


def bs4_paraser(html):
    all_value = []
    value = {}
    soup = BeautifulSoup(html, 'html.parser')
    # 获取影评的部分
    # main_div = soup.find_all('div',attrs={'class':'main'} limit=1)
    main_div = soup.find_all('ul', attrs={'class': 'list-ad-items'}, limit=1)
    for row in main_div:
        # 获取每一个影评，即影评的item
        all_div_item = row.find_all('li', attrs={'data-service': 'vip'})
        print(len(all_div_item))

        for r in all_div_item:
            print(r)
            memo = r.a.img['alt']
            print(memo)
            company = r.div.div.a.string
            print(company)
            tel = r.div.div.span.button['data-contact']
            print(tel)
            break
        #     # 获取影评的标题部分
        #     title = r.find_all('div',
        #                        attrs={'class': 'g-clear title-wrap'},
        #                        limit=1)
        #     if title is not None and len(title) > 0:
        #         value['title'] = title[0].a.string
        #         value['title_href'] = title[0].a['href']
        #         score_text = title[0].div.span.span['style']
        #         score_text = re.search(r'\d+', score_text).group()
        #         value['score'] = int(score_text) / 20
        #         # 时间
        #         value['time'] = title[0].div.find_all('span',
        #                                               attrs={'class':
        #                                                      'time'})[0].string
        #         # 多少人喜欢
        #         value['people'] = int(
        #             re.search(
        #                 r'\d+',
        #                 title[0].find_all('div',
        #                                   attrs={'class': 'num'
        #                                          })[0].span.string).group())
        #     # print r
        # all_value.append(value)
        # value = {}
    return all_value


#把传递解析函数，便于下面的修改
def get_html(url):
    headers = {
        'Accept':
        '*/*',
        'Accept-Encoding':
        'gzip, deflate, sdch',
        'Accept-Language':
        'zh-CN,zh;q=0.8',
        'Host':
        'www.360kan.com',
        'Proxy-Connection':
        'keep-alive',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    response.encoding = 'utf-8'
    print(request.get_method())

    # response.read()
    if response.code == 200:
        return 'ok'
    else:
        pass


if __name__ == "__main__":
    # value = get_html('http://www.360kan.com/m/haPkY0osd0r5UB.html')
    # for row in value:
    # print(row)
    bs4_paraser(html)
