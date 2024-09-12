# WELCOME
topic=">>>>>>>My Cab<<<<<<"
t=topic.center(70)
print (t)
name = input("What is Your Name - ")
x="Hi,"+name+". Welcome to My Cab!"
y=x.center(70)
print(y)

# AVAILABLE VEHICLE LISTS
A_AC_cars = ["Mazda_Axela","Honda_Civic","Toyota_Premio"]
A_NonAC_cars = ["TATA_Mini_Cab","Suzuki_Alto"]
A_AC_vans = ["Toyota_KDH","Nissan_Caravan","Toyota_Noah"]
A_NonAC_vans = ["Toyota_Litease","Nissan_Vanette"]
A_Three_wheelers = ["Bajaj","TVS_King","Piaggio"]
A_Lorries = ["Toyota","Nissan","Fuso","Isuzu"]
A_Trucks = ["Toyota","Nissan","Fuso","Isuzu","MAN"]
a=[1,2,]


# BOOKED VEHICLES LIST
B_AC_cars = []
B_NonAC_cars = []
B_AC_vans = []
B_NonAC_vans = []
B_Three_wheelers = []
B_Lorries = []
B_Trucks = []

p=5
q=6
r=p+q
print(r)

# ADDING OPTION
def Add_AC_Car():
    print("Our Available AC Cars : ")
    print(A_AC_cars)
    addACcars=input("\n\nWhich car do you want to add?\nEnter Car Name -")
    A_AC_cars.insert(0, addACcars)
    print("\n\nNow Our Available AC Cars : ")
    print(A_AC_cars)
    Add_Vehi_Back()

def Add_NonAC_Car():
    print("Our Available NonAC Cars : ")
    print(A_NonAC_cars)
    addNonACcars=input("\n\nWhich car do you want to add?\nEnter Car Name -")
    A_NonAC_cars.insert(0, addNonACcars)
    print("\n\nNow Our Available NonAC Cars : ")
    print(A_NonAC_cars)
    Add_Vehi_Back()

def Add_AC_Van():
    print("Our Available AC Vans : ")
    print(A_AC_vans)
    addACvans=input("\n\nWhich van do you want to add?\nEnter Van Name -")
    A_AC_vans.insert(0, addACvans)
    print("\n\nNow Our Available AC Vans : ")
    print(A_AC_vans)
    Add_Vehi_Back()

def Add_NonAC_Van():
    print("Our Available NonAC Vans : ")
    print(A_NonAC_vans)
    addNonACvans=input("\n\nWhich van do you want to add?\nEnter Van Name -")
    A_NonAC_vans.insert(0, addNonACvans)
    print("\n\nNow Our Available NonAC Vans : ")
    print(A_NonAC_vans)
    Add_Vehi_Back()

def Add_Three_Wheeler():
    print("Our Available Three Wheelers : ")
    print(A_Three_wheelers)
    addThreewheelers=input("\n\nWhich Three Wheeler do you want to add?\nEnter Three Wheeler Name -")
    A_Three_wheelers.insert(0, addThreewheelers)
    print("\n\nNow Our Available Three Wheelers : ")
    print(A_Three_wheelers)
    Add_Vehi_Back()

def Add_Lorry():
    print("Our Available Lorries : ")
    print(A_Lorries)
    addLorries=input("\n\nWhich lorry do you want to add?\nEnter Lorry Name -")
    A_Lorries.insert(0, addLorries)
    print("\n\nNow Our Available Lorries : ")
    print(A_Lorries)
    Add_Vehi_Back()

def Add_Trucks():
    print("Our Available Trucks : ")
    print(A_Trucks)
    addTrucks=input("\n\nWhich truck do you want to add?\nEnter Truck Name -")
    A_Trucks.insert(0, addTrucks)
    print("\n\nNow Our Available Trucks : ")
    print(A_Trucks)
    Add_Vehi_Back()

