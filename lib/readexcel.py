#!/usr/bin/env python
# _*_ coding:utf-8 _*_


__author__ = 'xiaochang'

import xlrd,os
from loguru import logger
'''
xlrd是下载的第三方库，用来读取excel表格的一个库
'''
class ReadExcel():
    """读取excel文件数据"""
    def __init__(self,fileName,SheetName="Sheet"):
        #open_workbook方法是打开电子表格读取数据
        self.data = xlrd.open_workbook(fileName)
        self.table = self.data.sheet_by_name(SheetName)
        # 获取总行数、总列数
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols
    #将所有表格中的内容都存放之list中然后return
    def read_data(self):
        if self.nrows > 1:
            # 获取第一行的内容，列表格式,首行标题固定keys，所有的key都一样
            keys = self.table.row_values(0)
            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, self.nrows):
                values = self.table.row_values(col)
                # keys，values组合转换为字典
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)
            return listApiData
        else:
            logger.error("表格是空数据!")
            return None

        # 根据caseID查找表格用例数据
    def read_oneData(self):
        if self.nrows > 1:
            # 获取第一行的内容，列表格式,首行标题固定keys，所有的key都一样
            keys = self.table.row_values(0)
            # 获取每一行的内容，列表格式
            for col in range(1, self.nrows):
                if self.table.row_values(col)[1] == self.case_id:
                    values = self.table.row_values(col)
                    # keys，values组合转换为字典
                    return  dict(zip(keys, values))
                    break

        else:
            logging.error("表格是空数据!")
            return None
'''
if __name__ == '__main__':
    file = os.path.dirname(__file__)
    p = os.path.dirname(file) + '/report/CskuidAndCspuid.xlsx'
    listData = ReadExcel(p).read_data()
    logger.debug(listData)
'''

