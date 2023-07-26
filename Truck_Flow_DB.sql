create database Truck_Flow_2;
use Truck_Flow_2;
create table Employee_Info(Employee_ID int primary key auto_increment,Employee_Name varchar(10),Employee_Age int(2),Employee_Gender varchar(6),Employee_Field varchar(10),Access_Key varchar(20));
alter table Employee_Info auto_increment=1001;
create view Operator_Info as select Employee_ID ,Employee_Name as Operator_Name,Employee_Age as Operator_Age,Employee_Gender as Operator_Gender,Access_Key as Operator_Key from Employee_Info where Employee_Field ="Operator";
create view Manager_Info as select Employee_ID ,Employee_Name as Manager_Name,Employee_Age as Manager_Age,Employee_Gender as Manager_Gender,Access_Key as Manager_Key from Employee_Info where Employee_Field ="Manager";
Create Table Truck_Info(Ticket_No int primary key auto_increment,Reg_No varchar(20),Type_Of_Goods varchar(10),Registered_By varchar(5),Driver_Name varchar(20),Driver_Contact varchar(10),Agency_Name varchar(20),Agency_Contact varchar(10),time_stamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
alter table Truck_Info auto_increment=001;
create view Driver_Info as select Driver_Name,Reg_No as Truck_Registration,Driver_Contact,Agency_Name,Agency_Contact,Ticket_No from Truck_Info;
create view Current_Queue as select Ticket_No,Reg_No as Truck_Registration_Number,Type_Of_Goods as cargo_type from Truck_Info;
Create Table Truck_DB(Ticket_No int primary key auto_increment,Reg_No varchar(20),Type_Of_Goods varchar(10),Registered_By varchar(5),Driver_Name varchar(20),Driver_Contact varchar(10),Agency_Name varchar(20),Agency_Contact varchar(10),time_stamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
alter table Truck_DB auto_increment=001;
Create Table Warehouse(Ramp_No int primary key,Goods_Type varchar(20),Truck_Reg_No varchar(20),Current_status varchar(10) ,time_stamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);


select *from Employee_Info;
select *from Operator_Info;
select *from Manager_Info;
select *from Truck_Info;
select *from Truck_DB;
select *from Driver_Info;
select *from Current_Queue;
select *from Warehouse;


-- insert into Operator_Info(Operator_Name,Operator_Age,Operator_Gender,Operator_Key) VALUES("Rahul","32","Male","pwd123");
-- insert into Employee_Info(Employee_Name,Employee_Age,Employee_Gender,Employee_Field,Access_Key) VALUES("Zack","41","Male","Operator","pwd234");
-- insert into Employee_Info(Employee_Name,Employee_Age,Employee_Gender,Employee_Field,Access_Key) VALUES("Anjali","27","Female","Operator","pwd345");
-- insert into Employee_Info(Employee_Name,Employee_Age,Employee_Gender,Employee_Field,Access_Key) VALUES("Rahul","31","Male","Manager","pwd456");
-- insert into Employee_Info(Employee_Name,Employee_Age,Employee_Gender,Employee_Field,Access_Key) VALUES("Suresh","28","Male","Staff","pwd000");

-- insert into Warehouse(Ramp_No,Goods_Type) VALUES(23,"Dairy");
-- insert into Warehouse(Ramp_No,Goods_Type) VALUES(24,"Poultry");
-- insert into Warehouse(Ramp_No,Goods_Type) VALUES(25,"Vegetables");



SHOW ENGINE INNODB STATUS;