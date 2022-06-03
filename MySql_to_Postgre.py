##pip3 install mysqlclient
##pip3 install psycopg2
import MySQLdb
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="book_application") # name of the data base
					  
import psycopg2
import psycopg2.extras

encoding = 'Latin1'

dbx=db.cursor()
#DB=psycopg2.connect("dbname='mysql'")
DB=psycopg2.connect(host = 'localhost',dbname = 'book_application',user = 'postgres',password = 'pass',port = 5432)
DC=DB.cursor()
DC.execute("set client_encoding = " + encoding)


mysql='''show tables from book_application'''
dbx.execute(mysql); ts=dbx.fetchall(); tables=[]
for table in ts: tables.append(table[0])
for table in tables:
    mysql='''describe book_application.%s'''%(table)
    dbx.execute(mysql); rows=dbx.fetchall()
    psql='drop table %s'%(table)
    DC.execute(psql) 
    DB.commit()

    psql='create table %s ('%(table)
    for row in rows:
        name=row[0]; type=row[1]
        if 'int' in type: type='int8'
        if 'blob' in type: type='bytea'
        if 'datetime' in type: type='timestamptz'
        psql+='%s %s,'%(name,type)
    psql=psql.strip(',')+')'
    print(psql)
    try: DC.execute(psql); DB.commit()
    except: pass

    msql='''select * from book_application.%s'''%(table)
    dbx.execute(msql); rows=dbx.fetchall()
    n=len(rows); print("Record no-",n); t=n
    if n==0: continue #skip if no data

    cols=len(rows[0])
    for row in rows:
        ps=', '.join(['%s']*cols)
        psql='''insert into %s values(%s)'''%(table, ps)
        DC.execute(psql,(row))
        n=n-1
        if n%1000==1: DB.commit(); 
    DB.commit()