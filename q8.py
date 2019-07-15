#     Create an RDS MySQL instance and connect to it from an EC2 instance. Perform crud operations using python.

# Deliverable: Python Script

# pymysql for db connection
import pymysql
#IMporting credentials from config file
from config import Config
import logging

#Initialize the logger
logging.basicConfig(filename="q8.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
#Creating an object 
logger=logging.getLogger() 
#set logger to debug
logger.setLevel(logging.DEBUG) 

host = "shriram-rds-db.csaruqlxxway.us-east-1.rds.amazonaws.com"
port = 3306
dbname = Config.db
username = Config.un
password = Config.pw

#Establish the connection
logger.info("Connecting")
conn = pymysql.connect(host, user=username,port=port,
                           passwd=password, db=dbname)

#Queries for each of the CURD operations
create = "CREATE TABLE student(sid int, sname varchar(30))"
insert = "INSERT INTO student(sid, sname) VALUES (1, 's1'),(2,'s2'),(3,'s3'),(4,'s4')"
read = "SELECT * FROM student"
update = "UPDATE student SET sname = 'student2' WHERE sid = 2"
delete = "DELETE FROM student WHERE sid = 2"


try:
	#Execute Create table
	logger.info("creating table")
    cur = conn.cursor()
    cur.execute(create)
    show = "show tables"
    cur.execute(show)
    logger.info("display data")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Execute insert and display
    logger.info("inserting records")    
    cur.execute(insert)
    cur.execute(read)
    logger.info("display data")
    rows = cur.fetchall()
    for row in rows:
        print(row)
   
   # EXcute update and display
    logger.info("updating data")
    cur.execute(update)
    cur.execute(read)
    logger.info("display data")
    rows = cur.fetchall()
    for row in rows:
        print(row)
   #execute delete and display
    logger.info("delete data")
    cur.execute(delete)
    cur.execute(read)
    logger.info("display data")
    rows = cur.fetchall()
    for row in rows:
        print(row)
   
   # commit the operations
   	logger.info("commit data")
    conn.commit()
except Exception as e:
    print(e)
finally:
    conn.close()