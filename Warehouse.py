# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:34:37 2022

@author: NAKUL
"""
from SQL_Bridge import SQL_Link
from tabulate import tabulate


class Ramps:
    def Display_ALL_Ramp_Status(self):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT Ramp_No,Goods_Type,Truck_Reg_No,Current_status FROM Warehouse ;")
        result=mycursor.fetchall()
        print("\nWarehouse Status: \n")
        print(tabulate(result, headers=['Ramp Number', 'Goods type','Truck Registration Number','Status'], tablefmt='psql'))
    
    def Empty_Ramp(self,Ramp_No):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("UPDATE Warehouse SET Truck_Reg_No=NULL WHERE Ramp_No=%s",(str(Ramp_No),)) 
        mycursor.execute("UPDATE Warehouse SET Current_status='EMPTY' WHERE Ramp_No=%s",(str(Ramp_No),))
        print("\nRamp Number:",Ramp_No,"is now empty...")
        mydb.commit()
        
    def Allocate_Ramp(self,Truck_Reg_No,Goods_Type):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("UPDATE Warehouse SET Truck_Reg_No=%s WHERE Goods_Type=%s AND Current_status='EMPTY'  ",(str(Truck_Reg_No),str(Goods_Type)))
        
        mycursor.execute("UPDATE Warehouse SET Current_status='OCCUPIED' WHERE Truck_Reg_No=%s AND Goods_Type=%s ",(str(Truck_Reg_No),str(Goods_Type)))
        
        mydb.commit()
        
        
        
        
# w1=Ramps()
# w1.Display_ALL_Ramp_Status()
# w1.Empty_Ramp(23)
# w1.Empty_Ramp(26)
# w1.Allocate_Ramp("KA 25 AB 2457 ","Beverages")
# w1.Display_ALL_Ramp_Status()