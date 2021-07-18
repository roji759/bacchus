""" import statements """
import mysql.connector as mysql

"""    
    Title: bacchus_populate.py
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 11 July 2021
    Description: Populating and printing tables from MySQL database bacchus.
"""

""" database config object """

db = mysql.connect(
    user="bacchus_user",
    password="MySQL8IsGreat!",
    host="127.0.0.1",
    database="bacchus",
)

mycursor = db.cursor()

'''Creating functions to populate specific tables'''


# Creating a Function to populate table rows
def distributors():
    sql = "INSERT INTO distributors (distributors_name) VALUES (%s)"
    val = [
        ('Kroger',),
        ('Walmart',),
        ('Amazon',),
        ('King Super',),
        ('IGA',),
        ('Wine World',),
    ]
    mycursor.executemany(sql, val)
    # Committing the changes to the table
    db.commit()


# Creating a Function to populate table rows
def product():
    sql = "INSERT INTO product (product_name, quantity) VALUES (%s,%s)"
    val = [
        ('Merlot', 100),
        ('Cabernet', 100),
        ('Chablis', 100),
        ('Chardonnay', 100),
    ]
    mycursor.executemany(sql, val)
    # Committing the changes to the table
    db.commit()


# Creating a Function to populate table rows
def supplies():
    sql = "INSERT INTO supplies (supply_name, quantity) VALUES (%s,%s)"
    val = [
        ('Bottles', 50),
        ('Corks', 50),
        ('Labels', 50),
        ('Boxes', 50),
        ('Vats', 50),
        ('Tubing', 50),
    ]
    mycursor.executemany(sql, val)
    # Commiting the changes to the table
    db.commit()


# Creating a Function to populate table rows
def suppliers():
    sql = "INSERT INTO suppliers (suppliers_name) VALUES (%s)"
    val = [
        ('Bottles & Things',),
        ('Box Central',),
        ('Tubing Galore',),
    ]
    mycursor.executemany(sql, val)
    # Committing the changes to the table
    db.commit()


# Creating a Function to populate table rows
def employees():
    sql = "INSERT INTO employees (first_name, last_name, department) VALUES (%s,%s,%s)"
    val = [
        ('Janet', 'Collins', 'Finance'),
        ('Roz', 'Murphy', 'Marketing'),
        ('Bob', 'Ulrich', 'Marketing'),
        ('Henry', 'Doyle', 'Production'),
        ('Maria', 'Constanza', 'Distribution'),
        ('Sam', 'Sammy', 'Production'),
    ]
    mycursor.executemany(sql, val)
    # Committing the changes to the table
    db.commit()


# Creating a Function to populate table rows
def hours():
    sql = "INSERT INTO hours_worked (date, hours_worked,employee_id) VALUES (%s,%s,%s)"
    val = [
        ('2020-07-10', 100, 1),
        ('2020-07-10', 100, 2),
        ('2020-07-10', 100, 3),
        ('2020-07-10', 100, 4),
        ('2020-07-10', 100, 5),
        ('2020-07-10', 100, 6),
    ]
    mycursor.executemany(sql, val)
    # Committing the changes to the table
    db.commit()


# Creating a Function to populate table rows
def supply_orders():
    supply_order_sql = "INSERT INTO supply_orders (order_date, estimated_delivery, actual_delivery, suppliers_id) " \
                       "VALUES (%s,%s,%s,%s)"
    supply_order_line_items_sql = "INSERT INTO supply_orders_line_items (supply_order_id, supplies_id, quantity)" \
                                  "VALUES(%s, %s, %s)"

    # Insert values

    # Order 1
    val = ('2020-07-10', '2020-07-15', '2020-07-20', 1)
    mycursor.execute(supply_order_sql, val)
    supply_order_id = mycursor.lastrowid
    val = [
        (supply_order_id, 1, 20),
        (supply_order_id, 2, 20)
    ]
    mycursor.executemany(supply_order_line_items_sql, val)

    # Order 2
    val = ('2020-07-10', '2020-07-15', '2020-07-20', 2)
    mycursor.execute(supply_order_sql, val)
    # Insert into supply order line item for last record
    supply_order_id = mycursor.lastrowid
    val = [
        (supply_order_id, 3, 20),
        (supply_order_id, 4, 20)
    ]
    mycursor.executemany(supply_order_line_items_sql, val)

    # Order 3
    val = ('2020-07-10', '2020-07-15', '2020-07-20', 3)
    mycursor.execute(supply_order_sql, val)
    # Insert into supply order line item for last record
    supply_order_id = mycursor.lastrowid
    val = [
        (supply_order_id, 5, 20),
        (supply_order_id, 6, 20)
    ]
    mycursor.executemany(supply_order_line_items_sql, val)

    # Committing the changes to the table
    db.commit()


# Creating a Function to populate table rows
def product_orders():
    sql = "INSERT INTO product_orders (date_of_order, product_id, quantity, cost_per_unit, distributors_id) VALUES (%s,%s,%s,%s,%s)"
    val = [
        ('2020-07-10', 1, 50, 5, 1),
        ('2020-07-10', 2, 50, 6, 2),
        ('2020-07-10', 3, 50, 7, 3),
        ('2020-07-10', 4, 50, 8, 4),
        ('2020-07-10', 3, 50, 7, 5),
        ('2020-07-10', 4, 50, 8, 6),
    ]
    mycursor.executemany(sql, val)
    # Committing the changes to the table
    db.commit()


'''The creating functions to print specific tables'''


