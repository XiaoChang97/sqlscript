import pymysql
from mysql import DB
import threading
from loguru import logger
class GetsqlData():
    # 实例化对象，连接数据库
    def __init__(self,sql,db):
        self.sql = sql
        self.db = db

    def get_goods(self):
        self.goodsconn = DB("Testdb_goods").conn
        # 获取游标对象
        cursor = self.goodsconn.cursor(pymysql.cursors.SSCursor)
        #cursor = self.goodsconn
        sql = 'SELECT cloudSkuId,cspuId FROM db_goods.t_cloudsku where status = 1;'
        #执行一个sql，executemany执行多个sql
        cursor.execute(sql)
        result = []
        while True:
            row = cursor.fetchone()
            result.append(row)
            if not row:
                result.pop()
                break
        cursor.close()
        self.goodsconn.close()
        # 获取结果集所有行
        return result


    def get_order(self):
        self.ordersconn = DB("Testdb_order").conn
        # 获取游标对象
        cursor = self.ordersconn.cursor(pymysql.cursors.SSCursor)
        sql = 'SELECT orderId,cskuId,cSpuId FROM db_order.t_order where status = 2;'
        # 执行一个sql，executemany执行多个sql
        cursor.execute(sql)
        result = []
        while True:
            row = cursor.fetchone()
            result.append(row)
            if not row:
                result.pop()
                break
        cursor.close()
        self.ordersconn.close()
        # 获取结果集所有行
        return result


    def SelectSql(self):
        self.conn = DB(self.db).conn
        '''
        获取流式游标对象，不会一次性缓存所有行，
        而是从储存块中读取记录，并且一条一条返回，不会出现接收数据时内存溢出而卡死的情况
        https://www.yuque.com/docs/share/2d47f800-c47c-45d5-8842-aad577e2573d?#
        '''
        cursor = self.conn.cursor(pymysql.cursors.SSCursor)
        sql = self.sql
        # 执行一个sql，executemany执行多个sql
        cursor.execute(sql)
        result = []
        #
        while True:
            row = cursor.fetchone()
            result.append(row)
            if not row:
                result.pop()
                break
        cursor.close()
        self.conn.close()
        # 获取结果集所有行
        return result
'''
if __name__ == '__main__':
    Testdb_order = "Testdb_order"
    Testdb_goods = "Testdb_goods"
    orderSql = "SELECT orderId,cskuId,cSpuId FROM db_order.t_order where status = 2;"
    goodsSql = "SELECT cloudSkuId,cspuId FROM db_goods.t_cloudsku where status = 1;"
    orderlist = GetsqlData(orderSql,Testdb_order).SelectSql()
'''
