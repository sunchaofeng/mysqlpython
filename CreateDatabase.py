# -*-coding:utf-8 -*-
#判断是否存在该数据库，如果存在删除，不存在就生成一个新的数据库
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
                print("已存在该数据库")
                c.execute('drop database ' + db_name)
            else:
                pass
        c.execute('create database ' + db_name)
        con.commit()
        con.close()

