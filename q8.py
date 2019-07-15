import pymysql
from config import Config

host = "shriram-rds-db.csaruqlxxway.us-east-1.rds.amazonaws.com"
port = 3306
dbname = Config.db
username = Config.un
password = Config.pw

conn = pymysql.connect(host, user=username,port=port,
                           passwd=password, db=dbname)

print(conn)