def Add_Vehicle():
    print("\n\nWhich vehicle do you want to add?\n  1.AC Cars\n  2.NonAC Cars\n  3.AC vans\n  4.NonAC Vans\n  5.Three Wheelers\n  6.Lorries\n  7.Trucks")
    addVehicle=int(input("Enter Your Number - "))
    if addVehicle==1:
        Add_AC_Car()
    elif addVehicle==2:
        Add_NonAC_Car()
    elif addVehicle==3:
        Add_AC_Van()
    elif addVehicle==4:
        Add_NonAC_Van()
    elif addVehicle==5:
        Add_Three_Wheeler()
    elif addVehicle==6:
        Add_Lorry()
    elif addVehicle==7:
        Add_Trucks()
    else:
        print("Invalid Number")
        Add_Vehicle()

def Add_Vehi_Back():
    print("\n\n92.Back to the main menu\n94.Back to the add vehicle menu")
    vehi_back_num=int(input("Enter Your Number - "))
    if vehi_back_num==92:
        Mainmenu()
    elif vehi_back_num==94:
        Add_Vehicle()
    else:
        print("Invalid number")
        Add_Vehi_Back()



# REMOVE OPTION
def Remove_AC_Car():
    print("Our Available AC Cars : ")
    print(A_AC_cars)
    removeACcars = input("\n\nWhich car do you want to remove?\nEnter Car Name - ")
    A_AC_cars.remove(removeACcars)
    print("\n\nNow Our Available AC Cars : ")
    print(A_AC_cars)
    Remove_Vehi_Back()

def Remove_NonAC_Car():
    print("Our Available NonAC Cars : ")
    print(A_NonAC_cars)
    removeNonACcars=input("\n\nWhich car do you want to remove?\nEnter Car Name -")
    A_NonAC_cars.remove(removeNonACcars)
    print("\n\nNow Our Available NonAC Cars : ")
    print(A_NonAC_cars)
    Remove_Vehi_Back()

def Remove_AC_Van():
    print("Our Available AC Vans : ")
    print(A_AC_vans)
    removeACvans = input("\n\nWhich van do you want to remove?\nEnter Van Name -")
    A_AC_vans.remove(removeACvans)
    print("\n\nNow Our Available AC Vans : ")
    print(A_AC_vans)
    Remove_Vehi_Back()

def Remove_NonAC_Van():
    print("Our Available NonAC Vans : ")
    print(A_NonAC_vans)
    removeNonACvans = input("\n\nWhich van do you want to remove?\nEnter Van Name -")
    A_NonAC_vans.remove(removeNonACvans)
    print("\n\nNow Our Available NonAC Vans : ")
    print(A_NonAC_vans)
    Remove_Vehi_Back()

def Remove_Three_Wheeler():
    print("Our Available Three Wheelers : ")
    print(A_Three_wheelers)
    removeThreewheelers=input("\n\nWhich Three Wheeler do you want to remove?\nEnter Three Wheeler Name -")
    A_Three_wheelers.remove(removeThreewheelers)
    print("\n\nNow Our Available Three Wheelers : ")
    print(A_Three_wheelers)
    Remove_Vehi_Back()

def Remove_Lorry():
    print("Our Available Lorries : ")
    print(A_Lorries)
    removeLorries=input("\n\nWhich lorry do you want to remove?\nEnter Lorry Name -")
    A_Lorries.remove(removeLorries)
    print("\n\nNow Our Available Lorries : ")
    print(A_Lorries)
    Remove_Vehi_Back()

def Remove_Trucks():
    print("Our Available Trucks : ")
    print(A_Trucks)
    removeTrucks=input("\n\nWhich truck do you want to remove?\nEnter Truck Name -")
    A_Trucks.remove(removeTrucks)
    print("\n\nNow Our Available Trucks : ")
    print(A_Trucks)
    Remove_Vehi_Back()

def Remove_Vehicle():
    print("\n\nWhich vehicle do you want to remove?\n  1.AC Cars\n  2.NonAC Cars\n  3.AC vans\n  4.NonAC Vans\n  5.Three Wheelers\n  6.Lorries\n  7.Trucks")
    removeVehicle=int(input("Enter Your Number - "))
    if removeVehicle==1:
        Remove_AC_Car()
    elif removeVehicle==2:
        Remove_NonAC_Car()
    elif removeVehicle==3:
        Remove_AC_Van()
    elif removeVehicle==4:
        Remove_NonAC_Van()
    elif removeVehicle==5:
        Remove_Three_Wheeler()
    elif removeVehicle==6:
        Remove_Lorry()
    elif removeVehicle==7:
        Remove_Trucks()
    else:
        print("Invalid Number")
        Remove_Vehicle()

