import os
import re
import time
from selenium import webdriver
# https://blog.csdn.net/weixin_42946604/article/details/86618237


def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    ### get html code
    # links = driver.find_elements_by_xpath('//*[@id="b_results"]/li')
    # links = driver.find_elements_by_tag_name('h2')
    # print(links)
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    # html = driver.page_source
    driver.quit()

    return html


from pyquery import PyQuery as pq


def get_info(html):
    doc = pq(html)
    ## Copy selector: body > div.resblock-list-container.clearfix > ul.resblock-list-wrapper
    mvs = doc('.grid_view li').items()
    for i in mvs:
        house_data = {
            'mv_name': re.sub('\s', ' ',
                              i.find('.title').text()),
            'mv_url': i.find('.hd a').attr('href')
        }
        print(house_data)
        ## 插入数据库 or csv


if __name__ == "__main__":
    url = "https://movie.douban.com/top250"
    shtml = get_html(url)
    get_info(shtml)
