# 作者：Sceva
# 日期：2021/8/13 23:25
# 工具：PyCharm
# Python版本：3.6.3
import xlrd
import xlwt
import openpyxl
import xlutils


# 读取指定文件，将数据写入

# 创建模板文件，将数据写入
class ReadExcel():  # 读取excel数据的类
    def __init__(self, file_name, sheet_name):
        self.file = openpyxl.load_workbook(file_name)
        self.sheet = self.file[sheet_name]
        print(self.file)
        print(self.sheet)


if __name__ == '__main__':
    a = ReadExcel("cases.xlsx", "sheet1")
