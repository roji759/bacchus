import os
import mysql.connector as mysql

""" 
    Title: bacchus_populate.py
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 11 July 2021
    Description: Creating and structuring bacchus database.
"""

""" import statements """

""" database config object """


# Creating a Function to create the database
def database_create():
    db = mysql.connect(
        user="bacchus_user",
        password="MySQL8IsGreat!",
        host="127.0.0.1",
    )

    mycursor = db.cursor()

    mycursor.execute("CREATE DATABASE bacchus")
    mycursor.close()


""" database config object """


# Creating a Function read a .sql file that establishes the empty tables for the database
def database_structure():
    db = mysql.connect(
        user="bacchus_user",
        password="MySQL8IsGreat!",
        host="127.0.0.1",
        database="bacchus",
    )

    mycursor = db.cursor()

    with open(os.path.dirname(__file__) + '/../dbscripts/bacchus_table_create.sql') as f:
        mycursor.execute(f.read(), multi=True)


database_create()
database_structure()


"""
Resources:
execute *.sql file with python MySQLdb. (2010, December 10). Stack Overflow. https://stackoverflow.com/questions/4408714/execute-sql-file-with-python-mysqldb
Getting Started with MySQL in Python. (2019, December 9). Datacamp.Com. https://www.datacamp.com/community/tutorials/mysql-python
MySQL Commands out of sync Python. (2019, January 1). Stack Overflow. https://stackoverflow.com/questions/53994303/mysql-commands-out-of-sync-python
Python MySQL Create Table. (n.d.). W3schools.Com. Retrieved July 11, 2021, from https://www.w3schools.com/python/python_mysql_create_table.asp
"""