def Remove_Vehi_Back():
    print("\n\n92.Back to the main menu\n95.Back to the remove vehicle menu")
    vehi_back_num=int(input("Enter Your Number - "))
    if vehi_back_num==92:
        Mainmenu()
    elif vehi_back_num==95:
        Remove_Vehicle()
    else:
        print("Invalid number")
        Add_Vehi_Back()




# HIRE VEHICLES
def Hire_AC_Cars():
    fname=input("Enter Your Full Name : ")
    age=int(input("Enter Your Age :"))
    nic=input("Enter Your NIC : ")
    if age>=18:
        print("Our Available AC Cars : ")
        print(A_AC_cars)
        removeACcars = input("\n\nWhich car do you want to Hire?\nEnter Car Name - ")
        A_AC_cars.remove(removeACcars)
        B_AC_cars.insert(0, removeACcars)
        print(fname + "," + removeACcars + " is hired successfully")
        print("\n\nNow Our Available AC Cars : ")
        print(A_AC_cars)
        Hire_Backmenu()
    else:
        print("Sorry.You Can't Hire A Vehicle!")
        Welcomemenu()

def Hire_NonAC_Cars():
    fname = input("Enter Your Full Name : ")
    age = int(input("Enter Your Age : "))
    nic = input("Enter Your NIC : ")
    if age >= 18:
        print("Our Available NonAC Cars : ")
        print(A_NonAC_cars)
        removeNonACcars = input("\n\nWhich car do you want to Hire?\nEnter Car Name -")
        A_NonAC_cars.remove(removeNonACcars)
        B_NonAC_cars.insert(0, removeNonACcars)
        print(fname + "," + removeNonACcars + " is hired successfully")
        print("\n\nNow Our Available NonAC Cars : ")
        print(A_NonAC_cars)
        Hire_Backmenu()

    else:
        print("Sorry.You Can't Hire A Vehicle!")
        Welcomemenu()

def Hire_AC_Vans():
    fname = input("Enter Your Full Name : ")
    age = int(input("Enter Your Age : "))
    nic = input("Enter Your NIC : ")
    if age >= 18:
        print("Our Available AC Vans : ")
        print(A_AC_vans)
        removeACvans = input("\n\nWhich van do you want to Hire?\nEnter Van Name -")
        A_AC_vans.remove(removeACvans)
        B_AC_vans.insert(0, removeACvans)
        print(fname + "," + removeACvans + " is hired successfully")
        print("\n\nNow Our Available AC Vans : ")
        print(A_AC_vans)
        Hire_Backmenu()

    else:
        print("Sorry.You Can't Hire A Vehicle!")
        Welcomemenu()

def Hire_NonAC_Vans():
    fname = input("Enter Your Full Name : ")
    age = int(input("Enter Your Age : "))
    nic = input("Enter Your NIC : ")
    if age >= 18:
        print("Our Available NonAC Vans : ")
        print(A_NonAC_vans)
        removeNonACvans = input("\n\nWhich van do you want to Hire?\nEnter Van Name -")
        A_NonAC_vans.remove(removeNonACvans)
        B_NonAC_vans.insert(0, removeNonACvans)
        print(fname + "," + removeNonACvans + " is hired successfully")
        print("\n\nNow Our Available NonAC Vans : ")
        print(A_NonAC_vans)
        Hire_Backmenu()

    else:
        print("Sorry.You Can't Hire A Vehicle!")
        Welcomemenu()

def Hire_Three_Wheeler():
    fname = input("Enter Your Full Name : ")
    age = int(input("Enter Your Age : "))
    nic = input("Enter Your NIC : ")
    if age >= 18:
        print("Our Available Three Wheelers : ")
        print(A_Three_wheelers)
        removeThreewheelers = input("\n\nWhich Three Wheeler do you want to Hire?\nEnter Three Wheeler Name -")
        A_Three_wheelers.remove(removeThreewheelers)
        B_Three_wheelers.insert(0, removeThreewheelers)
        print(fname + "," + removeThreewheelers + " is hired successfully")
        print("\n\nNow Our Available Three Wheelers : ")
        print(A_Three_wheelers)
        Hire_Backmenu()

    else:
        print("Sorry.You Can't Hire A Vehicle!")
        Welcomemenu()

