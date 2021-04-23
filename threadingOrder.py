import datetime,time
import threading,os
from loguru import logger
from lib.writeexcel import WriteExcel
from test_order import TestOrder
file = os.path.dirname(__file__)
log_path = file + '/log/log.log'
class threadingOrder(object):
    def test(self):
        start = time.time()
        #新增日志文件，超过50兆就新增一个日志文件
        logger.add('log_path_{time}', encoding='utf-8',rotation="50 MB")
        testorder = TestOrder()
        neworderdata = testorder.neworderdata
        #neworderdata = [[('2015684165184984','9999999','1000'),('2015684165184988','9999999','2004')],[('2015684165187410','9999999','2006'),('2015684165188888','9999999','2008')]]
        createThreading = []
        for list in neworderdata:
            logger.info("*****************开始创建子线程*****************")
            #T = TestOrder()
            #target为要创建线程的目标方法
            T = threading.Thread(target=testorder.test_cspuid,args=(list,))
            logger.info("*****************子线程{0}创建成功*****************".format(T.getName()))
            createThreading.append(T)
        for l in createThreading:
            l.start()
            logger.info("*****************成功启动子线程{0}*****************".format(l.getName()))
        for l in createThreading:
            l.join()
            logger.info("*****************成功结束子线程{0}*****************".format(l.getName()))

        logger.info("订单检测完毕，将所有错误订单和缺失的商品数据分别导出excel")
        WriteExcel().errorOrder_data(testorder.errorOrder)
        WriteExcel().missingCskuid_data(testorder.missingskuid)
        endtime = time.time()
        logger.info("脚本运行时间为{0}s".format((endtime - start)))
if __name__ == '__main__':
    threadingOrder().test()