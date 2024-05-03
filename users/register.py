import mysql.connector as p


con=p.connect(host="localhost",user="root",password="test",port=8000,database="CityHospital")
cur=con.cursor()

def register():
    print("****Register*****\n")
    username_new=input("Enter The New Username For Your Account\n")
    password_new=input(f"Enter The Password For {username_new} \n")
    query_check_avail="select password from users where usernmae='{}'".format(username_new)
    cur.execute(query_check_avail)
    z=cur.fetchall()
    if(z!=[]):
        print("The Entered Username Is Not Available Please Enter Any Other Username")
    else:
        query_insert="insert into users values('{}','{}')".format(username_new,password_new)
        cur.execute(query_insert)
        con.commit()
        print(f"You Are Successfully Registered Yourself With City Hospital\nYour Credentials Are\nUsername :- {username_new}\nPassword :-{password_new}")
    
