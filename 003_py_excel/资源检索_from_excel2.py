import os
import sys
import time
import xlrd
import xlwt
# import patterns as patterns
from xlutils.copy import copy
import xlwings as xw

today = time.strftime("%Y-%m-%d")
print(today)


##  读取excel并获取指定sheet中需要检索的单元格坐标和内容
def read_excel(checkSheets):
    ExcelFile = xlrd.open_workbook("activityNew.xlsx")
    print("此excel所有的sheet的名字：", ExcelFile.sheet_names())
    print()
    res = {}
    for chSheet in checkSheets.keys():
        sheet = ExcelFile.sheet_by_name(chSheet)
        ## 此sheet最大行数
        # maxrows = sheet.nrows
        print(chSheet + "此sheet的行数：", sheet.nrows, chSheet + "此sheet的列数：",
              sheet.ncols)
        ## 获取第11列，2-22行的数据
        # checkFileNamePrefix = sheet.col_values(10, 2, 22)
        temp = []
        if chSheet == 'firstRecharge':
            ## firstRecharge-sheet 的数据在19列
            for n in range(3, 11):
                targetValue = sheet.cell(n, 18).value
                temp.append({str(n) + '_18': targetValue})
            # checkFileNamePrefix = sheet.col_values(18, 2, 22)
        else:
            ## 其他2个均为第11列的数据
            for n in range(3, 11):
                targetValue = sheet.cell(n, 10).value
                temp.append({str(n) + '_10': targetValue})
        res[chSheet] = temp
        print(temp)
        print()
        print()
        # print(checkFileNamePrefix)
    print('需要被检索的sheet和文件名：', res)
    print()
    return res


## 重新写入excel并设置指定颜色
def rewrite_excel_2(data):
    ## 参数formatting_info=True，清除excel原来的样式
    ExcelFile = xlrd.open_workbook("activityNew.xlsx")
    nostyle = xlwt.XFStyle()
    w_style = copy(ExcelFile)
    w_style.save("activityNew.xlsx")

    ## 设置新样式
    style = "font:colour_index yellow;"
    style = "pattern: pattern solid, fore_colour ice_blue; font: bold on"
    style1 = xlwt.easyxf(style)
    for k, v in data.items():
        if len(v) > 0:
            ## 参数formatting_info=True，保留excel原来的样式
            ExcelFile = xlrd.open_workbook("activityNew.xlsx",
                                           formatting_info=True)
            rs = ExcelFile.sheet_by_name(k)
            ## xlutils.copy
            wb = copy(ExcelFile)
            ws = wb.get_sheet(k)

            for m in v:
                for o, q in m.items():
                    m2 = o.split("_")
                    ## 行坐标
                    x = int(m2[0])
                    ## 列坐标
                    y = int(m2[1])
                    ws.write(x, y, q, style1)
            wb.save("activityNew.xlsx")
            print('activityNew.xlsx - %s Rewrite ok' % k)


def rewrite_excel(data):
    app = xw.App(visible=True, add_book=True)
    filepath = r'activityNew.xlsx'
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
        print('activityNew.xlsx - %s Rewrite ok' % k)
    time.sleep(4)
    wb.save()
    wb.close()
    app.quit()


def search(search_path, filename):
    tmpfile = []
    for root, dirs, files in os.walk(search_path):
        # print("检索所在的目录：", root)
        # print("检索目录的文件夹：", dirs)
        # print("检索目录的原文件名：", files)
        # print("当前检索目录的文件去后缀后：", [x.split(".")[0] for x in files])
        tmpfile += files
    # print(sheetname + '目录下所有的文件名：', tmpfile)
    # print()
    # print()
    if filename in [x.split(".")[0] for x in tmpfile]:
        return True
    else:
        return False


## 检索开始 ##
def check_begin(abs_path, checkSheets, sheetFilesnames):
    file_not_exist = {}
    for sheetname in sheetFilesnames.keys():
        tmp = []
        search_path = abs_path + checkSheets[sheetname]
        for x in sheetFilesnames[sheetname]:
            # print(type(x), x)
            for _, n in x.items():
                # print(type(n), n)
                ## excel 默认数字为浮点型
                i = str(n).split(".")[0]
                # print("str(n).split("."):", i, type(i), len(i))
                isfile = search(search_path, i)
                if not isfile:
                    tmp.append(x)
                    print("检索-%s-结果不存在：%s" % (sheetname, x))
                file_not_exist[sheetname] = tmp
    print('此次检索后不存在的文件名：', file_not_exist)
    print()
    return file_not_exist


def write2txt_and_excel(file_not_exist):
    print('---------------- 正在写入TXT文件 ----------------')
    ## 文件名
    filename = "%s_%s.txt" % ("检索资源不存在", today)
    print("更多详情请查看", filename)
    with open(filename, "w") as f:
        temp = []
        for k in file_not_exist.keys():
            temp.append(k)
            for v in file_not_exist[k]:
                temp.append(str(v))
        f.write(("\n").join(temp))
    print('---------------- 写入TXT文件完成 ----------------')
    print()
    print('---------------- 正在修改excel文件 ----------------')
    rewrite_excel(file_not_exist)
    print('---------------- 修改excel文件完成 ----------------')


def main():
    ## 被检索excel中的sheet({'sheet工作簿':'目录名'})，清修改
    checkSheets = {
        'firstRecharge': 'firstRecharge',
        'bigGift': 'bigGift',
        'payBigGift': 'payBigGift',
    }

    ## 被检索文件所在目录（测试用）
    abs_Path = 'H:\\temp\\laya\\'
    print('执行脚本的参数详情：', sys.argv)
    print()
    # if len(sys.argv) > 1:
    #     abs_Path = sys.argv[1]
    # else:
    #     print('请传入检索的绝对路径：', sys.argv[0], '路径')
    #     return

    sheetFilesnames = read_excel(checkSheets)
    file_not_exist = check_begin(abs_Path, checkSheets, sheetFilesnames)
    ## 判断列表是否为空，不为空则写入文件
    if file_not_exist:
        write2txt_and_excel(file_not_exist)
    else:
        print('所有被检索的文件均已存在！')
        print("\033[5;37;41m骚年666\033[0m")


if __name__ == '__main__':
    main()