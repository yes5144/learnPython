import time
import xlwings as xw

data = {
    'firstRecharge': [{
        '3_18': 2004302.0
    }, {
        '4_18': 1000207.0
    }, {
        '5_18': 2002404.0
    }, {
        '10_18': 2004406.0
    }],
    'bigGift': [{
        '3_10': 20.0
    }, {
        '4_10': 30.0
    }, {
        '5_10': 40.0
    }, {
        '6_10': 50.0
    }, {
        '7_10': 60.0
    }, {
        '8_10': 70.0
    }, {
        '9_10': 80.0
    }, {
        '10_10': 100.0
    }],
    'payBigGift': [{
        '3_10': 'jingyugushan'
    }, {
        '4_10': 'baguaqiankundao'
    }, {
        '10_10': 'jingyugushan'
    }]
}
# app = xw.App(visible=True, add_book=False)
# # 文件位置：filepath，新建test文档，然后保存，关闭，结束程序
# filepath = r'xlwings_test.xlsx'
# wb = app.books.add()
# wb.sheets['paybiggift'].range('A1').value = 'hello xlwings'
# wb.save(filepath)
# time.sleep(8)
# wb.close()
# app.quit()

# 作者：早起收果子
# 链接：https://www.jianshu.com/p/e21894fc5501
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# app = xw.App(visible=True, add_book=True)
# app.display_alerts = False
# app.screen_updating = False
# 对于单元格也可以用表示行列的tuple进行引用
# A1单元格的引用
# xw.Range(1, 1)
# A1:C3单元格的引用
# xw.Range((1, 1), (3, 3))

# sht=xw.books['名字'].sheets['名字']
# 在第i+1行，第j+1列的单元格
# B1单元格
# rng=sht[0,1]


def rewrite_excel(data):
    app = xw.App(visible=True, add_book=True)
    filepath = r'h:\\xlwings_test2.xlsx'
    wb = app.books.open(filepath)
    for k, v in data.items():
        sht = wb.sheets[k]
        for m in v:
            for o, p in m.items():
                o2 = o.split('_')
                x = int(o2[0])
                y = int(o2[1])
                sht[x, y].value = p
                sht[x, y].color = (205, 67, 67)
    time.sleep(4)
    wb.save()
    wb.close()
    app.quit()


rewrite_excel(data)
