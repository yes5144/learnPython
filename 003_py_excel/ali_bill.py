#!/usr/bin/env python
# coding: utf8

import json

items = json.load(open("zzz_test_data/ali_bill.json", 'r',
                       encoding='utf-8'))["Data"]["Items"]["Item"]
for i in items:
    if i["PretaxAmount"] > 0:
        print(i["ProductName"], "\t", i["PretaxAmount"])
