# 作者：Sceva
# 日期：2021/8/13 23:25
# 工具：PyCharm
# Python版本：3.6.3
import xlrd
import xlwt
from xlutils.filter import process, XLRDReader, XLWTWriter

import os

# 读取指定文件，将文件存储为模板
def read_exceal(file):
    formdate=[]

    #表操作
    read  = xlrd.open_workbook(file)
    table = read.sheets()[0]
    r = table.nrows
    c = table.ncols
    for i in range(r):
        temp = []
        for j in range(c):
            # formdate.append(table.cell_value(i,j))
            temp.append(table.cell_value(i,j))
        formdate.append(temp)
    return formdate
# 创建模板文件，将数据写入
def write_exceal(mode,value,outfile):
    # value =[(1.0, '', '', '', ''), (2.0, 3.0, '', '', 5.0), ('', '', '', '', ''), ('', 4.0, '', 6.0, '') ,('', '', '', '', ''),( '', '', '', '', ''), ('', '', '', '', ''), (1.0, '', '', '', '')]

    rb = xlrd.open_workbook(mode, formatting_info=True)

    # 参考xlutils.copy库内的用法 参考xlutils.filter内的参数定义style_list

    w = XLWTWriter()


    process(XLRDReader(rb, 'unknown.xls'), w)

    wb = w.output[0][1]

    style_list = w.style_list

    #n表id   sheet 表内容
    for n, sheet in enumerate(rb.sheets()):
        sheet2 = wb.get_sheet(n)
        for r in range(sheet.nrows):

            for c, cell in enumerate(sheet.row_values(r)):

                style = style_list[sheet.cell_xf_index(r, c)]

                sheet2.write(r, c, value[r][c], style)

    wb.save(outfile)

mode_file = "big.xls"

a = read_exceal(mode_file)
print(a)
write_exceal(mode_file,a,"bbb.xls")

