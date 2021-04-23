from getsqldata.getsqldata import GetsqlData
from lib.writeexcel import WriteExcel
from loguru import logger
import os,threading
from lib.readexcel import ReadExcel
goodsSql = "SELECT cloudSkuId,cspuId FROM db_goods.t_cloudsku;"
orderSql = "SELECT orderId,cskuId,cSpuId FROM db_order.t_order;"
threadLock = threading.Lock()
class TestOrder(object):
    def __init__(self):
        '''
        #执行WriteExcel().write_data()方法导出查询的商品数据
        logger.info("开始查询并且导出t_cloudsku表中所有的数据>>>>>>>>>>>>>")
        WriteExcel().write_data()
        #从excel中读取商品数据
        goodsdata =  ReadExcel(goodsfile).read_data()
        '''
        #threading.Thread.__init__(self)
        # 从sql查询获取商品数据，返回list变量
        logger.info("*****************开始查询t_cloudsku表中所有的数据>>>>>>>>>>>>>")
        self.goodsdata = list(GetsqlData(goodsSql, 'Testdb_order').SelectSql())
        # 从sql查询获取订单数据,返回list变量
        logger.info("*****************开始查询t_order表中所有的数据>>>>>>>>>>>>>")
        self.orderdata = list(GetsqlData(orderSql, 'Testdb_order').SelectSql())
        logger.info("**************开始测试订单数据，t_order共{0}条订单，t_cloudsku共{1}条商品数据***********".format(len(self.orderdata),
                                                                                                  len(self.goodsdata)))
        #self.newgoodsdata = self.split_list(self.goodsdata,int(len(self.goodsdata)/2))
        self.neworderdata = self.split_list(self.orderdata,int(len(self.orderdata)/2))
        self.errorOrder = []
        self.missingskuid = []

    '''[123456]分割为-->[[123],[456]]'''
    def split_list(self, l: list = None, n: int = None, new_list: list = []):
        if len(l) <= n:
            new_list.append(l)
            return new_list
        else:
            new_list.append(l[:n])
            return self.split_list(l[n:], n)

    def test_cspuid(self,listdata):
        # 获取锁，用于线程同步
        #threadLock.acquire()
        for order in range(len(listdata)):
            logger.info("检测第{0}条订单".format(order+1))
            ordercskuid = int(listdata[order][1])
            ordercspuid = int(listdata[order][2])
            sign = True
            for goods in range(len(self.goodsdata)):
                goodscsksuid = int(self.goodsdata[goods][0])
                goodscspsuid = int(self.goodsdata[goods][1])
                if ordercskuid == goodscsksuid:
                    sign = False
                    if goodscspsuid != ordercspuid:
                        logger.error("订单{0}的cspuid不正确，ordercspuid:{1},goodscspuid:{2}".format(listdata[order][0],ordercspuid,goodscspsuid))
                        self.errorOrder.append(((listdata[order][0]),(ordercspuid),(goodscspsuid)))
                    else:
                        pass
                else:
                    pass
            if sign:
                logger.error("orderid：{0}的cskuid：{1}未在t_cloudsku中找到".format(listdata[order][0],ordercskuid))
                self.missingskuid.append(((listdata[order][0]), (ordercskuid)))
        # 释放锁，开启下一个线程
        #threadLock.release()


if __name__ == '__main__':
    listdata = [('20210211515454844','800','400'),('20210211515333333','500','700')]
    TestOrder().test_cspuid(listdata)