# 作者：Sceva
# 日期：2021/8/14 21:16
# 工具：PyCharm
# Python版本：3.6.3



#读取exceal
def hh():
    formdate = []
    # 表操作
    read = xlrd.open_workbook(file)
    table = read.sheets()[0]
    # 行操作
    """
    nrows = table.nrows  #获取该sheet中的有效行数
    
    table.row(rowx)  #返回由该行中所有的单元格对象组成的列表
    
    table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表
    
    table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表
    
    table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
    
    table.row_len(rowx) #返回该列的有效单元格长度
    
    """
    # nrows = table.nrows
    #
    # print(nrows)
    #
    # print(table)
    # print(read)
    # 对列的操作
    """
    ncols = table.ncols   #获取列表的有效列数
    
    table.col(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
    
    table.col_slice(colx, start_rowx=0, end_rowx=None)  #返回由该列中所有的单元格对象组成的列表
    
    table.col_types(colx, start_rowx=0, end_rowx=None)    #返回由该列中所有单元格的数据类型组成的列表
    
    
    """

    # 对单元格的操作
    """
    table.cell(rowx,colx)   #返回单元格对象
    
    table.cell_type(rowx,colx)    #返回单元格中的数据类型
    
    table.cell_value(rowx,colx)   #返回单元格中的数据
    """