import os
os.system("cls")
from colorama import Fore
import time
from tqdm import tqdm
for i in tqdm(range(100),colour='YELLOW'):
    time.sleep(0.02)
    
while True:
    os.system("cls")
    print(Fore.MAGENTA)
    print("                           *****************************************************")
    print("                           ** >>>>>>>>>>> LIBRARY MANAGMENT SYSTEM <<<<<<<<<< **")
    print("                           *****************************************************")
    print("                           **option 1 to Register the customer                **")
    print("                           **option 2 to See available books in library       **")
    print("                           **option 3 to Add new book data                    **")
    print("                           **option 4 to See customer record                  **")
    print("                           **option 5 to Remove customer record               **")
    print("                           **option 6 to Read facilitise                      **")
    print("                           **option 7 to Exit                                 **")
    print("                           *****************************************************")
    a=int(input("enter your option: "))

    if a==1:
        os.system("cls")        
        print(Fore.RED)
        class regeristration:
            def __init__(self,name,cnic,PHN,address,issuedate,returndate,price):
                self.name = name
                self.__cnic = cnic
                self.__PHN = PHN
                self.__address = address
                self.issuedate = issuedate
                self.returndate = returndate
                self.price = price
            def display_data(self):
                print("**************************************************")
                print("*************Customer saved record****************")
                print("**************************************************")
                print("**Name of customer: " + self.name )
                print("**CNIC NO:          " + self.__cnic)
                print("**Phone Number:     " + self.__PHN)
                print("**Address:          " + self.__address)
                print("**Issue date:       " + self.issuedate)
                print("**Rutern date:      " + self.returndate)
                print("**Price of book:    " + self.price)
                print("**************************************************")
        name = input("Please enter your name:")
        PHN = input("Enter your phone number")
        cnic = input("Enter your cnic")
        address = input("Enter your address")
        issuedate = input("Enter your issue date")
        returndate = input("Enter your return date")
        price = input("Enter the price of book")

        file = open(name,"w")
        file.write("***********************************************\n")
        file.write("**>>>>>>>>>>>>>>>(Customer detail)<<<<<<<<<<<**\n")
        file.write("***********************************************\n")
        file.write("**Name of customer:  " + name + "\n")
        file.write("**Phone number:      " + PHN + "\n")
        file.write("**CNIC :             " + cnic + "\n")
        file.write("**Address:           " + address + "\n")
        file.write("**issue date:        " + issuedate + "\n")
        file.write("**return date:       " + returndate + "\n")
        file.write("**price of book:     " + price+ "\n")
        file.write("***********************************************\n")
        file.close()
            
        objectcustomer=regeristration(name,PHN,cnic,address,issuedate,returndate,price)
        os.system("cls")
        objectcustomer.display_data()
        print("your registration have been successfully stored")

    
    elif a==2:
        os.system("cls")
        print(Fore.BLUE)
        class read:
            try:
                print("Enter a to read Art books data")
                print("Enter s to read Science book data")
                a=input("enter coustomer file name to read")
                os.system("cls")
                if a=='s':
                    f=open("Science.txt","r")
                    print(f.read())
                elif a=='a':
                    f=open("Art.txt","r")
                    print(f.read())
                else:
                    print("invalid information")
            except:
                print("invalid information...enter small a or s")
            finally:
                print("thanks you for come to")
                
    elif a==3:
        os.system("cls")
        print(Fore.MAGENTA)
        class book:
            def science_book(self,bookname,pub,issn,price):
                self.bookname=bookname
                self.pub=pub
                self.issn=issn
                self.price=price
                f = open("Science.txt","a")
                f.write("****************************************************\n")
                f.write("**>>>>>>>>>>>>>>>> Science book <<<<<<<<<<<<<<<<<<**\n")
                f.write("****************************************************\n")
                f.write("** Name of book:     " + self.bookname + "\n")
                f.write("** Name of publisher:" + self.pub +  " \n")
                f.write("** ISSN of book:     " + self.issn + " \n")
                f.write("** Price of book:    " + self.price +" \n")
                f.write("****************************************************\n")
                f.close()
        class others(book):
            def other_data(self,bookname,pub,issn,price):
                self.bookname=bookname
                self.pub=pub
                self.issn=issn
                self.price=price
                f = open("Art.txt","a")
                f.write("****************************************************\n")
                f.write("**>>>>>>>>>>>>>>>>>> Art book <<<<<<<<<<<<<<<<<<<<**\n")
                f.write("****************************************************\n")
                f.write("** Name of book:     " + self.bookname + "\n")
                f.write("** Name of publisher:" + self.pub +  " \n")
                f.write("** ISSN of book:     " + self.issn + " \n")
                f.write("** Price of book:    " + self.price +" \n")
                f.write("****************************************************\n")
                f.close()
        a=input("Enter name of a book: ")
        b=input("Enter publisher name: ")
        c=input("Enter ISSN of a book: ")
        d=input("Enter price of a book: ") 
        obj=others()
        print("option 1 to store book in science books inventory")
        print("option 2 to store book in Art books inventory")
        g=int(input("Enter your option:  \n"))
        if g==1:
            obj.science_book(a,b,c,d)
        elif g==2:
            obj.other_data(a,b,c,d)    
        else:
            print("invalid option")
               

    elif a==4:
        os.system("cls")
        print(Fore.MAGENTA)
        class read_regeristration:
                try:
                    x = input("enter customer file name to read")
                    file = open(x,"r")
                    print(file.read())
                except:
                    print("file is not available")
                else:
                    file.close()
                    print("Thank you")
                    
    elif a==5:
        os.system("cls")
        print(Fore.BLACK)
        class delete_record:
                try:
                    x = input("enter customer file name for verification of real person")
                    file = open(x,"r")
                    print(file.read())
                except:
                    print("file is not available")
                else:
                    file.close()
                    print("thank you")
                delete = input("Enter customer file name again to delete record")
                try:
                    os.remove(delete)
                except OSError:
                    print("Something went wrong")
                finally:
                    print("Your work is done")
    elif a==6:
        os.system("cls")
        print(Fore.GREEN)
        class facilities:
            print("We are giving you a Silent Environment in the library")
            print("We are providing you a Good sitting style")
            print("We are providing you a Fresh Environment ")
            print("We are providing Air conditioner")
            print("We are proving a Canteen you can take anything out of there")
                    
    elif a==7:
        os.system("cls")
        print("Thanks for visiting my library")
        break        
    else:
        os.system("cls")
        print("invalid information")  
    print(Fore.WHITE)
    c=input("enter 0 to got to main manue \n")
    if c==0:
        break
    else:
        continue         
   