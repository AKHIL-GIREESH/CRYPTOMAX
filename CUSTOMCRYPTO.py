#Generating userID
def userID_generator():
    from random import randint , choice , shuffle
    userID = []
    ID = ""
    noofuppercasechars = randint(3,5)
    for i in range(noofuppercasechars):
        uppercasechar = randint(65,90)
        userID.append(chr(uppercasechar))

    nooflowercasechars = randint(5,10)
    for i in range(nooflowercasechars):
        lowercasechar = randint(97,122)
        userID.append(chr(lowercasechar))

    noofdigits = randint(5,10)
    for i in range(noofdigits):
        digit = randint(0,100)
        userID.append(str(digit))

    x = ["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*"]
    noofspecialchars = randint(2,4)
    for i in range(noofspecialchars):
        specialchar = choice(x)
        userID.append(specialchar)

    shuffle(userID)
    for i in userID:
        ID+=i
    return ID

#--------------------------------------------------------------------------------------------------------------------------------------


#Adding data
def add_user(l):
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
    myobj = mydb.cursor()
    myobj.execute("SHOW TABLES")
    check0 = False
    for i in myobj:
        if i == ('users',):
            check0 = True
            break
    if check0 == False:
        myobj.execute("CREATE TABLE USERS(userid varchar(50) Primary key ,username varchar(20) Unique,password varchar(30),balance integer)")
    print("1. Register")
    print("2. Login")
    choice = int(input("Enter the choice:"))
    print()
    check1 = True
    if choice == 1:
        while True:
            username = input("Enter the username:")
            password = input("Enter the password:")
            balance = (input("Enter the amount in rupees:"))/10_000
            check1 = True
            myobj.execute("SELECT username from users")
            variable0 = myobj.fetchall()
            for i in variable0:
                if i[0] == username:
                    check1 = False
            if check1 == True:
                l.append([userID_generator(),username,password,balance])
                command = "INSERT INTO users VALUES(%s,%s,%s,%s)"
                myobj.executemany(command,l)
                mydb.commit()
                break
            else:
                print("user ID is already taken")

        myobj.execute("SELECT * FROM users")
        details = myobj.fetchall()
        for i in details:
            print(i)

    elif choice == 2:
        while True:
            name = input("Enter the username:")
            password = input("Enter the password:")
            myobj.execute("SELECT username,password from users")
            variable1 = myobj.fetchall()
            for i in variable1:
                if i == (name,password):
                    check1 == False
            if check1 == True:
                break
            else:
                print("user doesn't exist")
    
l = []
add_user(l)


#--------------------------------------------------------------------------------------------------------------------------------------


#Renaming
def rename_user():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
    myobj = mydb.cursor()
    while True:
        nameOG = input("Enter the current username:")
        password = input("Enter the current password:")
        check2 = False
        myobj.execute("SELECT username,password from users")
        variable2 = myobj.fetchall()
        for i in variable2:
            if i[0] == nameOG and i[1] == password :
                check2 = True
        if check2 == True:
            name = input("Enter the new username:")
            l = [name,password,nameOG]
            command = "UPDATE users SET username = %s WHERE password = %s AND username =%s"
            myobj.execute(command,l)
            mydb.commit()
        else:
            print("incorrect user ID or password")
        
    myobj.execute("SELECT * FROM users")
    details = myobj.fetchall()
    for i in details:
        print(i)
    
    
rename_user()

#--------------------------------------------------------------------------------------------------------------------------------------


#Changing password
def change_password():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
    myobj = mydb.cursor()
    name  = input("Enter the current username:")
    passwordOG = input("Enter the current password:")
    password = input("Enter the new password:")
    check3 = False
    myobj.execute("SELECT username,password from users")
    variable3 = myobj.fetchall()
    for i in variable3:
        if i[0] == name and i[1] == passwordOG :
            check3 = True
    if check3 == True:
        password = input("Enter the new username:")
        l = [password,passwordOG,name]
        command = "UPDATE users SET password = %s WHERE password = %s AND username =%s"
        myobj.execute(command,l)
        mydb.commit()
    else:
        print("incorrect user ID or password")    

    myobj.execute("SELECT * FROM users")
    details = myobj.fetchall()
    for i in details:
        print(i)
change_password()

#--------------------------------------------------------------------------------------------------------------------------------------


#Deleting user
def delete_user():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
    myobj = mydb.cursor()
    username = input("Enter the username:")
    password = input("Enter the password:")
    check4 = False
    myobj.execute("SELECT username,password from users")
    variable4 = myobj.fetchall()
    for i in variable4:
        if i[0] == nameOG and i[1] == password :
            check4 = True
    if check2 == True:
        l = [username,password]
        command = "DELETE FROM users WHERE username = %s AND password = %s"
        myobj.execute(command,l)
        mydb.commit()
    else:
        print("incorrect user ID or password")    

    myobj.execute("SELECT * FROM users")
    details = myobj.fetchall()
    for i in details:
        print(i)
delete_user()


#--------------------------------------------------------------------------------------------------------------------------------------

def conversion():
    x = int(input("Enter the no.of coins in rupees:"))
    return x*100000

#--------------------------------------------------------------------------------------------------------------------------------------

def RCGENERATOR(x):
    x = x.lower()
    rc = ""
    for i in x:
        if i.isalpha() == True:
            rc += str(ord(i) - 80)
            
        elif i.isnumeric() == True:
            rc += str(int(i) + 50)
    return f"{int(rc):o}"

#--------------------------------------------------------------------------------------------------------------------------------------


def find_user(x):
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
    myobj = mydb.cursor()
    myobj.execute("SELECT username FROM users ")
    variable2 = myobj.fetchall()
    for i in variable2:
        if i == (x,):
            return True
        return False


#--------------------------------------------------------------------------------------------------------------------------------------

def ledger(x,y,z):
    with open("ledger.csv","a",newline = " ") as f:
        append = csv.writer(f,delimiter = '')
        append.writerow([x,y,z])


#--------------------------------------------------------------------------------------------------------------------------------------

def transactions():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
    myobj = mydb.cursor()

    from_user = input("Enter the userID:")
    to_user = input("Enter the username of the reciever:")
    if find_user(to_user):
        amt = int(input("Enter the amount to be transferred"))
        myobj.execute("UPDATE users SET amount = amount - %d WHERE user =%s"%(amt , from_user))
        mydb.commit()
        myobj.execute("UPDATE users SET amount = amount + %d WHERE user =%s"%(amt , to_user))
        mydb.commit()
        ledger(from_user,to_user,amt)
    else:
        print("user does not exist")


#--------------------------------------------------------------------------------------------------------------------------------------            
                          
def blockchain():
    with open("ledger.csv") as f:
       x = []
       reading = csv.reader(f)
       for i in reading:
           x.append(i)
    megablock = {}
    fristtrans = True

    for i in range(len(x)):
        if fristtrans == True:
            rc = RCGENERATOR(x[i])
            megablock[rc] = ["BEGINNING",x[i]]
            prevrc = rc
            fristtrans = False
        else:
            rc = RCGENERATOR(x[i])
            megablock[str(int(prevrc) + int(rc))] = [prevrc,x[i]]
            prevrc = str(int(prevrc) + int(rc)) 
    print(megablock) 





