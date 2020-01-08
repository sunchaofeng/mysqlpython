# -*-coding:utf-8 -*-
import MySQLdb
def cre_db(db_name):
        # 数据库连接
        con = MySQLdb.connect("127.0.0.1", user='root', passwd='83610361', charset='utf8')
        #创建游标
        c = con.cursor()
        #执行sql语句
        c.execute("show databases")
        #获取查询结果
        rows = c.fetchall()
        print(rows)
        for row in rows:
            tmp="%2s"%row
        #判断数据库是否存在
        if db_name==tmp:
            c.execute('drop database ' + db_name)
            c.execute('create database ' + db_name)
        else:
            c.execute('create database ' + db_name)
        con.commit()
        con.close()

