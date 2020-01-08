import csv
import MySQLdb
from datetime import datetime, date
input_file = "data/supplier_data.csv"
# Connect to a MySQL database
con = MySQLdb.connect(host='127.0.0.1',
					  port=3306,
					  db='my_suppliers',
					  user='root',
					  passwd='83610361',
					  charset='utf8' #编码方式
					 )
c = con.cursor()
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)

#将csv数据写入数据库,写入之前要先建立数据库my_suppliers和表Suppliers以及列名和类型
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		if column_index < 4:
			data.append(str(row[column_index]).lstrip('$').replace(',', '').strip())
		else:
			a_date = datetime.date(datetime.strptime(str(row[column_index]), '%m/%d/%y'))
			# %Y: year is 2016; %y: year is 15
			a_date = a_date.strftime('%Y-%m-%d')
			data.append(a_date)
	print(data)
	c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
con.commit() #执行以上操作
#查询表里面数据
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
	row_list_output = []
	for column_index in range(len(row)):
		row_list_output.append(str(row[column_index]))
	print(row_list_output)
#最后应该关闭所有的游标和连接
c.close()
con.close()