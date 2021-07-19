""" import statements """
import mysql.connector as mysql

"""
    Title: bacchus_delivery_report.py
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 18 July 2021
    Description: Which distributor carries which wine?
"""

""" database config object """

db = mysql.connect(
    user="bacchus_user",
    password="MySQL8IsGreat!",
    host="127.0.0.1",
    database="bacchus",
)

# Initialize cursor
cursor = db.cursor()

# Get list of all distributors
sql_all_distributors = "SELECT distributors_id, distributors_name FROM distributors;"
cursor.execute(sql_all_distributors)
distributors = cursor.fetchall()

# Print report title
print("-- Report for which distributor carries which wine?-- \n")

# Iterate through all the distributors and print wines they carry
for distributor in distributors:
    # Retrieve all the wine names current distributor has ever ordered
    sql_distributor_wines = "SELECT product_name " \
                            "FROM product " \
                            "WHERE product_id IN (" \
                            "   SELECT product_id FROM product_orders WHERE distributors_id = " + str(distributor[0]) + \
                            ");"
    cursor.execute(sql_distributor_wines)
    wines_sold_by_distributor = cursor.fetchall()

    # Print distributor name
    print("Distributor Name: {}".format(distributor[1]))

    # Iterate through all the wines this distributor has ever ordered and print
    for wine in wines_sold_by_distributor:
        print("\t{}".format(wine[0]))

    # Print separator
    print("--------------------------")
