import MySQLdb
import sys
import pandas as pd
#查询perhourdata数据库里面数据
con = MySQLdb.connect(host='127.0.0.1',
					  port=3306,
					  db='perhourdata',
					  user='root',
					  passwd='83610361',
					  charset='utf8'  # 编码方式
					  )
c = con.cursor()
c.execute("SELECT * FROM hour_data00to08 where 区站号='58724'")
#c.execute("select * from hour_data09to18 where 区站号='F3101'")
rows = c.fetchall()
col = c.description
colname=[]
#通过for循环将列标题赋值给colname列表
for i in range(len(col)):
	colname.append(col[i][0])
test=pd.DataFrame(columns=colname,data=rows)
test.to_csv('data/58724.csv',index=False)
