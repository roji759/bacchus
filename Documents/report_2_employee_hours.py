""" 
    Title: report_2_employee_hours.py
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 14 July 2021
    Description: Pulling table data from MySQL database bacchus, using INNER JOIN and concatanation to calculate each employees hour total for the last four quarters.
"""

""" import statements """
import mysql.connector as mysql
from mysql.connector import errorcode


""" database config object """
db = mysql.connect(
    user = "bacchus_user",
    password = "MySQL8IsGreat!",
    host = "127.0.0.1",
    database = "bacchus",
)


mycursor = db.cursor()

#Creating empty list variable for later use
employee_yearly = []

#Creating function that will be called to print the employees hour totals
def employee_yearly_hours_report():


    #X integer will allow for iteration through employees
    x = 0
    #Y will select the employees hours worked in the initial list and then iterate to grab multiple entries
    y = 1
    #Selecting all of the employee Ids to see how many employees there are
    mycursor.execute("SELECT employee_id FROM employees")
    length_determine = mycursor.fetchall()
    #Integer variable containing the number of employees
    num_of_employees = int(len(length_determine))

    #While statement that continues based on the number of employees found in the previous query
    while x < num_of_employees:
    
        #Used an INNER JOIN to grab the needed columns of one employee per iteration of the while loop, with the y variable allowing for iteration through the employees
        mycursor.execute("SELECT first_name, last_name, department, hours_worked FROM employees e INNER JOIN hours_worked w ON w.employee_id = e.employee_id WHERE e.employee_id ="+str(y))
        employee_info = mycursor.fetchall()
        #Appending each employees first name, last name, department and the sum of their previous four quartes worth of hours
        employee_yearly.append([employee_info[0][0],employee_info[0][1],employee_info[0][2],employee_info[0][3]+employee_info[1][3]+employee_info[2][3]+employee_info[3][3]])
        x = x + 1
        y = y + 1

    print("\n -- DISPLAYING EMPLOYEE HOURS FOR THE LAST FOUR QUARTERS--")
    #For loop to iterate through the appended list printing the employee total hour data in a nice format
    for employee in employee_yearly:
        print(" First Name:  {}\n Last Name:   {}\n Department:  {}\n Total Hours: {}\n ".format(employee[0], employee[1],employee[2], employee[3]))



#Calling the function
employee_yearly_hours_report()


'''
References:
E. (2020, November 25). How to Find the Length of List in Python? Edureka. https://www.edureka.co/blog/python-list-length/
Python - Add List Items. (n.d.). W3schools.Com. Retrieved July 15, 2021, from https://www.w3schools.com/python/python_lists_add.asp
SQL INNER JOIN: The Beginner’s Guide to Inner Join in SQL. (2020, April 4). SQL Tutorial. https://www.sqltutorial.org/sql-inner-join/
'''