'''
This is the first file created in order to create the database and the required tables in the project
'''


import mysql.connector as c
def create_database():
    db = c.connect(host='localhost', user='root', passwd='2580')
    cur = db.cursor()
    sql = 'create database my_library;'
    cur.execute(sql)
    db.commit()

create_database()

def create_table1():
    db=c.connect(host='localhost', user='root', passwd='2580',database='my_library')
    cur=db.cursor()
    sql='''create table books 
    ( ISBN int(15) NOT NULL , BOOK_NAME varchar(100) NOT Null, std varchar(10), Quantity integer(5) NOT NULL,
    CONSTRAINT books_pk PRIMARY KEY (ISBN)
    );
    '''
    cur.execute(sql)

create_table1()

# def create_table1():
#     db=c.connect(host='localhost', user='root', passwd='2580',database='my_library')
#     cur=db.cursor()
#     sql='''create table books
#     ( ISBN int(15) NOT NULL , BOOK_NAME varchar(100) NOT Null, std varchar(10), Quantity integer(5) NOT NULL,
#     CONSTRAINT books_pk PRIMARY KEY (ISBN)
#     );
#     '''
#     cur.execute(sql)


def create_table2():
    db=c.connect(host='localhost', user='root', passwd='2580',database='my_library')
    cur=db.cursor()
    sql='''create table issues( name varchar(50) ,phno integer(15) , isbn integer(15),quantity integer(5),date_of_issue date,time varchar(20))
    '''
    cur.execute(sql)
create_table2()

def create_table3():
    db=c.connect(host='localhost', user='root', passwd='2580',database='my_library')
    cur=db.cursor()
    sql='''create table return_book(name varchar(50) ,phno integer(15) , isbn integer(15),quantity integer(5),date_of_return date,time varchar(20))
    '''
    cur.execute(sql)
create_table3()




