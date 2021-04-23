import pymysql,yaml,os
#logging.config.fileConfig(os.path.join(os.path.dirname(__file__),'config','log.conf'))
#ydata = 'D:\肖畅工作\学习\接口测试\python接口自动化\sqlscript\config\connDB.yaml'

ydata = os.path.join(os.path.dirname(__file__),'config','connDB.yaml')
class DB(object):
    #初始化建立数据库连接
    def __init__(self,dbname):
        with open(ydata, 'r', encoding='utf-8') as file:
            data = yaml.load(file.read(), Loader=yaml.FullLoader)
            conn = data.get(dbname)
        self.conn = pymysql.connect(
            host = conn.get('host'),
            user = conn.get('user'),
            password =  conn.get('password'),
            database = conn.get('database'),
            charset='utf8'
        )
"""
if __name__ == '__main__':
    logging.info("日志·")
    conn = DB("Testdb_goods").conn
    #使用cursor()方法创造一个游标对象
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询
    t = cursor.execute("SELECT cloudSkuId,cspuId FROM db_goods.t_cloudsku;")
    x = cursor.fetchall()
    logging.info(type(x),x)
    cursor.close()
    conn.close()
"""
