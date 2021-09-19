from tkinter import *
from tkinter import messagebox

root_splash_screen = Tk()

root_splash_screen.overrideredirect(True)

canvas = Canvas(width = 640 , height = 640)
canvas.pack()

photo = PhotoImage(file = 'F:\Wallpapers\CRYPTOMAX.png')

canvas.create_image(0,0, image=photo , anchor = NW)

def main():
    root_splash_screen.destroy()
    root  = Tk()
    root.geometry("1920x1080")
    root.configure(bg = "white")

    upperline1 = Label(root,text = "",bg = "#E00000",padx = 1920 , pady = 60)
    upperline1.pack()
    heading=Label(root,text="CRYPTOMAX",bg = "white")
    heading.config(font=("Courier",50))
    heading.pack()


    #DARK THEME


    def pg3d():
        root1d = Tk()
        root1d.geometry("1920x1080")
        root1d.configure(bg = "#202020")

        upperline2d = Label(root1d,text = "",bg = "#CF780A",padx = 1920 , pady = 60)
        upperline2d.pack()

        L10d = Label(root1d , text = "       ",bg = "#202020")
        L10d.pack()

        def viewprofiled():
            root1d.withdraw()
            root_vpd = Tk()
            root_vpd.geometry("1920x1080")
            root_vpd.configure(bg = "#202020")
            pass
        
            def pro_homed():
                root_vpd.withdraw()
                root1d.deiconify()

            global l    
            profile_usernamed = Label(root_vpd , text = l[0][1] , bg = "#CF780A",fg = "#202020")
            profile_usernamed.pack()

            pl1d = Label(root_vpd , text = "                " , bg = "#CF780A",fg = "#484848")
            pl1d.pack()
            
            profile_passwordd = Label(root_vpd , text = l[0][2] , bg = "#CF780A",fg = "#202020")
            profile_passwordd.pack()

            pl2d = Label(root_vpd , text = "                " , bg = "#CF780A",fg = "#202020")
            pl2d.pack()

            profile_balanced = Label(root_vpd , text = l[0][3] , bg = "#CF780A",fg = "#202020")
            profile_balanced.pack()

            pl3d = Label(root_vpd , text = "                " , bg = "#CF780A",fg = "#202020")
            pl3d.pack()

            profile_encryptedd = Label(root_vpd , text = l[0][0] , bg = "#CF780A",fg = "#202020")
            profile_encryptedd.pack()

            pl4d = Label(root_vpd , text = "                " , bg = "#CF780A",fg = "#202020")
            pl4d.pack()
                    
            profile_home_buttond = Button(root_vpd,text = "Home",padx =50, pady = 25,bg = "#CF780A",fg = "#202020" ,command = pro_homed)
            profile_home_buttond.pack()

        Profile_buttond = Button(root1d,text = "Profile",padx =50, pady = 25,bg = "#CF780A",fg = "#202020" ,command = viewprofiled)
        Profile_buttond.pack()

        L3d = Label(root1d, text = "       ",bg = "#202020")
        L3d.pack()

        def transactiond():
            root1d.withdraw()
            root_trd = Tk()
            root_trd.geometry("1920x1080")
            root_trd.configure(bg = "#202020")
            pass
            def tran_homed():
                root_trd.withdraw()
                root1d.deiconify()
                
            transaction_home_buttond = Button(root_trd,text = "Home",padx =50, pady = 25,bg = "#CF780A",fg = "#202020" ,command = tran_homed)
            transaction_home_buttond.pack()
        Transaction_buttond = Button(root1d,text = "Transaction",padx =50, pady = 25,bg = "#CF780A",fg = "#202020" ,command = transactiond)
        Transaction_buttond.pack()
        L4d = Label(root1d , text = "       ",bg = "#202020")
        L4d.pack()

        def ledgerd():
            root1d.withdraw()
            root_ledd = Tk()
            root_ledd.geometry("1920x1080")
            root_ledd.configure(bg = "#202020")
            pass
            def led_homed():
                root_ledd.withdraw()
                root1d.deiconify()

            led_home_buttond = Button(root_ledd,text = "Home",padx =50, pady = 25,bg = "#CF780A",fg = "#202020" ,command = led_homed)
            led_home_buttond.pack()
        Ledger_buttond = Button(root1d,text = "Public Ledger" ,padx =50, pady = 25,bg = "#CF780A",fg = "#202020" , command = ledgerd)
        Ledger_buttond.pack()
        L5d = Label(root1d , text = "       ",bg = "#202020")
        L5d.pack()

        def blockchaind():
            root1d.withdraw()
            root_blcd = Tk()
            root_blcd.geometry("1920x1080")
            root_blcd.configure(bg = "#202020")
            pass
            def mining_homed():
                root_blcd.withdraw()
                root1d.deiconify()

            mining_home_buttond = Button(root_blcd,text = "Home",padx =50, pady = 25,bg = "#CF780A",fg = "#202020" ,command = mining_homed)
            mining_home_buttond.pack()
        Blockchain_buttond = Button(root1d,text = "Mining",padx =50, pady = 25,bg = "#CF780A",fg = "#202020" ,command = blockchaind)
        Blockchain_buttond.pack()
        L6d = Label(root1d , text = "       ",bg = "#202020")
        L6d.pack()

        def conversiond():
            root1d.withdraw()
            root_cond = Tk()
            root_cond.geometry("1920x1080")
            root_cond.configure(bg = "#202020")
            pass
            def con_homed():
                root_cond.withdraw()
                root1d.deiconify()

            conversion_entryd = Entry(root_cond , width = 25 , bg = "#484848",fg = "white")
            conversion_entryd.pack()

            def convertd():
                convert_buttond.destroy()
                x = int(conversion_entryd.get())//10
                conversion_labeld = Label(root_cond ,text = x)
                conversion_labeld.pack()
                convert_labeld.insert(0,"Enter the amount in rupees",fg="white")

            convert_buttond = Button(root_cond , text = "Convert",padx =25, pady = 15,bg = "#CF780A",fg = "#202020" ,command =convertd)
            convert_buttond.pack()
            

            L13d = Label(root_cond, text = "       ",bg = "#202020")
            L13d.pack()

            con_home_buttond = Button(root_cond,text = "Home",padx =50, pady = 25,bg = "#CF780A",fg = "#202020" ,command = con_homed)
            con_home_buttond.pack(side = BOTTOM)
        Conversion_buttond = Button(root1d,text = "Conversion",padx =50, pady = 25,bg = "#CF780A",fg = "#202020" ,command = conversiond)
        Conversion_buttond.pack()
        L7d = Label(root1d , text = "       ",bg = "#202020")
        L7d.pack()

        def Light_theme():
            root1d.withdraw()
            pg3()

        Light_theme_button = Button(root1d, text = "LIGHT MODE", padx =50, pady = 25,bg = "#CF780A",fg = "#202020" , command=Light_theme)
        Light_theme_button.pack()
        L11d = Label(root1d , text = "       ",bg = "#202020")
        L11d.pack()
        
        def Back_to_homed():
            root1d.destroy()
            root.deiconify()
            
        Home_backd = Button(root1d,text="HOME" , padx =50, pady = 25,bg = "#CF780A",fg = "#202020" , command=Back_to_homed)
        Home_backd.pack()

    #--------------------------------------------------------------------------------------------------------------------------------------

    #REGULAR THEME
        
    def pg3():
        root1 = Tk()
        root1.geometry("1920x1080")
        root1.configure(bg = "white")

        upperline2 = Label(root1,text = "",bg = "#E00000",padx = 1920 , pady = 60)
        upperline2.pack()

        L10 = Label(root1 , text = "       ",bg = "white")
        L10.pack()

        def viewprofile():
            root1.withdraw()
            root_vp = Tk()
            root_vp.geometry("1920x1080")
            root_vp.configure(bg = "white")
            pass
        
            def pro_home():
                root_vp.withdraw()
                root1.deiconify()

            global l    
            profile_username = Label(root_vp , text = l[0][1] , bg = "#484848",fg = "white")
            profile_username.pack()

            pl1 = Label(root_vp , text = "                " , bg = "#484848",fg = "#484848")
            pl1.pack()
            
            profile_password = Label(root_vp , text = l[0][2] , bg = "#484848",fg = "white")
            profile_password.pack()

            pl2 = Label(root_vp , text = "                " , bg = "#484848",fg = "#484848")
            pl2.pack()

            profile_balance = Label(root_vp , text = l[0][3] , bg = "#484848",fg = "white")
            profile_balance.pack()

            pl3 = Label(root_vp , text = "                " , bg = "#484848",fg = "#484848")
            pl3.pack()

            profile_encrypted = Label(root_vp , text = l[0][0] , bg = "#484848",fg = "white")
            profile_encrypted.pack()

            pl4 = Label(root_vp , text = "                " , bg = "#484848",fg = "#484848")
            pl4.pack()

            def change_username():
                
                root_vp.withdraw()
                root_username = Tk()
                root_username.geometry("1920x1080")
                root_username.configure(bg = "white")
                
                change_username1_label = Label(root_username , text = "Enter the new username")
                change_username1.pack()
                
                change_username1 = Entry(root_username,bg = "#484848" , fg = "white")
                change_username1.pack()

                change_username2_label = Label(root_username , text = "Re-enter the new username")
                change_username2.pack()
                
                change_username2 = Entry(root_username,bg = "#484848" , fg = "white")
                change_username2.pack()

                def checking():
                    if change_username1.get() == change_username2.get():
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                        myobj = mydb.cursor()

                        global l   
                        list1 = [username1.get() , l[0][1]]
                        command = "UPDATE users SET username = %s WHERE username = %s"
                        myobj.execute(command,l)
                        mydb.commit()

                    else:
                        messagebox.showerror("Oops!", "Enter the username correctly")
                        
                checkname = Button(root_username ,bg = "#484848" , fg = "white",command = checking)
                checkname.pack()
                
            change_username_button = Button(root_vp,text = "Change Username" ,padx =50, pady = 25,bg = "#484848",fg = "white" ,command = change_username)
            change_username_button.pack()
            
            profile_home_button = Button(root_vp,text = "Home",padx =50, pady = 25,bg = "#484848",fg = "white" ,command = pro_home)
            profile_home_button.pack()

        Profile_button = Button(root1,text = "Profile",padx =50, pady = 25,bg = "#484848",fg = "white" ,command = viewprofile)
        Profile_button.pack()

        L3 = Label(root1, text = "       ",bg = "white")
        L3.pack()

        def transaction():
            root1.withdraw()
            root_tr = Tk()
            root_tr.geometry("1920x1080")
            root_tr.configure(bg = "white")
            pass

            def tran_home():
                root_tr.withdraw()
                root1.deiconify()
                
            transaction_home_button = Button(root_tr,text = "Home",padx =50, pady = 25,bg = "#484848",fg = "white" ,command = tran_home)
            transaction_home_button.pack()

        Transaction_button = Button(root1,text = "Transaction",padx =50, pady = 25,bg = "#484848",fg = "white" ,command = transaction)
        Transaction_button.pack()

        L4 = Label(root1 , text = "       ",bg = "white")
        L4.pack()

        def ledger():
            root1.withdraw()
            root_led = Tk()
            root_led.geometry("1920x1080")
            root.configure(bg = "white")
            pass
            def led_home():
                root_led.withdraw()
                root1.deiconify()

            led_home_button = Button(root_led,text = "Home",padx =50, pady = 25,bg = "#484848",fg = "white" ,command = led_home)
            led_home_button.pack()
        Ledger_button = Button(root1,text = "Public Ledger" ,padx =50, pady = 25,bg = "#484848",fg = "white" , command = ledger)
        Ledger_button.pack()
        L5 = Label(root1 , text = "       ",bg = "white")
        L5.pack()

        def blockchain():
            root1.withdraw()
            root_blc = Tk()
            root_blc.geometry("1920x1080")
            root_blc.configure(bg = "white")
            pass
            def mining_home():
                root_blc.withdraw()
                root1.deiconify()

            mining_home_button = Button(root_blc,text = "Home",padx =50, pady = 25,bg = "#484848",fg = "white" ,command = mining_home)
            mining_home_button.pack()
        Blockchain_button = Button(root1,text = "Mining",padx =50, pady = 25,bg = "#484848",fg = "white" ,command = blockchain)
        Blockchain_button.pack()
        L6 = Label(root1 , text = "       ",bg = "white")
        L6.pack()

        def conversion():
            root1.withdraw()
            root_con = Tk()
            root_con.geometry("1920x1080")
            root_con.configure(bg = "white")

            conversion_entry = Entry(root_con , width = 25 , bg = "#484848",fg = "white")
            conversion_entry.pack()
            conversion_entry.insert(0,"Enter the amount in Rupees")
            
            def convert():
                convert_button.destroy()
                x = int(conversion_entry.get())//10
                conversion_label = Label(root_con ,text = x ,width = 25 , bg = "#484848",fg = "white") 
                conversion_label.pack()
                
            
            def con_home():
                root_con.withdraw()
                root1.deiconify()

            convert_button = Button(root_con , text = "Convert",padx =25, pady = 15,bg = "#484848",fg = "white" ,command =convert)
            convert_button.pack()

            L13 = Label(root_con , text = "       ",bg = "white")
            L13.pack()
        
            con_home_button = Button(root_con,text = "Home",padx =50, pady = 25,bg = "#484848",fg = "white" ,command = con_home)
            con_home_button.pack(side = BOTTOM)
        Conversion_button = Button(root1,text = "Conversion",padx =50, pady = 25,bg = "#484848",fg = "white" ,command = conversion)
        Conversion_button.pack()
        L7 = Label(root1 , text = "       ",bg = "white")
        L7.pack()

        def Dark_theme():
            root1.withdraw()
            pg3d()

        Dark_theme_button = Button(root1, text = "DARK MODE", padx =50, pady = 25,bg = "#484848",fg = "white" , command=Dark_theme)
        Dark_theme_button.pack()
        L11 = Label(root1 , text = "       ",bg = "white")
        L11.pack()

        def Back_to_home():
            root1.destroy()
            root.deiconify()
            
        Home_back = Button(root1,text="HOME" , padx =50, pady = 25,bg = "#484848",fg = "white" , command=Back_to_home)
        Home_back.pack()
        
    #--------------------------------------------------------------------------------------------------------------------------------------

    def pg1():
        def pg2_signup():
            Sign_up_button.destroy()
            Sign_in_button.destroy()
            Exit_out.destroy()
            sign_up_label = Label(root,text = "platform to signup",bg = "white") #sign up (page 2)
            sign_up_label.pack()
            
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

            def signup_filling():
                
                #username
                username_Label_signup = Label(root , text = "USERNAME" ,bg = "#484848" , fg = "white")
                username_Label_signup.pack()
                    
                username_signup = Entry(root , bg = "#484848" , fg = "white")
                username_signup.pack()

                blankline1_signup = Label(root , text = "" , bg = "white" )
                blankline1_signup.pack()

                #password
                password_Label_signup = Label(root , text = "PASSWORD" ,bg = "#484848" , fg = "white")
                password_Label_signup.pack()
                    
                password_signup = Entry(root , bg = "#484848" , fg = "white")
                password_signup.pack()

                blankline2_signup = Label(root , text = "" , bg = "white" )
                blankline2_signup.pack()

                #account balance
                balance_Label_signup = Label(root , text = "DEPOSIT" ,bg = "#484848" , fg = "white")
                balance_Label_signup.pack()
                    
                balance_signup = Entry(root , bg = "#484848" , fg = "white")
                balance_signup.pack()
                    
                blankline3_signup = Label(root , text = "" , bg = "white" )
                blankline3_signup.pack()

                    
                def signupcheck():

                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                    myobj = mydb.cursor()
                    
                    def pg2_up_pg3():
                        sign_up_label.destroy()
                        pg2_sup_to_pg1()
                        root.withdraw()
                        pg3()

                    global l    
                    myobj.execute("SELECT username from users")
                    variable0 = myobj.fetchall()
                    encryption = userID_generator()
                    check1 = True
                    for i in variable0:
                        if i[0] == username_signup.get():
                            check1 = False
                    if check1 == True:
                        l.append([encryption,username_signup.get(),password_signup.get(),balance_signup.get()])
                        command = "INSERT INTO users VALUES(%s,%s,%s,%s)"
                        myobj.executemany(command,l)
                        mydb.commit()
                        l = [(encryption(),username_signup.get(),password_signup.get(),balance_signup.get())]
                        pg2_up_pg3()
                        
                    else:
                        messagebox.showwarning("Oops!", "Username already exists")   
                      
                sign_up_access = Button(root,text ="Submit" , padx =50, pady = 25,bg = "#484848",fg = "white" , command= signupcheck)
                sign_up_access.pack()

                L8 = Label(root , text = "       ",bg = "white")
                L8.pack()
                    
                            
                def pg2_sup_to_pg1():
                    balance_Label_signup.destroy()
                    balance_signup.destroy()
                    blankline3_signup.destroy()
                    
                    password_signup.destroy()
                    password_Label_signup.destroy()
                    blankline2_signup.destroy()
                    
                    blankline1_signup.destroy()
                    username_Label_signup.destroy()
                    username_signup.destroy()
                    
                    sign_up_access.destroy()
                    sign_up_label.destroy()
                    sign_up_back.destroy()
                    L8.destroy()
                    pg1()

                
                sign_up_back = Button(root,text="BACK" , padx =50, pady = 25,bg = "#484848",fg = "white" , command= pg2_sup_to_pg1)
                sign_up_back.pack()
                

            signup_filling()
        #---------------------------------------------------------------------------------------------------------------
        def pg2_signin():
            Sign_up_button.destroy()
            Sign_in_button.destroy()
            Exit_out.destroy()
            sign_in_label = Label(root , text = "platform to sign in",bg = "white") #pg2
            sign_in_label.pack()
            

            def signin_filling():
                
                #username
                username_Label_signin = Label(root , text = "USERNAME" ,bg = "#484848" , fg = "white")
                username_Label_signin.pack()
                    
                username_signin = Entry(root , bg = "#484848" , fg = "white")
                username_signin.pack()

                blankline4_signin = Label(root , text = "" , bg = "white" )
                blankline4_signin.pack()

                #password
                password_Label_signin = Label(root , text = "PASSWORD" ,bg = "#484848" , fg = "white")
                password_Label_signin.pack()
                    
                password_signin = Entry(root , bg = "#484848" , fg = "white")
                password_signin.pack()

                blankline5_signin = Label(root , text = "" , bg = "white" )
                blankline5_signin.pack()

                def signincheck():

                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                    myobj = mydb.cursor()
                    
                    def pg2_in_pg3():
                        sign_in_label.destroy()
                        pg2_sin_to_pg1()
                        root.withdraw()
                        pg3()

                    global l    
                    myobj.execute("SELECT * from users")
                    variable0 = myobj.fetchall()
                    check1 = True
                    for i in variable0:
                        if i[1:3] == (username_signin.get(),password_signin.get()):
                            check1 = False
                            l.append(i)
                            
                    if check1 == False:
                        pg2_in_pg3()
                    else:
                        messagebox.showerror("Failed to Sign In!", "Username or Password is incorrct")

                sign_in_access = Button(root,text ="Login" , padx =50, pady = 25,bg = "#484848",fg = "white" , command= signincheck)
                sign_in_access.pack()

                L9 = Label(root , text = "       ",bg = "white")
                L9.pack()

                def pg2_sin_to_pg1():
                    username_Label_signin.destroy()
                    username_signin.destroy()
                    blankline4_signin.destroy()

                    password_Label_signin.destroy()
                    password_signin.destroy()
                    blankline5_signin.destroy()

                    sign_in_access.destroy()
                    sign_in_label.destroy()
                    sign_in_back.destroy()
                    L9.destroy()
                    pg1()

                sign_in_back = Button(root,text="BACK" , padx =50, pady = 25,bg = "#484848",fg = "white" , command= pg2_sin_to_pg1 )
                sign_in_back.pack()

            signin_filling()    

        def exit_out():
            root.destroy()
    #--------------------------------------------------------------------------------------------------------------------------------
        #Creating table alone
            
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
            myobj.execute("CREATE TABLE USERS(userid varchar(50) Primary key ,username varchar(20) Unique,password varchar(30),balance integer(50))")

        
        Sign_up_button = Button(root ,text ="Sign Up" ,padx =50, pady = 25,bg = "#484848",fg = "white" ,command= pg2_signup)#sign up (page 1)
        Sign_up_button.pack()

        L1 = Label(root , text = "       ",bg = "white")
        L1.pack()

        Sign_in_button = Button(root, text ="Sign In" ,padx =52 ,pady = 25,bg = "#484848",fg = "white", command= pg2_signin) #sign in (page 1)
        Sign_in_button.pack()

        L2 = Label(root , text = "       ",bg = "white")
        L2.pack()

        Exit_out = Button(root,text = "Exit" ,padx =60,pady = 25,bg = "#484848",fg = "white", command= exit_out)
        Exit_out.pack()


    pg1()

l = []

root_splash_screen.after(3000, main)

mainloop()