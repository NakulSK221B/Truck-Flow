from SQL_Bridge import SQL_Link
from Driver import driver
class truck(driver):
    _reg_no=""
    _Cargo=""
    _Emp_ID=""
    _D_Name=""
    _D_Contact=""
    _Agency_Name=""
    _Agency_Contact=""
    
    def settruckdetails(self,Employee_ID):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        print("\nRegistering New Truck....")
        self.reg_no=input("\nEnter Registration Number of the truck:")
        self.Cargo=self.cargo_type()
        self.Emp_ID=Employee_ID
        self.D_Name=input("\nEnter Driver's Name:")
        self.D_Contact=input("\nEnter Driver's Contact:")
        self.Agency_Name=input("\nEnter Agency's Name:")
        self.Agency_Contact=input("\nEnter Agency's Contact:")
        mycursor.execute("INSERT INTO Truck_Info(Reg_No,Type_Of_Goods,Registered_By,Driver_Name,Driver_Contact,Agency_Name,Agency_Contact)VALUES(%s,%s,%s,%s,%s,%s,%s)",(str(self.reg_no),str(self.Cargo),str(self.Emp_ID),str(self.D_Name),str(self.D_Contact),str(self.Agency_Name),str(self.Agency_Contact)))
        Ticket_No=mycursor.lastrowid
        print("\nTicket Number Issued:",Ticket_No)
        mydb.commit()
    
    def cargo_type(self):
        choose=input("\nChoose Cargo Type: \n(1)Dairy \n(2)Poultry \n(3)Vegetables \n(4)Beverages \nEnter Your Choice:")
        if choose=="1":
            cargo="Dairy"
            return str(cargo)
        elif choose=="2":
            cargo="Poultry"
            return str(cargo)
        elif choose=="3":
            cargo="Vegetables"
            return str(cargo)
        elif choose=="4":
            cargo="Beverages"
            return str(cargo)
        
        
    def printtruckdetails(self,Ticket_No):
        mydb=SQL_Link.SQL_Login()
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT * FROM Truck_Info where Ticket_No =%s;",(str(Ticket_No),))
        record=mycursor.fetchall()
        print("\nPrinting truck Details....\n")
        for row in record:
            print("Ticket Number: ", row[0], )
            print("Registration Number:", row[1])
            print("Cargo Type:", row[2])
            print("Employee ID of Registerer:", row[3])
            print("Driver Name", row[4])
            print("Driver Contact", row[5])
            print("Agency Name", row[6])
            print("Agency Contact", row[7])
            
            
    def Backup_Truck_Info(self):
        mydb=SQL_Link.SQL_Login()
        mycursor=mydb.cursor()
        
        mycursor.execute("INSERT INTO Truck_DB(Reg_No,Type_Of_Goods,Registered_By,Driver_Name,Driver_Contact,Agency_Name,Agency_Contact) SELECT Reg_No,Type_Of_Goods,Registered_By,Driver_Name,Driver_Contact,Agency_Name,Agency_Contact FROM Truck_Info")
        print("\nTruck Info Backed up successfully....\n")
        mydb.commit()
        
        
# t1=truck()
# t1.settruckdetails("1002")
# # t1.Backup_Truck_Info()
# # t1.printtruckdetails("001")
# # t2=truck()
# # t2.setdimensions('KA 20 rA 2345', 23, 34, 45, 'B45')
# # t2.printdimensions()
# # print(truck.truck_dict)
    
        