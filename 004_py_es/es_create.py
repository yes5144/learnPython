#!/usr/bin/env python
# coding: utf8
#

from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='192.168.1.186', port=9200)

# es.get(ve)


## insertData
def insertData():
    es.create(index='my_index',
              doc_type='test_type',
              id=11,
              ignore=[400, 409],
              body={
                  "name": "python",
                  "addr": "河南省"
              })
    res = es.get(index='my_index', doc_type='test_type', id=11)
    print(res)
    es.search()
    es.scroll()


if __name__ == "__main__":
    insertData()
