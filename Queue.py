# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:04:40 2022

@author: NAKUL
"""
from SQL_Bridge import SQL_Link
from tabulate import tabulate
from Warehouse import Ramps

class Queue(Ramps):
    def display_Current_Queue(self):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT * FROM Current_Queue limit 0,5 ;")
        result=mycursor.fetchall()
        print("\nCurrent Queue: \n")
        print(tabulate(result, headers=['Ticket_no', 'Registration Number','Cargo type'], tablefmt='psql'))

    def Deletion_Menu(self):
        self.display_Current_Queue()
        Del_Reg=input("Enter Registration Number to be Deleted: ")
        self.Delete_Queue_Entry(Del_Reg)


    def Delete_Queue_Entry(self,Reg_No):
          mydb=SQL_Link.SQL_Login()
         
          mycursor=mydb.cursor()
          
          mycursor.execute("DELETE FROM Truck_Info WHERE Reg_No=%s",(str(Reg_No),))  
          print("\nTruck Number:",Reg_No,"successfully deleted...")
          mydb.commit()
    
          
    def Queue_to_Ramp(self):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT * FROM Current_Queue limit 0,5 ;")
        result=mycursor.fetchall()
        for row in result:
            Truck_Reg_No=row[1]
            Cargo_type=row[2]
            self.Allocate_Ramp(Truck_Reg_No, Cargo_type)
            # if reg_no==None:
            #     print("\nWarehouse Currently at full capacity....")
            # else:
            #     self.Delete_Queue_Entry(reg_no)
        
# Q1=Queue()
# Q1.display_Current_Queue() 
# Q1.Update_Queue_Entry()
# Q1.Queue_to_Ramp()
# # Q1.Delete_Queue_Entry("1")
# Q1.Display_ALL_Ramp_Status()
# Q1.display_Current_Queue()   
        