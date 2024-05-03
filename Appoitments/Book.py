import mysql.connector as p
import random
con=p.connect(host="localhost",user="root",password="test",port=8000,database="CityHospital")
cur=con.cursor()

def book():
    global d
    global user
    user=input("Please Enter Your Usernmae")
    d=input(f"Enter {user} The Date For Appoitment ! Please Enter In DD/MM/YYYY Foramte\n")
    query_of_doc="select * from doctors"
    cur.execute(query_of_doc)
    doc_name=cur.fetchall()
    radn=random.randint(0,6)
    temp=doc_name[radn]
    global use_doc
    use_doc=temp[0]
    print(f"Hey Your Appoitment Is Fixed With The Doctor {use_doc} On {d}")
    intodb()
    exit()

def intodb():
    query_into_db="insert into appointment values('{}','{}','{}')".format(user,d,use_doc)
    cur.execute(query_into_db)
    con.commit()
    
    
