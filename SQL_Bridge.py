# -*- coding: utf-8 -*-
"""
Created on Mon May 9 11:41:03 2022

@author: NAKUL
"""
import mysql.connector

class SQL_Link():
    
    def SQL_Login():
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          password="A11F0R0N3",
          database="Truck_Flow_2")
        return mydb
    
    

# sql=SQL_Link()
# sql.SQL_Login()
# print("connected")
#mycursor = mydb.cursor()
#Create New DB
# mycursor.execute("CREATE DATABASE mydatabase")

# #TO CHECK ALL CURRENT DB
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)
  
#TO Create Table 
#mycursor.execute("CREATE TABLE Employee (Employee_ID INT AUTO_INCREMENT PRIMARY KEY, Company_name VARCHAR(255),name VARCHAR(255))")

# Insert Values
# statement = "INSERT INTO Employee (Employee_ID, Company_name, name) VALUES (%s, %s, %s)"
# values = [
#   (101,'ABC','Peter'),
#   (102,'ABC','Tony'),
#   (103,'ABC','Bruce'),
#   (104,'ABC','Robin'),
#   (105,'ABC','Selena')]

# mycursor.executemany(statement,values)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")


