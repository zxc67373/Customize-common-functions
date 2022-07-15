# 常用功能
import xlrd
# import xlwt


# 打开实验数据表格
def excel_open(path):
    book = xlrd.open_workbook(path)
    # 选择页数为第1页
    sheet1 = book.sheets()[0]

    # 获取表中第1列的数据
    y_noone = sheet1.col_values(1)[1:]
    # print('第2列且不要第一个值： ', y_noone)
    return y_noone


from xlutils.copy import copy


def excel_insert(path, sheet_name, rows, cols, value):
    book = xlrd.open_workbook(path)
    # 选择页数为第1页
    # sheet1 = book.sheets()[0]
    xls_copy = copy(book)
    sheet1 = xls_copy.get_sheet(sheet_name)
    sheet1.write(rows, cols, value)
    xls_copy.save(path)


# print(excel_process('转译与ocr抽取结果.xls'))
# print(excel_insert('转译与ocr抽取结果.xls','转译与ocr抽取结果',1,5,123))
