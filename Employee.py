from SQL_Bridge import SQL_Link

class employee:
    def __init__(self):
        print("\n....")
        
    # def setemployeedetails(self):
        
    
    def printemployeedetails(self,Employee_ID):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT * FROM Employee_Info where Employee_ID =%s;",(str(Employee_ID),))
        record=mycursor.fetchall()
        print("\nPrinting Employee Details....\n")
        for row in record:
            print("Employee Id :", row[0], )
            print("Name: ", row[1])
            print("Age:", row[2])
            print("Gender: ", row[3])
            print("Employment Position:",row[4])
       
    
        
# e1=employee()
# e1.setemployeedetails()
# e1.printemployeedetails("1001")