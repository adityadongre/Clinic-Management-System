import mysql.connector as db
from prettytable import PrettyTable

class Patient:
    def __init__(self):
        #connect to server
        mydb = db.connect(host="localhost",user="root",passwd="")

        #create cursor
        myCursor = mydb.cursor()

        #create Database 
        myCursor.execute("create database if not exists BasicDB")

        self.mydb = db.connect(host="localhost",user="root",passwd="",database="BasicDB")
        self.myCursor = self.mydb.cursor()
        
        # craete table
        self.myCursor.execute("""create table if not exists Patient(id int primary key auto_increment,name varchar(25),age int(3),reason varchar(25),adate Date,location varchar(25),mob Bigint)""")

    # insertvalues
    def insertData(self,name,age,reason,a,location,mob):
        query = ("""insert into Patient(name,age,reason,adate,location,mob) values(%s,%s,%s,%s,%s,%s)""")
        data = (name,age,reason,a,location,mob)
        self.myCursor.execute(query,data)
        self.mydb.commit()

    def displayTable(self):
        self.myCursor.execute("""select * from patient""")
        mydata = self.myCursor.fetchall()
        x = PrettyTable()
        x.field_names = ['id','name','age','reason','adate','location','mob']
        for dt in mydata:
            x.add_row(dt)
        print(x)

    def delete(self,n):
        query="""DELETE FROM patient WHERE name = %s"""
        data=(n,)
        self.myCursor.execute(query,data)
        self.mydb.commit()
    
    def search(self,name):
        query = """select * from patient where name=%s"""
        data = (name,)
        self.myCursor.execute(query,data)
        mydata = self.myCursor.fetchone()
        return mydata

    def display(self):
        query = """select * from patient"""
        self.myCursor.execute(query)
        mydata = self.myCursor.fetchall()
        return mydata

    def deletePreviousTable(self):
        self.myCursor.execute("""drop table Patient""")

obj = Patient()

class Doctor:
    def __init__(self):
        #connect to server
        mydb = db.connect(host="localhost",user="root",passwd="")

        #create cursor
        myCursor = mydb.cursor()

        #create Database 
        myCursor.execute("create database if not exists BasicDB")

        self.mydb = db.connect(host="localhost",user="root",passwd="",database="BasicDB")
        self.myCursor = self.mydb.cursor()
        
        # craete table
        self.myCursor.execute("""create table if not exists Doctor(id int primary key auto_increment,name varchar(25),contact Bigint,fees int(5))""")

    def acceptDoctorDetails(self,name,contact,fees):
        query = ("""insert into Doctor(name,contact,fees) values(%s,%s,%s)""")
        data = (name,contact,fees)
        self.myCursor.execute(query,data)
        self.mydb.commit()

    def displayTable(self):
        self.myCursor.execute("""select * from Doctor""")
        mydata = self.myCursor.fetchall()
        x = PrettyTable()
        x.field_names = ['id','name','contact','fees']
        for dt in mydata:
            x.add_row(dt)
        print(x)

    def search(self,rn):
        pass

    def display(self,o):
        pass

    def delete(self,n):
        query="""DELETE FROM doctor WHERE doctor.name = %s"""
        data=(n,)
        self.myCursor.execute(query,data)
        self.mydb.commit()

    def deletePreviousTable(self):
        self.myCursor.execute("""drop table Doctor""")

d = Doctor()

