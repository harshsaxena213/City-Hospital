import mysql.connector as p
import smtplib
from email.message import EmailMessage 
import random

con=p.connect(host="localhost",user="root",password="test",port=8000,database="CityHospital")
cur=con.cursor()


def otp_validation():
    otp=""
    for i in range(4):
        otp+=str(random.randint(0,9))

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("test@gmail.com","test")
    
    query="select email from users where usernmae='{}'".format(usernmae)
    cur.execute(query)
    temp=cur.fetchall()
    user_email=temp[0][0]
    
    msg=EmailMessage()
    msg["Subject"]="Dear"+usernmae+"Your Otp For Login Is Here"
    msg["From"]="test"
    msg["To"]=user_email
    msg.set_content(f"Dear {usernmae} Your Otp To Login Is {otp} Don't Share This Otp To Anyone For Security Reasons")
    server.send_message(msg)
    
    validate=input("Please Enter The Otp Sent On Your Register Email Id")
    if(validate==otp):
        return True
    else:
        exit

def login():
    
    print("****Login****\n")
    global usernmae
    usernmae=input("Please Enter Your Regitered Usernmae \n")
    password=input("Please Enter Your Password\n")
    query="select password from  users where usernmae='{}'".format(usernmae)
    cur.execute(query)
    p=cur.fetchall()
    if(p==[]):
        print("Incorrect Username\n")
        exit
    elif(p[0][0]==password):
        z=otp_validation()
        if(z)==True:
            return True
        else:
            print("Invalid Otp")
    else:
        print("Incorrect Password\n")

def cookie():
    return usernmae