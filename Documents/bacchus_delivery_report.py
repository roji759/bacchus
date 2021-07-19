""" 
    Title: bacchus_delivery_report.py
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 17 July 2021
    Description: Generates report for delivery information
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

cursor = db.cursor()

# holds query strings
sql_drop_view ="\
    DROP VIEW IF EXISTS supplier_delivery"

sql_delivery_query = "\
    CREATE VIEW supplier_delivery AS\
    SELECT\
        MONTH(supply_orders.actual_delivery) AS mo,\
        suppliers.suppliers_name,\
        DATEDIFF(supply_orders.actual_delivery, supply_orders.estimated_delivery) AS days_late,\
        DATEDIFF(supply_orders.actual_delivery, supply_orders.order_date) AS delivery_time,\
        supply_orders.suppliers_id,\
        supply_orders.supply_order_id\
    FROM suppliers\
      LEFT OUTER JOIN supply_orders\
        ON supply_orders.suppliers_id = suppliers.suppliers_id"

sql_avg_by_month_query = "\
    SELECT\
        mo,\
        suppliers_name,\
        AVG(days_late),\
        AVG(delivery_time)\
    FROM supplier_delivery\
    GROUP BY\
        suppliers_id,\
        mo\
    ORDER BY\
        mo"

cursor.execute(sql_drop_view)
cursor.execute(sql_delivery_query)


cursor.execute(sql_avg_by_month_query)
deliveries = cursor.fetchall()

print("\n\n-- Report for Supplier Delivery Time by Month --")
for delivery in deliveries:
    print("Month: {}\tSupplier: {}\t\tAverage Days Late: {}\tAverage Delivery Time: {}".format(delivery[0], delivery[1], delivery[2], delivery[3]))

db.close()

input("\n\n Press any key to continue...")