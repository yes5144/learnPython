import os
import xlrd
import xlwt
from xlutils.copy import copy
import time

data = {
    'firstRecharge': [{
        '4_18': 1000207.0
    }, {
        '5_18': 2002404.0
    }, {
        '10_18': 2004406.0
    }],
    'bigGift': [{
        '4_10': 30.0
    }, {
        '9_10': 80.0
    }, {
        '10_10': 100.0
    }],
    'payBigGift': [{
        '6_10': 'jinsijia'
    }, {
        '7_10': 'xisuijing'
    }, {
        '8_10': 'zijinhuluxiang'
    }, {
        '9_10': 'chiriyanyandao'
    }, {
        '10_10': 'jingyugushan'
    }]
}

for k, v in data.items():
    print(k, v)
    for m in v:
        print(m, type(m))
        for n, o in m.items():
            print(n, o)
            print(n.split("_"))

        break


def rewrite_excel(k, v):
    if len(v) > 0:
        ExcelFile = xlrd.open_workbook("activityNew.xlsx")
        rs = ExcelFile.sheet_by_name(k)
        wb = copy(ExcelFile)
        ws = wb.get_sheet(k)
        ## 40
        font = xlwt.Font()
        font.colour_index = 40
        style0 = xlwt.XFStyle()
        style0.font = font

        for m in v:
            print(type(m), m)
            for o, q in m.items():
                m2 = o.split("_")
                print('m222', m2)
                x = int(m2[0])
                y = int(m2[1])
                ws.write(x, y, q, style0)
        wb.save("activityNew.xlsx")


for k, v in data.items():
    rewrite_excel(k, v)
