import mysql.connector as p
from users import login
from users import register
from Appoitments import Book
from Appoitments import view
from Appoitments import delete

con=p.connect(host="localhost",user="root",password="test",port=8000,database="CityHospital")
cur=con.cursor()

def service():
        print(f"*****{login.cookie()} , Welcome To The City Hospital*****\n")
        ask=input("1)Book An Appointment \n2)View An Appoitment \n 3)Delete And Appoitment\n")
        if(ask=="1"):
            Book.book()
        elif(ask=="2"):
            view.view()
        elif(ask=="3"):
            delete.delete()
            
def verify():
    return login.login()


    
print("*****Welcome To The City Hospital*****\n")
ask=input("1)Login\n2)Register\n")

if(ask=="1"):
    z=verify()
    if(z==True):
        service()
elif(ask=="2"):
    register.register()
    z=verify()
    if(z==True):
        service()