while True:
    print(" \n ================================= ")
    print(" =======WELCOME TO MYCLINIC======= ")
    print(" ================================= ")
    print()
    print("1. Admin \n2. Doctor \n3. Patient \n4. Exit")
    loginchoice = input("Enter your choice :- ")

    if loginchoice == '1':
        adminuserID = 'Admin1'
        adminpassword = '1234'

        choiceadminuserID = input("Enter User ID :- ")
        if choiceadminuserID == adminuserID:

            choiceadminpassword = input("Enter password :- ")
            if choiceadminpassword == adminpassword:
                print("Admin Login Successfull \n")

                while True:
                    print("1. Docter Details \n2. Patient Details \n3. Exit")
                    
                    achoice = input("Enter Your Choice :- ")
                    if achoice == '1':
                        print("Docter Details")

                        while True:
                            print("\n1. Display Docter Details \n2. Delete Docter Details \n3. Add Docter \n4. Exit")
                            dchoice = input("Enter Your choice :- ")

                            if dchoice == '1':
                                print("Display Docter Details")
                                print("\n List of Docters\n")
                                
                                # full Table Display
                                d.displayTable()

                                print("1. Want to See Again \n2. Exit")
                                nExit = input("Enter Choice :- ")
                                if nExit == 2:
                                    break

                            elif dchoice == '2':
                                print("Delete Docter Details")
                                while True:
                                    n = input("Enter Docter Name :- ")
                                    #Delete
                                    d.delete(n)

                                    d.displayTable()

                                    print("1. Want to delete another Docter data \n2. Exit")
                                    nExit=int(input("Enter your Choice :-"))
                                    if nExit==2:
                                        break

                            elif dchoice == '3':
                                while True:
                                    print("Add New Docter")

                                    name = input("Enter Docter Name :- ")

                                    import re
                                    while True:
                                        contact = input("Enter valid contact number :- ")
                                        pattern = re.compile("(0|91)?[-\s]?[7-9][0-9]{9}$")
                                        if pattern.match(contact):
                                            break
                                        else:
                                            print(f"{contact} is not valid")

                                    while True:
                                        fees = input("Enter Docter Fees :- ")
                                        if fees.isdigit() == True:
                                            fees = int(fees)
                                            break
                                        else:
                                            print("Invalid Input Try Again !!!!")

                                    d.acceptDoctorDetails(name,contact,fees)

                                    d.displayTable()

                                    print("1.Enter New Entry\n2.Exit")
                                    ch1 = input("Enter Choice :- ")
                                    if ch1 == '1':
                                        continue
                                    elif ch1 == '2':
                                        print("Thank You!!!")
                                        break
                                    else:
                                        print("Invalid INPUT!!!!!")
                                        break

                            elif dchoice == '4':
                                print("Exit Docter")
                                break

                            else:
                                print("INVALID INPUT PLEASE TRY AGAIN!!!!!!!\n")

                    elif achoice == '2':
                        print("\nPatient Details")

                        while True:
                            print("\n1. Display Patient Details \n2. Search Patient Details \n3. Delete Patient Details \n4. Exit")
                            pchoice = input("Enter your Choice :- ")
                        
                            if pchoice == '1':
                                print("1. Display Patient Details")
                                print("\n List of Patients \n")

                                #full table display
                                data = obj.display()

                                x = PrettyTable()
                                x.field_names=['id','name','age','reason','adate','location','mob']
                                for dt in data:
                                    x.add_row(dt)
                                print(x)

                                print("1. Want to See Again \n2. Exit")
                                nExit = input("Enter Choice :- ")
                                if nExit == 2:
                                    break

                            elif pchoice == '2':
                                print("2. Search Patient Details")                         
                                while True:
                                    name = input("Enter Patient Name :-")
                                    data = obj.search(name)       
                                    x = PrettyTable()
                                    x.field_names=['id','name','age','reason','adate','location','mob']
                    
                                    x.add_row(data)
                                    print(x)  
                                    
                                    print("\n1. Want to see another patient data\n2. Exit")
                                    nExit = int(input("Enter Your Choice :- "))
                                    if nExit==2:
                                        break

                            elif pchoice == '3':
                                print("3. Delete Details of Patient")
                                while True:
                                    n = input("Enter Patient Name :- ")                                    
                                    #Delete
                                    obj.delete(n)
                                    print("List After Deletion")
                                    obj.displayTable()

                                    print("1. Want to delete another Patient data \n2. Exit")
                                    nExit=int(input("Enter your Choice :-"))
                                    if nExit==2:
                                        break

                            elif pchoice == '4':
                                print("Exit Patient Details\n")
                                break

                            else:
                                print("INVALID INPUT PLEASE TRY AGAIN!!!!!!!\n")    
                                
                    elif achoice == '3':
                        print("Exit Admin \n")
                        break

                    else:
                        print("INVALID ADMIN CHOICE !!!!!! \n")

            else:
                print("****WRONG PASSWORD****\n")

        else:
            print("INVALID USER ID !!!!!!\n")

    elif loginchoice == '2':
        docteruserID = 'Doctor'
        docterpassword = '1234'

        choicedocteruserID = input("Enter userID :- ")
        if choicedocteruserID == docteruserID:

            choicedocterpassword = input ("Enter password :- ")
            if choicedocterpassword == docterpassword:
                print("Doctor Login Successfull \n")
                while True:
                    obj.displayTable()
                    
                    print("\n1. Want to search another Patient \n2. Exit")
                    nExit = int(input("Enter Your Choice :- "))
                    if nExit == 2:
                        break

            else:
                print("****WRONG PASSWORD****\n")

        else:
            print("INVALID USER ID !!!!!!\n")

    elif loginchoice == '3':
        print("Patient Login\n")
        while True:
            print("1. Take Appointment \n2. Display Details \n3. Exit")
            pchoice1 = input("Enter your Choice :- ")
            
            if pchoice1 == '1':
                while True:
                    print("Take A Appointment ")
                    #Name
                    name = input("Enter Patient Name :- ")

                    #Age
                    while True:
                        age = input("Enter Patient Age :- ")
                        if age.isdigit() == True:
                            age=int(age)
                            break
                        else:
                            print("Invalid input Try Again !!!!")

                    #Reason
                    reason = input("Enter your Reason :- ")

                    #Appointment Date
                    import datetime
                    a = datetime.datetime.now()
                    res = a.strftime("%d %b %Y")
                    # adate = input("Enter your Appointment Date :-",res)
                    adate = print("Appointment Date :- ",res)

                    #Location
                    location = input("Enter your Location :-")
                    
                    import re
                    #Mobile number
                    while True:
                        mob = input("Enter valid number :- ")
                        pattern = re.compile("(0|91)?[-\s]?[7-9][0-9]{9}$")
                        if pattern.match(mob):
                            break
                        else:
                            print(f"{mob} is not valid")

                    obj.insertData(name,age,reason,a,location,mob)

                    print("\n1. Want to take anthor appointment \n2. Exit")
                    nExit = int(input("Enter Your Choice :- "))
                    if nExit == 2:
                        break

            elif pchoice1 == '2':
                print("Display Patient Details \n")
                while True:
                    #Search
                    name = input("Enter Patient Name :- ")

                    data = obj.search(name)       
                    x = PrettyTable()
                    x.field_names=['id','name','age','reason','adate','location','mob']
                    # for dt in data:
                    x.add_row(data)
                    print(x)             

                    print("\n1. Want to see another patient data\n2. Exit")
                    nExit = int(input("Enter Your Choice :- "))
                    if nExit==2:
                        break
                    
            elif pchoice1 == '3':
                print("Exit")
                break

            else:
                print("INVALID INPUT PLEASE TRY AGAIN!!!!!!!\n")

    elif loginchoice == '4':
        print("exit Login")
        break

    elif loginchoice == '*':
        obj.deletePreviousTable()
        d.deletePreviousTable()
        break

    elif loginchoice == '#':
        d.acceptDoctorDetails("Doctor",7738125294,100)
        break

    else:
        print("INVALID INPUT PLEASE TRY AGAIN!!!!!!! \n")
