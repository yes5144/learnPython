import os
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
    house = doc('.resblock-list-wrapper li').items()
    for i in house:
        house_data = {
            '小区': i.find('.name').text(),
            '链接': i.find('.resblock-img-wrapper').attr('href')
        }
        print(house_data)
        ## 插入数据库 or csv


if __name__ == "__main__":
    # url = "http://cn.bing.com"
    url = "https://sz.fang.lianjia.com/loupan/bba0eba300/"
    shtml = get_html(url)
    get_info(shtml)