def Hire_Lorry():
    fname = input("Enter Your Full Name : ")
    age = int(input("Enter Your Age : "))
    nic = input("Enter Your NIC : ")
    if age >= 18:
        print("Our Available Lorries : ")
        print(A_Lorries)
        removeLorries = input("\n\nWhich lorry do you want to Hire?\nEnter Lorry Name -")
        A_Lorries.remove(removeLorries)
        B_Lorries.insert(0, removeLorries)
        print(fname + "," + removeLorries + " is hired successfully")
        print("\n\nNow Our Available Lorries : ")
        print(A_Lorries)
        Hire_Backmenu()

    else:
        print("Sorry.You Can't Hire A Vehicle!")
        Welcomemenu()

def Hire_Trucks():
    fname = input("Enter Your Full Name : ")
    age = int(input("Enter Your Age : "))
    nic = input("Enter Your NIC : ")
    if age >= 18:
        print("Our Available Trucks : ")
        print(A_Trucks)
        removeTrucks = input("\n\nWhich truck do you want to Hire?\nEnter Truck Name -")
        A_Trucks.remove(removeTrucks)
        B_Trucks.insert(0, removeTrucks)
        print(fname + "," + removeTrucks + " is hired successfully")
        print("\n\nNow Our Available Trucks : ")
        print(A_Trucks)
        Hire_Backmenu()

    else:
        print("Sorry.You Can't Hire A Vehicle!")
        Welcomemenu()

def Hire_Backmenu():
    print("\n92.Back to the main menu\n93.Back to the Categories\n98.Release This Vehicle")
    hireback_num=int(input("\n\nPlease Enter Your Number - "))
    if hireback_num==92:
        Customer_Mainmenu()
    elif hireback_num==93:
        Categories()
    elif hireback_num==98:
        Release_Vehicle()
    else:
        print("Invalid Number!")
        Hire_Backmenu()



# RELEASE VEHICLES
def Release_AC_Car():
    print("Our Available AC Cars : ")
    print(A_AC_cars)
    releaseACcars=input("\n\nWhich car do you want to release?\nEnter Car Name -")
    A_AC_cars.insert(0, releaseACcars)
    B_AC_cars.remove(releaseACcars)
    print(name+","+releaseACcars+"is released successfully ")
    print("\n\nNow Our Available AC Cars : ")
    print(A_AC_cars)
    Release_Vehi_Back()

def Release_NonAC_Car():
    print("Our Available NonAC Cars : ")
    print(A_NonAC_cars)
    releaseNonACcars=input("\n\nWhich car do you want to release?\nEnter Car Name -")
    A_NonAC_cars.insert(0, releaseNonACcars)
    B_NonAC_cars.remove(releaseNonACcars)
    print(name + "," + releaseNonACcars + "is released successfully ")
    print("\n\nNow Our Available NonAC Cars : ")
    print(A_NonAC_cars)
    Release_Vehi_Back()

def Release_AC_Van():
    print("Our Available AC Vans : ")
    print(A_AC_vans)
    releaseACVans=input("\n\nWhich van do you want to release?\nEnter Van Name -")
    A_AC_vans.insert(0, releaseACVans)
    B_AC_vans.remove(releaseACVans)
    print(name + "," + releaseACVans + "is released successfully ")
    print("\n\nNow Our Available AC Vans : ")
    print(A_AC_vans)
    Release_Vehi_Back()

def Release_NonAC_Van():
    print("Our Available NonAC Vans : ")
    print(A_NonAC_vans)
    releaseNonACvans=input("\n\nWhich van do you want to release?\nEnter Van Name -")
    A_NonAC_vans.insert(0, releaseNonACvans)
    B_NonAC_vans.remove(releaseNonACvans)
    print(name + "," + releaseNonACvans + "is released successfully ")
    print("\n\nNow Our Available NonAC Vans : ")
    print(A_NonAC_vans)
    Release_Vehi_Back()

