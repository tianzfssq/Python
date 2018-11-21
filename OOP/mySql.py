import mysql.connector

# 打开数据库连接
conn = mysql.connector.connect(user='root', password='12345678', database='test', use_unicode=True)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

conn.commit()
cursor.close()