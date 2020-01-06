import csv
import MySQLdb
import sys
from datetime import datetime, date
input_file = "data/supplier_data.csv"
# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='jingyi', passwd='1252')
c = con.cursor()
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader)

#将csv数据写入数据库
for row in file_reader:
	data = []
	for column_index in range(len(header)):
		if column_index < 4:
			data.append(str(row[column_index]).lstrip('$')\
			.replace(',', '').strip())
		else:
			a_date = datetime.date(datetime.strptime(\
			str(row[column_index]), '%m/%d/%y'))
			# %Y: year is 2016; %y: year is 15
			a_date = a_date.strftime('%Y-%m-%d')
			data.append(a_date)
	print(data)
	c.execute("""INSERT INTO Suppliers VALUES (%s, %s, %s, %s, %s);""", data)
con.commit()
#查询表里面数据
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
	row_list_output = []
	for column_index in range(len(row)):
		row_list_output.append(str(row[column_index]))
	print(row_list_output)