def Release_Three_Wheeler():
    print("Our Available Three Wheelers : ")
    print(A_Three_wheelers)
    releaseThreewheelers=input("\n\nWhich Three Wheeler do you want to release?\nEnter Three Wheeler Name -")
    A_Three_wheelers.insert(0, releaseThreewheelers)
    B_Three_wheelers.remove(releaseThreewheelers)
    print(name + "," + releaseThreewheelers + "is released successfully ")
    print("\n\nNow Our Available Three Wheelers : ")
    print(A_Three_wheelers)
    Release_Vehi_Back()

def Release_Lorry():
    print("Our Available Lorries : ")
    print(A_Lorries)
    releaseLorries=input("\n\nWhich lorry do you want to release?\nEnter Lorry Name -")
    A_Lorries.insert(0, releaseLorries)
    B_Lorries.remove(releaseLorries)
    print(name + "," + releaseLorries + "is released successfully ")
    print("\n\nNow Our Available Lorries : ")
    print(A_Lorries)
    Release_Vehi_Back()

def Release_Trucks():
    print("Our Available Trucks : ")
    print(A_Trucks)
    releaseTrucks=input("\n\nWhich truck do you want to release?\nEnter Truck Name -")
    A_Trucks.insert(0, releaseTrucks)
    B_Trucks.remove(releaseTrucks)
    print(name + "," + releaseTrucks + "is released successfully ")
    print("\n\snNow Our Available Trucks : ")
    print(A_Trucks)
    Release_Vehi_Back()

def Release_Vehicle():
    print("\n\nWhich vehicle do you want to release?\n  1.AC Cars\n  2.NonAC Cars\n  3.AC vans\n  4.NonAC Vans\n  5.Three Wheelers\n  6.Lorries\n  7.Trucks")
    releaseVehicle=int(input("Enter Your Number - "))
    if releaseVehicle==1:
        Release_AC_Car()
    elif releaseVehicle==2:
        Release_NonAC_Car()
    elif releaseVehicle==3:
        Release_AC_Van()
    elif releaseVehicle==4:
        Release_NonAC_Van()
    elif releaseVehicle==5:
        Release_Three_Wheeler()
    elif releaseVehicle==6:
        Release_Lorry()
    elif releaseVehicle==7:
        Release_Trucks()
    else:
        print("Invalid Number")
        Release_Vehicle()

def Release_Vehi_Back():
    print("\n\n92.Back to the main menu\n94.Back to the release vehicle menu")
    relvehi_back_num=int(input("Enter Your Number - "))
    if relvehi_back_num==92:
        Customer_Mainmenu()
    elif relvehi_back_num==97:
        Release_Vehicle()
    else:
        print("Invalid number")
        Release_Vehi_Back()


