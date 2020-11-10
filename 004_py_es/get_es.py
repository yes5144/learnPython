#!/usr/bin/env python
#

import requests

DATA = """{
  "size": 0,
  "_source": {
    "excludes": []
  },
  "aggs": {
    "2": {
      "terms": {
        "field": "key2",
        "size": 1000000,
        "order": {
          "_count": "desc"
        }
      }
    }
  },
  "stored_fields": [
    "*"
  ],
  "script_fields": {},
  "docvalue_fields": [
    "notafter",
    "notbefore"
  ],
  "query": {
    "bool": {
      "must": [
        {
          "exists": {
            "field": "hosts"
          }
        },
        {
          "match_phrase": {
             #这里是要查询的字段
          }
        }
      ],
      "filter": [
        {
          "match_all": {}
        }
      ],
      "should": [],
      #这里可以添加一些否定的筛选条件，例如下面的例子就是让father字段不能为Root的条件
      "must_not": [
        {
          "match_phrase": {
            "father": {
              "query": "Root"
            }
          }
        }
      ]
    }
  }
}"""

requests.request("GET",
                 "http://:8200/" + index + "/_search",
                 data=json.dumps(eval(DATA)).replace("key1", key1).replace(
                     "key2", key2),
                 headers={'content-type': 'application/json'})