def print_distributors():
    # Selecting fields from team table
    mycursor.execute("SELECT distributors_id, distributors_name FROM distributors")
    # Storing results from cursor.execute in variable
    distributor_info = mycursor.fetchall()
    print("\n -- DISPLAYING DISTRIBUTORS RECORDS --")
    # Iterating through variable storing query results and displaying the output
    for dist in distributor_info:
        print(" Distributors Id: {}\n Distributors Name: {}\n".format(dist[0], dist[1]))


def print_products():
    # Selecting fields from product table
    mycursor.execute("SELECT product_id, product_name, quantity FROM product")
    # Storing results from cursor.execute in variable
    product_info = mycursor.fetchall()
    print("\n -- DISPLAYING PRODUCT RECORDS --")
    # Iterating through variable storing query results and displaying the output
    for prod in product_info:
        print(" Product Id: {}\n Product Name: {}\n Quantity: {}\n".format(prod[0], prod[1], prod[2]))


def print_product_orders():
    # Selecting fields from product_orders table
    mycursor.execute(
        "SELECT product_order_id, date_of_order, product_id, quantity, cost_per_unit, distributors_id FROM product_orders")
    # Storing results from cursor.execute in variable
    product_order_info = mycursor.fetchall()
    print("\n -- DISPLAYING PRODUCT ORDER RECORDS --")
    # Iterating through variable storing query results and displaying the output
    for order in product_order_info:
        print(
            " Product Order Id: {}\n Date of Order: {}\n Product Id: {}\n quantity: {}\n Cost per Unit: {}\n Distributors Id: {}\n"
                .format(order[0], order[1], order[2], order[3], order[4], order[5]))


def print_suppliers():
    # Selecting fields from suppliers table
    mycursor.execute("SELECT suppliers_id, suppliers_name FROM suppliers")
    # Storing results from cursor.execute in variable
    suppliers_info = mycursor.fetchall()
    print("\n -- DISPLAYING SUPPLIERS RECORDS --")
    # Iterating through variable storing query results and displaying the output
    for supplier in suppliers_info:
        print(" Suppliers Id: {}\n Suppliers Name: {}\n".format(supplier[0], supplier[1]))


def print_supplies():
    # Selecting fields from supplies table
    mycursor.execute("SELECT supplies_id, supply_name, quantity FROM supplies")
    # Storing results from cursor.execute in variable
    supplies_info = mycursor.fetchall()
    print("\n -- DISPLAYING SUPPLIES RECORDS --")
    # Iterating through variable storing query results and displaying the output
    for supply in supplies_info:
        print(" Supplies Id: {}\n Supply Name: {}\n quantity: {}\n".format(supply[0], supply[1], supply[2]))


def print_supply_orders():
    # Selecting fields from supply_orders table
    sql = "SELECT " \
          "supply_orders.supply_order_id, order_date, supplies_id, quantity, " \
          "estimated_delivery, actual_delivery, suppliers_id FROM supply_orders " \
          "INNER JOIN supply_orders_line_items " \
          "ON supply_orders_line_items.supply_order_id = supply_orders.supply_order_id;"
    mycursor.execute(sql)
    # Storing results from cursor.execute in variable
    supply_order_info = mycursor.fetchall()
    print("\n -- DISPLAYING SUPPLY ORDERS RECORDS --")
    # Iterating through variable storing query results and displaying the output
    for supplyorder in supply_order_info:
        print(
            " Supply Order Id: {}\n Order Date: {}\n Supplies Id: {}\n quantity: {}\n Estimated Delivery: {}"
            "\n Actual Delivery: {}\n Suppliers Id: {}\n"
                .format(supplyorder[0], supplyorder[1], supplyorder[2], supplyorder[3], supplyorder[4],
                        supplyorder[5], supplyorder[6]))


def print_employees():
    # Selecting fields from employees table
    mycursor.execute("SELECT employee_id, first_name, last_name, department FROM employees")
    # Storing results from cursor.execute in variable
    employee_info = mycursor.fetchall()
    print("\n -- DISPLAYING EMPLOYEE RECORDS --")
    # Iterating through variable storing query results and displaying the output
    for employee in employee_info:
        print(" Employee Id: {}\n First Name: {}\n Last Name: {}\n Department: {}\n".format(employee[0], employee[1],
                                                                                            employee[2], employee[3]))


def print_hours_worked():
    # Selecting fields from hours_worked table
    mycursor.execute("SELECT entry_id, date, hours_worked, employee_id FROM hours_worked")
    # Storing results from cursor.execute in variable
    hours_worked_info = mycursor.fetchall()
    print("\n -- DISPLAYING HOURS WORKED RECORDS --")
    # Iterating through variable storing query results and displaying the output
    for hour in hours_worked_info:
        print(" Entry Id: {}\n Date: {}\n Hours Worked: {}\n Employee Id: {}\n".format(hour[0], hour[1], hour[2],
                                                                                       hour[3]))


'''The following populate their respective tables, comment them out as needed'''

distributors()
product()
supplies()
suppliers()
employees()
hours()
supply_orders()
product_orders()

'''The following functions prints their respective tables, comment them out as needed'''
print_distributors()
print_products()
print_product_orders()
print_suppliers()
print_supplies()
print_supply_orders()
print_employees()
print_hours_worked()

"""
Resources:
execute *.sql file with python MySQLdb. (2010, December 10). Stack Overflow. https://stackoverflow.com/questions/4408714/execute-sql-file-with-python-mysqldb
Getting Started with MySQL in Python. (2019, December 9). Datacamp.Com. https://www.datacamp.com/community/tutorials/mysql-python
MySQL Commands out of sync Python. (2019, January 1). Stack Overflow. https://stackoverflow.com/questions/53994303/mysql-commands-out-of-sync-python
Python MySQL Create Table. (n.d.). W3schools.Com. Retrieved July 11, 2021, from https://www.w3schools.com/python/python_mysql_create_table.asp
"""
