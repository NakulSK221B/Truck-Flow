# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:27:44 2022

@author: NAKUL
"""

from Employee import employee
from SQL_Bridge import SQL_Link
from Queue import Queue as Q
from Warehouse import Ramps as wh
import site

class manager(employee,Q,wh):
    def __init__(self):
        print("...")
    
    def manager_Login(self):
        manager_ID=str(input("\nEnter manager ID: "))
        manager_Key=str(input("\nEnter manager Key: "))
        print("Verifing....")
        manager.manager_verify(manager_ID,manager_Key)
        return manager_ID
        
    def printmanagerdetails(self,manager_ID):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT * FROM manager_Info where Employee_ID =%s;",(str(manager_ID),))
        record=mycursor.fetchall()
        print("\nPrinting manager Details....\n")
        for row in record:
            print("Employee Id = ", row[0], )
            print("Name = ", row[1])
            print("Age  = ", row[2])
            print("Gender  = ", row[3], "\n")
            
            
    def manager_verify(manager_ID,manager_Key):
        
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT * FROM manager_Info where Employee_ID = %s and manager_Key = %s;",(str(manager_ID),str(manager_Key)))
        Login_Status=mycursor.fetchone()
        
        if Login_Status==None:
            print("\nError, Your Credentials were invalid !")
            site.sys.exit()
        else:
            print("\nLogin Successful")
            

# o1=manager()
# o1.setmanagerdetails()
# print(manager.manager_Dict)
# o1.printmanagerdetails("1003")