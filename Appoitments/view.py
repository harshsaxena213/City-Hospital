import mysql.connector as p
import random
con=p.connect(host="localhost",user="root",password="test",port=8000,database="CityHospital")
cur=con.cursor()

def view():
    global user 
    user=input("Enter The Username")
    query_view="select doc_name,D from appointment where username='{}'".format(user)
    cur.execute(query_view)
    p=cur.fetchall()
    print(f"You Have Fixed A Appointment On {p[0][0]} With Doctor {p[0][1]}")
    
