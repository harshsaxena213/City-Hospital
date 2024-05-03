import mysql.connector as p

con=p.connect(host="localhost",user="root",password="test",port=8000,database="CityHospital")
cur=con.cursor()


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
        print("Looged In\n")
        return True
    else:
        print("Incorrect Password\n")

def cookie():
    return usernmae