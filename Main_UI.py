# -*- coding: utf-8 -*-
"""
Created on Sat May 28 19:54:22 2022

@author: NAKUL
"""
from Security import Security as Sc
from Manager import manager as mng

class UI(Sc,mng):
    __ID=""
    def main_screen(self):        
        print("\nWelcome to Trunk Flow Application Console....\n")
        Choice1=int(input("\nChoose Your Interface.....\n(1)Manager \n(2)Security \nEnter Your Selection:"))
        if Choice1==1:
            m1=mng()
            m1.manager_Login()
            self.Manager_Options(m1)
        elif Choice1==2:
            Sc1=Sc()
            Sc1.Security_Login()
            self.Security_Options(Sc1)
        else:
            print("\nInvalid Entry....")
     
    def Security_Options(self,Sc1):
        while(1):
            print("\nWelcome to the Security Console....\n")
            print("Please select your desired action: \n(1)View Current Queue \n(2)Register New Truck \n(3)View Truck Details")
            Choice2=int(input("\nEnter Your Selection:"))
            if Choice2==1:
                Sc1.display_Current_Queue()
            elif Choice2==2:
                Sc1.settruckdetails(Sc1.ID)
                Sc1.Backup_Truck_Info()
                Sc1.Queue_to_Ramp()
            elif Choice2==3:
                T_No=input("\nEnter Ticket Number: ")
                Sc1.printtruckdetails(T_No)
            else:
                print("\nInvalid Entry....")
                
    def Manager_Options(self,m1):
        while(1):
            print("\nWelcome to the Manager Console....\n")
            print("Please select your desired action: \n(1)View Current Queue \n(2)View Warehouse Status \n(3)Empty Ramp \n(4)Delete Truck From Queue \n(5)View Employee Details  ")
            Choice3=int(input("\nEnter Your Selection:"))
            if Choice3==1:
                m1.display_Current_Queue()
            elif Choice3==2:
                m1.Display_ALL_Ramp_Status()
            elif Choice3==3:
                m1.Display_ALL_Ramp_Status()
                Ramp_No=input("\nEnter Ramp Number to be made vacant....")
                m1.Empty_Ramp(Ramp_No)
                m1.Queue_to_Ramp()
                m1.Display_ALL_Ramp_Status()
            elif Choice3==4:
                m1.Deletion_Menu()
            elif Choice3==5:
                e_id=input("\nEnter Employee ID: ")
                m1.printemployeedetails(e_id)
            else:
                print("\nInvalid Entry....")

    
UI1=UI()
UI1.main_screen()
        


