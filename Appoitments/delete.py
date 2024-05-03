import mysql.connector as p
import random
con=p.connect(host="localhost",user="root",password="test",port=8000,database="CityHospital")
cur=con.cursor()

def delete():
    global user 
    user=input("Enter The Username")
    query_view="select doc_name,D from appointment where username='{}'".format(user)
    cur.execute(query_view)
    p=cur.fetchall()
    query_del="delete from appointment where username='{}'".format(user)
    cur.execute(query_del)
    con.commit()
    print(f"Your Appointment With Doctor {p[0][1]} On {p[0][0]} Is Now Cancelled ")
    