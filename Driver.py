from SQL_Bridge import SQL_Link

class driver:
    
    def __init__(self):
        print("\nNew Driver Registered...")
    
    def printdriverinfo(self,Ticket_No):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT * FROM Driver_Info where Ticket_No =%s;",(str(Ticket_No),))
        record=mycursor.fetchall()
        print("\nPrinting Driver Details....\n")
        if record==None:
            print("\nNo record Found....")
        else:
            for row in record:
                print("Driver Name:", row[0], )
                print("Truck Registration Number: ", row[1])
                print("Driver Contact Number:", row[2])
                print("Agency Name: ", row[3])
                print("Agency Contact Number:",row[4])
                print("Ticket Number: ",row[5])
        
        
# d1=driver()
# d1.setcontactinfo()
# d1.printdriverinfo("001")
# d2=driver()
# d2.setcontactinfo('abc','vrl', 8973274, 894328921)
# print(driver.driver_Dict)