#!/usr/bin/env python
# coding: utf8
#

# http://www.linuxyw.com/790.html
# https://www.cnblogs.com/ghj1976/p/5293250.html
# https://elasticsearch-py.readthedocs.io/en/master/
#
"""
__author__ = '戴儒锋'
使用elasticsearch模块获取昨天某站点访问日志的所有数据
elasticsearch模块中指定使用scroll用来避免深度分页查找数据时的性能消耗
scan（扫描）搜索类型是和scroll（滚屏）API一起使用来从Elasticsearch里高效地取回巨大数量的结果而不需要付出深分页的代价。
size被应用到每一个分片上，所以我们在每个批次里最多或获得size * number_of_primary_shards（size*主分片数）
scroll= "1m" 指定快照时间为1分钟
"""
import datetime
from elasticsearch import Elasticsearch
# 格式为：2016.7.19 的昨日日期
yesterday = (datetime.datetime.now() +
             datetime.timedelta(days=-1)).strftime("%Y.%m.%d")
# 格式为：2016-7-19 的昨日日期
filter_yesterday = (datetime.datetime.now() +
                    datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
# 格式为：2016.7.18 的前天日期
before_yesterday = (datetime.datetime.now() +
                    datetime.timedelta(days=-2)).strftime("%Y.%m.%d")
# 请求elasticsearch节点的url
url = "http://192.168.1.41:9200/"
# 使用的索引，因日期时区问题，所以要指定昨天和前天的索引名
index_name = "logstash-apache-www.linuxyw.com-{date},logstash-apache-www.linuxyw.com-{b_date}".format(
    date=yesterday, b_date=before_yesterday)
# 实例化Elasticsearch类，并设置超时间为120秒，默认是10秒的，如果数据量很大，时间设置更长一些
es = Elasticsearch(url, timeout=120)
# DSL查询语法，在下面es.search使用
data = {
    "size": 3,  #指定每个分片最大返回的数据量，可根据日志量进行设置
    "query": {
        "bool": {
            # 指定要匹配的字符，这里是查找所有数据
            "must": {
                "match_all": {}
            },
            # 过滤，指定时间范围，这里设置成昨天0点到24点，代码上||-8h，因为ELK用的是UTC时间，跟北京时间误差8小时，所以要减8小时，这就是日志里的北京时间了
            "filter": {
                "range": {
                    "@timestamp": {
                        "gt":
                        "{date}T00:00:00||-8h".format(date=filter_yesterday),
                        "lt":
                        "{date}T23:59:59||-8h".format(date=filter_yesterday),
                    }
                }
            }
        }
    },
    "aggs": {
        "log_filename": {
            "terms": {
                "field": "log_source.keyword",
                "size": 20
            }
        }
    }
}
# 设置要过滤返回的字段值，要什么字段，就在这里添加，这样可以节约返回的数据量（带宽，内存等）
return_fields = [
    '_scroll_id',
    'hits.hits._source.timestamp',
    'hits.hits._source.@timestamp',
    'hits.hits._source.clientip',
    'hits.hits._source.request',
]


def main():
    # 指定search_type="scan"模式，并返回_scroll_id给es.scroll获取数据使用
    res = es.search(index=index_name,
                    body=data,
                    search_type="scan",
                    scroll="1m")
    scrollId = res["_scroll_id"]  # 获取scrollID
    # for vv in res['aggregations']['app_log_filename']['buckets']:
    #     print vv.values()

    response = es.scroll(
        scroll_id=scrollId,
        scroll="1m",
        filter_path=return_fields,
    )
    print len(response['hits']['hits'])  # 打印获取到的日志数量
    # for hit in response['hits']['hits']:
    #     print hit['_source']


if __name__ == "__main__":
    main()