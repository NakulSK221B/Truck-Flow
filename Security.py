from Employee import employee
from SQL_Bridge import SQL_Link
from Truck import truck as tr
from Queue import Queue as Q
import site
class Security(employee,tr,Q):
    def __init__(self):
        print("...")
    
    def Security_Login(self):
        Security_ID=str(input("\nEnter Security ID: "))
        Security_Key=str(input("\nEnter Security Key: "))
        print("Verifing....")
        Security.Security_verify(Security_ID,Security_Key)
        self.ID=Security_ID
        return Security_ID
        
    def printSecuritydetails(self,Security_ID):
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT * FROM Operator_Info where Employee_ID =%s;",(str(Security_ID),))
        record=mycursor.fetchall()
        print("\nPrinting Security Details....\n")
        for row in record:
            print("Employee Id = ", row[0], )
            print("Name = ", row[1])
            print("Age  = ", row[2])
            print("Gender  = ", row[3], "\n")
            
            
    def Security_verify(Security_ID,Security_Key):
        
        mydb=SQL_Link.SQL_Login()
       
        mycursor=mydb.cursor()
        
        mycursor.execute("SELECT * FROM Operator_Info where Employee_ID = %s and Operator_Key = %s;",(str(Security_ID),str(Security_Key)))
        Login_Status=mycursor.fetchone()
        
        if Login_Status==None:
            print("\nError, Your Credentials were invalid !")
            site.sys.exit()
            
        else:
            print("\nLogin Successful")
            

# o1=Security()
# o1.setSecuritydetails()
# print(Security.Security_Dict)
# o1.printSecuritydetails("1001")