# VIEW CATEGORIES
def Categories():
    print("1.Cars\n2.Vans\n3.Three Wheelers\n4.Lorries\n5.Trucks")
    vehi_num= int(input("\n\nPlease Enter Your Number - "))
    if vehi_num==1:
        top1="***CAR***"
        top1_cen=top1.center(70)
        print(top1_cen)
        print("* The maximum number of passengers - 3 & 4")
        print("A/C\n  1.Mazda Axela\n  2.Honda Civic\n  3.Toyota Premio")
        print("\nNon A/C\n  4.TATA Mini Cab\n  5.Suzuki Alto")
        print("Do you want to hire a AC Car or NonAC Car?\n\n  1.AC Car\n  2.NonAC Car\n  3.Back to main menu")
        hireInput=int(input("Enter Your Number - "))
        if hireInput==1:
            Hire_AC_Cars()
        elif hireInput==2:
            Hire_NonAC_Cars()
        elif hireInput==3:
            Mainmenu()
        else:
            print("Invalid Number!")
            Categories()


    elif vehi_num==2:
        top2="***VAN***"
        top2_cen=top2.center(70)
        print(top2_cen)
        print("* The maximum number of passengers - 6 & 8")
        print("A/C\n  1.Toyota KDH\n  2.Nissan Caravan\n  3.Toyota Noah")
        print("\nNon A/C\n  4.Toyota Litease\n  5.Nissan Vanette")
        print("Do you want to hire a AC Van or NonAC Van?\n\n  1.AC Van\n  2.NonAC Van\n  3.Back to main menu")
        hireInputcvan = int(input("Enter Your Number - "))
        if hireInputcvan == 1:
            Hire_AC_Vans()
        elif hireInputcvan == 2:
            Hire_NonAC_Vans()
        elif hireInputcvan == 3:
            Mainmenu()
        else:
            print("Invalid Number!")
            Categories()

    elif vehi_num==3:
        top3="***Three Wheeler***"
        top3_cen=top3.center(70)
        print(top3_cen)
        print("* The maximum number of passengers - 3")
        print("1.Bajaj\n2.TVS King\n3.Piaggio")
        print("Do you want to hire a Three wheeler?\n\n 1.Yes\n  2.No")
        hInputthree=input("Enter youe number - ")
        if hInputthree==1:
            Hire_Three_Wheeler()
        elif hInputthree==2:
            Mainmenu()
        else:
            print("Invalid Number!")
            Categories()

    elif vehi_num==4:
        top4="***LORRY***"
        top4_cen=top4.center(70)
        print(top4_cen)
        print("* Max load and size - 2500kg and 3500kg")
        print("1.Toyota\n2.Nissan\n3.Fuso\n4.Isuzu")
        print("Do you want to hire a Lorry?\n\n 1.Yes\n  2.No")
        hInputlorry = input("Enter youe number - ")
        if hInputlorry == 1:
            Hire_Lorry()
        elif hInputlorry == 2:
            Mainmenu()
        else:
            print("Invalid Number!")
            Categories()

    elif vehi_num == 5:
        top5 = "***TRUCK***"
        top5_cen = top5.center(70)
        print(top5_cen)
        print("* Size – 7 ft and 12 ft")
        print("1.Toyota\n2.Nissan\n3.Fuso\n4.Isuzu\n5.MAN")
        print("Do you want to hire a Truck?\n\n 1.Yes\n  2.No")
        hInputtruck = input("Enter youe number - ")
        if hInputtruck == 1:
            Hire_Trucks()
        elif hInputtruck == 2:
            Mainmenu()
        else:
            print("Invalid Number!")
            Categories()

    else:
        print("Invalid Request!")
    Cus_Backmenu()


# MAIN MENUS
def Mainmenu():
    print("* Please go through the following menu.")
    print("1.Vehicle Categories\n2.Add a Vehicle\n3.Remove a Vehicle\n4.Hire a Vehicle\n5.Release a Vehicle")
    menu_num=int(input("\n\nPlease  Enter Your Number - "))
    if menu_num==1:
        Categories()
    elif menu_num==2:
        Add_Vehicle()
    elif menu_num==3:
        Remove_Vehicle()
    elif menu_num==4:
        Categories()
    elif menu_num==5:
        Release_Vehicle()
    else:
        print("Invalid Number!")
        Mainmenu()

def Customer_Mainmenu():
    print("* Please go through the following menu.")
    print("1.Vehicle Categories\n2.Hire a Vehicle\n3.Release a Vehicle")
    cusmenu_num = int(input("\n\nPlease  Enter Your Number - "))
    if cusmenu_num == 1:
        Categories()
    elif cusmenu_num == 2:
        Categories()
    elif cusmenu_num == 3:
        Release_Vehicle()
    else:
        print("Invalid Number!")
        Customer_Mainmenu()


# BACK MENUS
def Backmenu():
    print("\n92.Back to the main menu\n93.Back to the Categories")
    back_num=int(input("\n\nPlease Enter Your Number - "))
    if back_num==92:
        Mainmenu()
    elif back_num==93:
        Categories()
    else:
        print("Invalid Number!")
        Backmenu()

def Cus_Backmenu():
    print("\n92.Back to the main menu\n93.Back to the Categories")
    back_num = int(input("\n\nPlease Enter Your Number - "))
    if back_num == 92:
        Customer_Mainmenu()
    elif back_num == 93:
        Categories()
    else:
        print("Invalid Number!")
        Backmenu()


# WECOME MENU
def Welcomemenu():
    print("Who are you?\n  1.A customer\n  2.An admin")
    Welcome_num=int(input("Enter your number - "))
    if Welcome_num==1:
        Customer_Mainmenu()
    elif Welcome_num==2:
        Mainmenu()
    else:
        print("Invalid number!")
        Welcomemenu()


# END
def End():
    quit()


# PROGRAM
Welcomemenu()
End()






