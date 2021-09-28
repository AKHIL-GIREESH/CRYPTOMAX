from tkinter import *
from tkinter import messagebox

root_splash_screen = Tk()
root_splash_screen.overrideredirect(True)

canvas = Canvas(width = 640 , height = 640)
canvas.pack()

photo = PhotoImage(file = 'F:\Wallpapers\CRYPTOMAX.png')

canvas.create_image(0,0, image=photo , anchor = NW)

def main():  #main part
    root_splash_screen.destroy()
    root  = Tk()
    root.geometry("1920x1080")
    root.configure(bg = "white")

    upperline1 = Label(root, text = "",bg = "#E00000",padx = 1920 , pady = 60)
    upperline1.pack()
    
    heading=Label(root,text="CRYPTOMAX",bg = "white")
    heading.config(font=("Copperplate",50))
    heading.pack()

    lowerline1 = Label(root,text="", bg = "#004b8f",padx = 1920 , pady = 60)
    lowerline1.pack(side = BOTTOM)

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
                    
            def change_usernamed():
                
                root_vpd.withdraw()
                root_usernamed = Tk()
                root_usernamed.geometry("1920x1080")
                root_usernamed.configure(bg = "#202020")
                
                change_username1_labeld = Label(root_usernamed , text = "Enter the new username")
                change_username1_labeld.pack()
                
                change_username1d = Entry(root_usernamed,width = 18, bg = "#CF780A" , fg = "#202020")
                change_username1d.config(font=("copperplate",15))
                change_username1d.pack()

                change_username2_labeld = Label(root_usernamed , text = "Re-enter the new username")
                change_username2_labeld.pack()
                
                change_username2d = Entry(root_usernamed,width = 18,bg = "#CF780A" , fg = "#202020")
                change_username2d.config(font=("copperplate",15))
                change_username2d.pack()

                def checkingd():
                    if change_username1d.get() == change_username2d.get():
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                        myobj = mydb.cursor()

                        global l   
                        list1d = [change_username1d.get() , l[0]]
                        command = "UPDATE users SET username = %s WHERE userid = %s"
                        myobj.execute(command,list1d)
                        mydb.commit()
                        l[1] = change_username1d.get()

                        change_username1_labeld.destroy()
                        change_username1d.destroy()

                        change_username2_labeld.destroy()
                        change_username2d.destroy()

                        checknamed.destroy()
                        
                        
                    else:
                        messagebox.showerror("Oops!", "Enter the username correctly")
                        
                checknamed = Button(root_usernamed ,text = "CHANGE",width = 18 , height = 3,bg = "#CF780A" , fg = "#202020",command = checkingd)
                checknamed.config(font=("copperplate",15))
                checknamed.pack()

                def userhomed():
                    root_usernamed.withdraw()
                    root_vpd.deiconify()

                Luser2d = Label(root_usernamed , text = "       ",bg = "#202020")
                Luser2d.pack()
                
                user_homed = Button(root_usernamed ,text="BACK",width = 18 , height = 3,bg = "#CF780A",fg = "#202020" ,command = userhomed)
                user_homed.config(font=("copperplate",15))
                user_homed.pack()

                
            change_username_buttond = Button(root_vpd,text = "CHANGE USERNAME" ,width = 18 , height = 3,bg = "#CF780A",fg = "#202020" ,command = change_usernamed)
            change_username_buttond.config(font=("copperplate",15))
            change_username_buttond.pack()
            
            def change_passwordd():

                root_vpd.withdraw()
                root_passwordd = Tk()
                root_passwordd.geometry("1920x1080")
                root_passwordd.configure(bg = "#202020")
                
                change_password1_labeld = Label(root_passwordd , text = "Enter the new password")
                change_password1_labeld.pack()
                
                change_password1d = Entry(root_passwordd,width = 18,bg = "#CF780A" , fg = "#202020")
                change_password1d.config(font=("copperplate",15))
                change_password1d.pack()

                change_password2_labeld = Label(root_passwordd , text = "Re-enter the new password")
                change_password2_labeld.pack()
                
                change_password2d = Entry(root_passwordd,width = 18 ,bg = "#CF780A" , fg = "#202020")
                change_password2d.config(font=("copperplate",15))
                change_password2d.pack()

                def checking_passwordd():
                    if change_password1d.get() == change_password2d.get():
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                        myobj = mydb.cursor()

                        global l   
                        list2 = [change_password1d.get() , l[0]]
                        command = "UPDATE users SET password= %s WHERE userid = %s"
                        myobj.execute(command,list2)
                        mydb.commit()
                        l[2] = change_password1d.get()
                    else:
                        messagebox.showerror("Oops!", "Enter the password correctly")
                        
                checkpasswordd = Button(root_passwordd ,text = "CHANGE" ,width = 18 , height = 3,bg = "#CF780A" , fg = "#202020",command = checking_passwordd)
                checkpasswordd.config(font=("copperplate",15))
                checkpasswordd.pack()

                def passhomed():
                    root_passwordd.withdraw()
                    root_vpd.deiconify()

                Lpass2d = Label(root_passwordd , text = "       ",bg = "#202020")
                Lpass2d.pack()
                
                passhomedd = Button(root_passwordd ,text = "BACK" ,width = 18 , height = 3,bg = "#CF780A",fg = "#202020" ,command = passhomed)
                passhomedd.config(font=("copperplate", 15))
                passhomedd.pack()
                
            change_password_buttond = Button(root_vpd,text = "CHANGE PASSWORD" ,width = 18 , height = 3,bg = "#CF780A",fg = "#202020" ,command = change_passwordd)
            change_password_buttond.config(font=("copperplate",15))
            change_password_buttond.pack()
                    
            profile_home_buttondd = Button(root_vpd,text = "BACK",width = 18 , height = 3,bg = "#CF780A",fg = "#202020" ,command = pro_homed)
            profile_home_buttondd.config(font=("copperplate",15))
            profile_home_buttondd.pack()
        

        Profile_buttond = Button(root1d,text = "PROFILE",width = 18 , height = 3,bg = "#CF780A",fg = "#202020" ,command = viewprofiled)
        Profile_buttond.config(font=("copperplate",15))
        Profile_buttond.pack()

        L3d = Label(root1d, text = "       ",bg = "#202020")
        L3d.pack()

        def transactiond():
            root1d.withdraw()
            root_trd = Tk()
            root_trd.geometry("1920x1080")
            root_trd.configure(bg = "#202020")
            pass

            def tran_depositd():
                root_trd.withdraw()
                root_depositd = Tk()
                root_depositd.geometry("1920x1080")
                root_depositd.configure(bg = "#202020")

                depol1d = Label(root_depositd , text = "Enter the amount to be deposited")
                depol1d.pack()

                depoentry1d = Entry(root_depositd , bg = "#202020" , fg = "#CF780A")
                depoentry1d.config(font=("copperplate",15))
                depoentry1d.pack()

                Ltran3d = Label(root_depositd , text = "       ",bg = "#202020")
                Ltran3d.pack()
                
                def depositingd():
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                    myobj = mydb.cursor()

                    global l

                    list1d = [int(depoentry1d.get()) + l[3] , l[0]]
                    command = "UPDATE users SET balance = %s WHERE userid = %s"
                    myobj.execute(command,list1d)
                    mydb.commit()
                    l[3] += int(depoentry1d.get()) 

                    depol2d = Label(root_depositd , text= "Deposited successfully")
                    depol2d.pack()

                def depohomed():
                    root_depositd.withdraw()
                    root_trd.deiconify()
                    
                depobuttond = Button(root_depositd ,text = "INVEST",width = 18,height = 3,bg = "#CF780A",fg = "#202020" ,command = depositingd)
                depobuttond.config(font=("copperplate",15))
                depobuttond.pack()

                Ltran2d = Label(root_depositd , text = "       ",bg = "#202020")
                Ltran2d.pack()
                
                dephomed = Button(root_depositd ,text = "HOME",width = 18, height = 3,bg = "#CF780A",fg = "#202020" ,command = depohomed)
                dephomed.config(font=("copperplate",15))
                dephomed.pack()

            def tran_payd():
                root_trd.withdraw()
                root_payd = Tk()
                root_payd.geometry("1920x1080")
                root_payd.configure(bg = "#202020")

                payl1d = Label(root_payd , text = "Enter the amount to be payed")
                payl1d.pack()

                payentry1d = Entry(root_payd , bg = "#CF780A" , fg = "#202020")
                payentry1d.config(font=("copperplate",15))
                payentry1d.pack()

                Lpay3d = Label(root_payd , text = "       ",bg = "#202020")
                Lpay3d.pack()

                payl2d = Label(root_payd , text = "Enter the name of the user")
                payl2d.pack()

                payentry2d = Entry(root_payd , bg = "#CF780A" , fg = "#202020")
                payentry2d.config(font=("copperplate",15))
                payentry2d.pack()

                Lpay4d = Label(root_payd , text = "       ",bg = "#202020")
                Lpay4d.pack()

                def find_userd(x):
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                    myobj = mydb.cursor()
                    myobj.execute("SELECT username FROM users ")
                    variable2d = myobj.fetchall()
                    check = False
                    for i in variable2d:
                        if i == (x,):
                            check = True
                    if check == True:
                        return True
                    return False

                def ledger(x,y,z):
                    list3d = [x+str(y)+z]
                    with open("PUBLIC_LEDGER.txt","a") as f:
                        for i in list3d:
                            f.write(i+"\n") 
                    
                    with open("PUBLIC_LEDGER.txt") as f:
                        return [i for i in (f.read()).split("\n")]

                def payingd():
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                    myobj = mydb.cursor()

                    global l

                    if find_userd(payentry2d.get()) == True:
                        xd = l[3] - int(payentry1d.get())
                        l1d = [xd,l[0]]
                        command1d = "UPDATE users SET balance = %s WHERE userid =%s"
                        myobj.execute(command1d,l1d)
                        mydb.commit()

                        myobj.execute("SELECT username , balance from users")

                        yd = myobj.fetchall()
                            
                        for i in yd:
                            if i[0] == payentry2d.get() :
                                xd = i[1] + int(payentry1d.get())
                            
                            
                        l2d = [xd, payentry2d.get()]  

                        commandd = "UPDATE users \
                                    SET balance = %s \
                                    WHERE username =%s"
                        myobj.execute(commandd,l2d)
                        mydb.commit()
                        ledgerd(l[1],payentry1d.get(),payentry2d.get())

                        payl2d = Label(root_payd , text= "Deposited successfully")
                        payl2d.pack()

                    else:
                        messagebox.showerror("Oops!", "User doesn't exist")
                
                def payhomed():
                    root_payd.withdraw()
                    root_trd.deiconify()
                    
                paybuttond = Button(root_payd ,text = "PAY",height = 3 , width = 18 ,bg = "#CF780A",fg = "#202020" ,command = payingd)
                paybuttond.config(font=("copperplate",15))
                paybuttond.pack()

                Lpay2d = Label(root_payd , text = "       ",bg = "#202020")
                Lpay2d.pack()
                
                payhomd = Button(root_payd ,text = "BACK",height = 3 , width = 18 ,bg = "#CF780A",fg = "#202020" ,command = payhomed)
                payhomd.config(font=("copperplate",15))
                payhomd.pack()
            

            def tran_homed():
                root_trd.withdraw()
                root1d.deiconify()

            transaction_deposit_button = Button(root_trd,text="DEPOSIT", height = 3, width =15,bg = "#CF780A",fg = "#202020" ,command = tran_depositd)
            transaction_deposit_button.config(font=("copperplate",15))
            transaction_deposit_button.pack()

            transaction_label1 = Label(root_trd,text = "           " , bg = "#202020")
            transaction_label1.pack()
            
            transaction_pay_button = Button(root_trd,text="DEPOSIT",height = 3, width = 18,bg = "#CF780A",fg = "#202020" ,command = tran_payd)
            transaction_pay_button.config(font=("copperplate",15))
            transaction_pay_button.pack()

            transaction_label2 = Label(root_trd,text = "           " , bg = "#202020")
            transaction_label2.pack()

            transaction_home_buttond = Button(root_trd,text = "BACK",height = 3, width = 18, bg = "#CF780A",fg = "#202020" ,command = tran_homed)
            transaction_home_buttond.config(font=("copperplate",15))
            transaction_home_buttond.pack()

        Transaction_buttond = Button(root1d,text = "TRANSACTION",height = 3 , width = 18 ,bg = "#CF780A",fg = "#202020" ,command = transactiond)
        Transaction_buttond.config(font=("copperplate",15))
        Transaction_buttond.pack()

        L4d = Label(root1d , text = "       ",bg = "#202020")
        L4d.pack()

        def ledgerd():
            root1d.withdraw()
            root_ledd = Tk()
            root_ledd.geometry("1920x1080")
            root_ledd.configure(bg = "#202020")
            
            with open("PUBLIC_LEDGER.txt") as f:
                for i in (f.read()).split("\n"):
                    Label(root_ledd , text = i , fg = "#202020" , bg = "#CF780A").pack()
                    Label(root_ledd,text = "").pack()

            def led_homed():
                root_ledd.withdraw()
                root1d.deiconify()

            led_home_buttond = Button(root_ledd,text = "BACK",height = 3,width = 18 ,bg = "#CF780A",fg = "#202020" ,command = led_homed)
            led_home_buttond.config(font=("copperplate",15))
            led_home_buttond.pack()
        
        Ledger_buttond = Button(root1d,text = "PUBLIC LEDGER" ,height = 3 , width = 18,bg = "#CF780A",fg = "#202020" , command = ledgerd)
        Ledger_buttond.config(font=("copperplate",15))
        Ledger_buttond.pack()
        
        L5d = Label(root1d , text = "       ",bg = "#202020")
        L5d.pack()

        def RCGENERATORd(xd):
            xd = xd.lower()
            rcd = ""
            for i in xd:
                if i.isalpha() == True:
                    rcd += str(ord(i) - 80)
                    
                elif i.isnumeric() == True:
                    rcd += str(int(i) + 50)

            return f"{int(rcd):o}"

        def blockchaind():
            root1d.withdraw()
            root_blcd = Tk()
            root_blcd.geometry("1920x1080")
            root_blcd.configure(bg = "#202020")
            
            xd = []
            with open("PUBLIC_LEDGER.txt") as f:
                for i in (f.read()).split("\n"):
                    xd.append(i)
                    
            megablockd = {}
            fristtransd = True

            for i in range(len(xd)):
                if fristtransd == True:
                    rcd = RCGENERATORd(xd[i])
                    megablockd[rcd] = ["BEGINNING",xd[i]]
                    prevrcd = rcd
                    fristtransd = False
                else:
                    rcd = RCGENERATORd(xd[i])
                    megablockd[str(int(prevrcd) + int(rcd))] = [prevrcd,xd[i]]
                    prevrcd = str(int(prevrcd) + int(rcd)) 
            
            Label(root_blcd , text= megablockd).pack()
            
            def mining_homed():
                root_blcd.withdraw()
                root1d.deiconify()

            mining_home_buttond = Button(root_blcd,text = "Home",height = 3, width = 18,bg = "#CF780A",fg = "#202020" ,command = mining_homed)
            mining_home_buttond.config(font=("copperplate",15))
            mining_home_buttond.pack()
        
        Blockchain_buttond = Button(root1d,text = "MINING",height = 3, width = 18,bg = "#CF780A",fg = "#202020" ,command = blockchaind)
        Blockchain_buttond.config(font=("copperplate",15))
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
            conversion_entryd.config(font=("copperplate",15))
            conversion_entryd.pack()

            def convertd():
                convert_buttond.destroy()
                x = int(conversion_entryd.get())//10
                
                conversion_labeld = Label(root_cond ,text = x)
                conversion_labeld.pack()
                
                conversion_labeld.insert(0,"Enter the amount in rupees",fg="white")
                conversion_labeld.pack()

            convert_buttond = Button(root_cond , text = "Convert",height = 3 , width = 18,bg = "#CF780A",fg = "#202020" ,command =convertd)
            convert_buttond.config(font=("copperplate",15))
            convert_buttond.pack()
            

            L13d = Label(root_cond, text = "       ",bg = "#202020")
            L13d.pack()

            con_home_buttond = Button(root_cond,text = "Home",height = 3, width = 18,bg = "#CF780A",fg = "#202020" ,command = con_homed)
            con_home_buttond.config(font=("copperplate",15))
            con_home_buttond.pack(side = BOTTOM)
        
        Conversion_buttond = Button(root1d,text = "Conversion",height=3, width = 18,bg = "#CF780A",fg = "#202020" ,command = conversiond)
        Conversion_buttond.config(font=("copperplate",15))
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
            
        Home_backd = Button(root1d,text="HOME" , height =3 , width = 18,bg = "#CF780A",fg = "#202020" , command=Back_to_homed)
        Home_backd.config(font=("copperplate",15))
        Home_backd.pack()

    #--------------------------------------------------------------------------------------------------------------------------------------

    #REGULAR THEME
        
    def pg3():
        root1 = Tk()
        root1.geometry("1920x1080")
        root1.configure(bg = "white")

        upperline2 = Label(root1,text = "",bg = "#E00000",padx = 1920 , pady = 40)
        upperline2.pack()

        lowerline2  = Label(root1,text="", bg = "#004b8f",padx= 1920, pady=40)        
        lowerline2.pack(side = BOTTOM)

        global l

        heading=Label(root1,text="WELCOME "+ l[1],bg = "white" ,fg = "#484848")
        heading.config(font=("Sans-serif",40))
        heading.pack()


        L10 = Label(root1 , text = "       ",bg = "white")
        L10.pack()

        def viewprofile():
            root1.withdraw()
            root_vp = Tk()
            root_vp.geometry("1920x1080")
            root_vp.configure(bg = "white")
            
            upperline3 = Label(root_vp,text = "",bg = "#E00000",padx = 1920 , pady = 60)
            upperline3.pack()

            heading_vp = Label(root_vp, text = "PROFILE", bg = "white" , fg = "#484848")
            heading_vp.config(font=("copperplate",50))
            heading_vp.pack()

            l_vp = Label(root_vp ,bg = "white")
            l_vp.pack()

            lowerline3  = Label(root_vp,text="", bg = "#004b8f",padx= 1920, pady=60)        
            lowerline3.pack(side = BOTTOM)
        
            def pro_home():
                root_vp.withdraw()
                root1.deiconify()

            global l    
            profile_username = Label(root_vp ,width = 18 , text = "USERNAME:" + l[1] , bg = "white",fg = "#484848")
            profile_username.config(font=("copperplate",15))
            profile_username.pack()

            pl1 = Label(root_vp , text = "                " , bg = "white")
            pl1.pack()
            
            profile_password = Label(root_vp ,width = 18, text = "PASSWORD:" + l[2] , bg = "white",fg = "#484848")
            profile_password.config(font=("copperplate",15))
            profile_password.pack()

            pl2 = Label(root_vp , text = "                " , bg = "white")
            pl2.pack()

            profile_balance = Label(root_vp ,width = 18, text = "BALANCE:" + str(l[3]) , bg = "white",fg = "#484848")
            profile_balance.config(font=("copperplate",15))
            profile_balance.pack()

            pl3 = Label(root_vp , text = "                " , bg = "white")
            pl3.pack()

            profile_encrypted = Label(root_vp ,width = 50, text = "USER-ID: " + l[0] , bg = "white",fg = "#484848")
            profile_encrypted.config(font=("copperplate",15))
            profile_encrypted.pack()

            pl4 = Label(root_vp , text = "                " , bg = "white")
            pl4.pack()

            def change_username():
                
                root_vp.withdraw()
                root_username = Tk()
                root_username.geometry("1920x1080")
                root_username.configure(bg = "white")

                upperline4 = Label(root_username,text = "",bg = "#E00000",padx = 1920 , pady = 60)
                upperline4.pack()

                heading_user = Label(root_username, text = "CHANGE USERNAME", bg = "white" , fg = "#484848")
                heading_user.config(font=("copperplate",50))
                heading_user.pack()

                l_user = Label(root_username ,bg = "white")
                l_user.pack()

                lowerline4  = Label(root_username,text="", bg = "#004b8f",padx= 1920, pady=60)        
                lowerline4.pack(side = BOTTOM)
                
                change_username1_label = Label(root_username ,width=30, text = "Enter the new username",fg = "#484848",bg = "white")
                change_username1_label.config(font=("copperplate",15))
                change_username1_label.pack()
                
                change_username1 = Entry(root_username,bg = "#484848" , fg = "white")
                change_username1.config(font=("copperplate",15))
                change_username1.pack()

                change_username2_label = Label(root_username , width = 30, text = "Re-enter the new username", fg = "#484848" , bg = "white")
                change_username2_label.config(font=("copperplate",15))
                change_username2_label.pack()
                
                change_username2 = Entry(root_username,bg = "#484848" , fg = "white")
                change_username2.config(font=("copperplate",15))
                change_username2.pack()

                def checking():
                    if change_username1.get() == change_username2.get():
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                        myobj = mydb.cursor()

                        global l   
                        list1 = [change_username1.get() , l[0]]
                        command = "UPDATE users SET username = %s WHERE userid = %s"
                        myobj.execute(command,list1)
                        mydb.commit()
                        l[1] = change_username1.get()

                        change_username1_label.destroy()
                        change_username1.destroy()

                        change_username2_label.destroy()
                        change_username2.destroy()

                        checkname.destroy()

                        userl2 = Label(root_username , text= "Updated successfully")
                        userl2.pack()
                        
                        
                    else:
                        messagebox.showerror("Oops!", "Enter the username correctly")
                        
                l_username = Label(root_username,bg = "white")
                l_username.pack()

                checkname = Button(root_username ,text = "Change",height = 3, width = 18,bg = "#484848" , fg = "white",command = checking)
                checkname.config(font=("copperplate",15))
                checkname.pack()

                def userhome():
                    root_username.withdraw()
                    root_vp.deiconify()

                Luser2 = Label(root_username , text = "       ",bg = "white")
                Luser2.pack(side = BOTTOM)
                
                user_home = Button(root_username ,text="Home",height=3, width= 15 ,bg = "#484848",fg = "white" ,command = userhome)
                user_home.config(font=("copperplate",15))
                user_home.pack(side = BOTTOM)

                
            change_username_button = Button(root_vp,text = "CHANGE USERNAME" ,height = 3 , width = 18,bg = "#484848",fg = "white" ,command = change_username)
            change_username_button.config(font=("copperplate",14))
            change_username_button.pack()

            l_vp3 = Label(root_vp ,bg = "white")
            l_vp3.pack()
            
            def change_password():

                root_vp.withdraw()
                root_password = Tk()
                root_password.geometry("1920x1080")
                root_password.configure(bg = "white")
                
                upperline5 = Label(root_password,text = "",bg = "#E00000",padx = 1920 , pady = 60)
                upperline5.pack()

                heading_pass = Label(root_password, text = "CHANGE PASSWORD", bg = "white" , fg = "#484848")
                heading_pass.config(font=("copperplate",50))
                heading_pass.pack()

                l_pass = Label(root_password ,bg = "white")
                l_pass.pack()
                
                lowerline5  = Label(root_password,text="", bg = "#004b8f",padx= 1920, pady=60)        
                lowerline5.pack(side = BOTTOM)
                
                change_password1_label = Label(root_password , text = "Enter the new password",bg = "white", width =30)
                change_password1_label.config(font=("copperplate",15))
                change_password1_label.pack()
                
                change_password1 = Entry(root_password,bg = "#484848" , fg = "white")
                change_password1.config(font=("copperplate",15))
                change_password1.pack()

                l_pass = Label(root_password , bg = "white")
                l_pass.pack()

                change_password2_label = Label(root_password , text = "Re-enter the new password",bg = "white", width =30)
                change_password2_label.config(font=("copperplate",15))
                change_password2_label.pack()
                
                change_password2 = Entry(root_password,bg = "#484848" , fg = "white")
                change_password2.config(font=("copperplate",15))
                change_password2.pack()

                l_pass1 = Label(root_password , bg = "white")
                l_pass1.pack()

                def checking_password():
                    if change_password1.get() == change_password2.get():
                        import mysql.connector
                        mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                        myobj = mydb.cursor()

                        global l   
                        list2 = [change_password1.get() , l[0]]
                        command = "UPDATE users SET password= %s WHERE userid = %s"
                        myobj.execute(command,list2)
                        mydb.commit()
                        l[2] = change_password1.get()

                        change_password1_label.destroy()
                        change_password1.destroy()

                        change_password2_label.destroy()
                        change_password2.destroy()

                        checkpassword.destroy()

                        passl2 = Label(root_password , text= "Updated successfully")
                        passl2.pack()
                        
                    else:
                        messagebox.showerror("Oops!", "Enter the password correctly")
                        
                checkpassword = Button(root_password , text = "Change",width = 18, height = 3,bg = "#484848" , fg = "white",command = checking_password)
                checkpassword.config(font=("copperplate",15))
                checkpassword.pack()

                def passhome():
                    root_password.withdraw()
                    root_vp.deiconify()

                Lpass2 = Label(root_password , text = "       ",bg = "white")
                Lpass2.pack(side = BOTTOM)
                
                pass_home = Button(root_password ,text = "BACK", width = 18, height = 3,bg = "#484848",fg = "white" ,command = passhome)
                pass_home.config(font=("copperplate",15))
                pass_home.pack(side = BOTTOM)
                
            change_password_button = Button(root_vp,text = "CHANGE PASSWORD" ,width = 18, height = 3,bg = "#484848",fg = "white" ,command = change_password)
            change_password_button.config(font=("copperplate",14))
            change_password_button.pack()
                
            l_vp4 = Label(root_vp,bg = "white")
            l_vp4.pack(side = BOTTOM)

            profile_home_button = Button(root_vp,text = "HOME",width = 17, height = 3,bg = "#484848",fg = "white" ,command = pro_home)
            profile_home_button.config(font=("copperplate",15))
            profile_home_button.pack(side = BOTTOM)

        Profile_button = Button(root1,text = "PROFILE",width = 18, height = 3,bg = "#484848",fg = "white" ,command = viewprofile)
        Profile_button.config(font=("copperplate",15))
        Profile_button.pack()

        L3 = Label(root1, text = "       ",bg = "white")
        L3.pack()

        def transaction():
            root1.withdraw()
            root_tr = Tk()
            root_tr.geometry("1920x1080")
            root_tr.configure(bg = "white")

            upperline6 = Label(root_tr,text = "",bg = "#E00000",padx = 1920 , pady = 60)
            upperline6.pack()

            lowerline6  = Label(root_tr,text="", bg = "#004b8f",padx= 1920, pady=60)        
            lowerline6.pack(side = BOTTOM)
            
            def tran_deposit():
                root_tr.withdraw()
                root_deposit = Tk()
                root_deposit.geometry("1920x1080")
                root_deposit.configure(bg = "white")

                upperline7 = Label(root_deposit,text = "",bg = "#E00000",padx = 1920 , pady = 60)
                upperline7.pack()

                lowerline7  = Label(root_deposit,text="", bg = "#004b8f",padx= 1920, pady=60)        
                lowerline7.pack(side = BOTTOM)

                depol1 = Label(root_deposit , text = "Enter the amount to be deposited", width = 17)
                depol1.pack()

                depoentry1 = Entry(root_deposit , bg = "#484848" , fg = "white")
                depoentry1.config(font=("copperplate",15))
                depoentry1.pack()

                Ltran3 = Label(root_deposit , text = "       ",bg = "white")
                Ltran3.pack()
                
                def depositing():
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                    myobj = mydb.cursor()

                    global l

                    list1 = [int(depoentry1.get()) + l[3] , l[0]]
                    command = "UPDATE users SET balance = %s WHERE userid = %s"
                    myobj.execute(command,list1)
                    mydb.commit()
                    l[3] += int(depoentry1.get()) 

                    depol1.destroy()
                    depoentry1.destroy()
                    Ltran3.destroy()
                    depobutton.destroy()

                    depol2 = Label(root_deposit , text= "Deposited successfully")
                    depol2.pack()

                def depohome():
                    root_deposit.withdraw()
                    root_tr.deiconify()
                    
                depobutton = Button(root_deposit ,text = "Invest",height = 2, width = 18, bg = "#484848",fg = "white" ,command = depositing)
                depobutton.config(font=("copperplate",15))
                depobutton.pack()

                Ltran2 = Label(root_deposit , text = "       ",bg = "white")
                Ltran2.pack()
                
                depo_home = Button(root_deposit ,text = "Home",height = 2, width = 18, bg = "#484848",fg = "white" ,command = depohome)
                depo_home.config(font=("copperplate",15))
                depo_home.pack()

            def tran_pay():
                root_tr.withdraw()
                root_pay = Tk()
                root_pay.geometry("1920x1080")
                root_pay.configure(bg = "white")

                upperline8 = Label(root_pay,text = "",bg = "#E00000",padx = 1920 , pady = 60)
                upperline8.pack()

                lowerline8  = Label(root_pay,text="", bg = "#004b8f",padx= 1920, pady=60)        
                lowerline8.pack(side = BOTTOM)

                payl1 = Label(root_pay , text = "Enter the amount to be payed")
                payl1.pack()

                payentry1 = Entry(root_pay , bg = "#484848" , fg = "white")
                payentry1.config(font=("copperplate",15))
                payentry1.pack()

                Lpay3 = Label(root_pay , text = "       ",bg = "white")
                Lpay3.pack()

                payl2 = Label(root_pay , text = "Enter the name of the user")
                payl2.pack()

                payentry2 = Entry(root_pay , bg = "#484848" , fg = "white")
                payentry2.config(font=("copperplate",15))
                payentry2.pack()

                Lpay4 = Label(root_pay , text = "       ",bg = "white")
                Lpay4.pack()

                def find_user(x):
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                    myobj = mydb.cursor()
                    myobj.execute("SELECT username FROM users ")
                    variable2 = myobj.fetchall()
                    check = False
                    for i in variable2:
                        if i == (x,):
                            check = True
                    if check == True:
                        return True
                    return False

                def ledger(x,y,z):
                    list3 = [x+str(y)+z]
                    with open("PUBLIC_LEDGER.txt","a") as f:
                        for i in list3:
                            f.write(i+"\n")
                    
                    with open("PUBLIC_LEDGER.txt") as f:
                        return [i for i in (f.read()).split("\n")]

                def paying():
                    import mysql.connector
                    mydb = mysql.connector.connect(host="localhost",user="root",passwd = "lmao",database = "CRYPTOCURRENCY")
                    myobj = mydb.cursor()

                    global l

                    if find_user(payentry2.get()) == True:
                        x = l[3] - int(payentry1.get())
                        l1 = [x,l[0]]
                        command1 = "UPDATE users SET balance = %s WHERE userid =%s"
                        myobj.execute(command1,l1)
                        mydb.commit()

                        myobj.execute("SELECT username , balance from users")

                        y = myobj.fetchall()
                            
                        for i in y:
                            if i[0] == payentry2.get() :
                                x = i[1] + int(payentry1.get())
                            
                            
                        l2 = [x, payentry2.get()]  

                        command = "UPDATE users \
                                    SET balance = %s \
                                    WHERE username =%s"
                        myobj.execute(command,l2)
                        mydb.commit()
                        ledger(l[1],payentry1.get(),payentry2.get())

                        payl1.destroy()
                        payentry1.destroy()
                        Lpay3.destroy()
                        
                        payl2.destroy()
                        payentry2.destroy()
                        Lpay4.destroy()

                        payl5 = Label(root_pay , text= "Deposited successfully")
                        payl5.pack()


                    else:
                        messagebox.showerror("Oops!", "User doesn't exist")
                
                def payhome():
                    root_pay.withdraw()
                    root_tr.deiconify()
                    
                paybutton = Button(root_pay ,text = "Pay",height = 3 , width = 18, bg = "#484848",fg = "white" ,command = paying)
                paybutton.config(font=("copperplate",15))
                paybutton.pack()

                Lpay2 = Label(root_pay , text = "       ",bg = "white")
                Lpay2.pack()
                
                pay_home = Button(root_pay ,text = "Back",height = 3, width = 18,bg = "#484848",fg = "white" ,command = payhome)
                pay_home.config(font=("copperplate",15))
                pay_home.pack()
                        
                
            def tran_home():
                root_tr.withdraw()
                root1.deiconify()

            transaction_deposit_button = Button(root_tr ,text ="Deposit",height = 3 , width = 18,bg = "#484848",fg = "white" ,command = tran_deposit)    
            transaction_deposit_button.config(font=("copperplate",15))
            transaction_deposit_button.pack()

            Ltran1 = Label(root1 , text = "       ",bg = "white")
            Ltran1.pack()

            transaction_pay_button = Button(root_tr ,text ="Pay",height = 3 , width = 18,bg = "#484848",fg = "white" ,command = tran_pay)    
            transaction_pay_button.config(font=("copperplate",15))
            transaction_pay_button.pack()

            Ltran4 = Label(root1 , text = "       ",bg = "white")
            Ltran4.pack()

            transaction_home_button = Button(root_tr,text = "Home",height = 3, width = 18,bg = "#484848",fg = "white" ,command = tran_home)
            transaction_home_button.config(font=("copperplate",15))
            transaction_home_button.pack()

        Transaction_button = Button(root1,text = "TRANSACTION",height = 3 , width = 18, bg = "#484848",fg = "white" ,command = transaction)
        Transaction_button.config(font=("copperplate",15))
        Transaction_button.pack()

        L4 = Label(root1 , text = "       ",bg = "white")
        L4.pack()
  

        def ledger():
            root1.withdraw()
            root_led = Tk()
            root_led.geometry("1920x1080")
            root.configure(bg = "white")

            upperline9 = Label(root_led,text = "",bg = "#E00000",padx = 1920 , pady = 60)
            upperline9.pack()

            lowerline9  = Label(root_led,text="", bg = "#004b8f",padx= 1920, pady=60)        
            lowerline9.pack(side = BOTTOM)
            
            with open("PUBLIC_LEDGER.txt") as f:
                for i in (f.read()).split("\n"):
                    Label(root_led , text = i , fg = "white" , bg = "#484848").pack()
                    Label(root_led,text = "").pack()

            def led_home():
                root_led.withdraw()
                root1.deiconify()

            led_home_button = Button(root_led,text = "Home",height = 3, width = 18, bg = "#484848",fg = "white" ,command = led_home)
            led_home_button.config(font=("copperplate",15))
            led_home_button.pack()
        
        Ledger_button = Button(root1,text = "Public Ledger" ,height = 3 , width = 18, bg = "#484848",fg = "white" , command = ledger)
        Ledger_button.config(font=("copperplate",15))
        Ledger_button.pack()
        
        L5 = Label(root1 , text = "       ",bg = "white")
        L5.pack()

        
        def RCGENERATOR(x):
            x = x.lower()
            rc = ""
            for i in x:
                if i.isalpha() == True:
                    rc += str(ord(i) - 80)
                    
                elif i.isnumeric() == True:
                    rc += str(int(i) + 50)
            
            return f"{int(rc):o}" 
        
        def blockchain():
            root1.withdraw()
            root_blc = Tk()
            root_blc.geometry("1920x1080")
            root_blc.configure(bg = "white")

            upperline10 = Label(root_blc,text = "",bg = "#E00000",padx = 1920 , pady = 60)
            upperline10.pack()

            lowerline10 = Label(root_blc,text="", bg = "#004b8f",padx= 1920, pady=60)       
            lowerline10.pack(side = BOTTOM)
            
                
            x = []
            with open("PUBLIC_LEDGER.txt") as f:
                for i in (f.read()).split("\n"):
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
            Label(root_blc , text= megablock).pack()

            def mining_home():
                root_blc.withdraw()
                root1.deiconify()

            mining_home_button = Button(root_blc,text = "Home",height = 3, width = 18,bg = "#484848",fg = "white" ,command = mining_home)
            mining_home_button.config(font=("copperplate",15))
            mining_home_button.pack()
        
        Blockchain_button = Button(root1,text = "Mining",height = 3, width = 18,bg = "#484848",fg = "white" ,command = blockchain)
        Blockchain_button.config(font=("copperplate",15))
        Blockchain_button.pack()
        
        L6 = Label(root1 , text = "       ",bg = "white")
        L6.pack()

        def conversion():
            root1.withdraw()
            root_con = Tk()
            root_con.geometry("1920x1080")
            root_con.configure(bg = "white")

            upperline11 = Label(root_con,text = "",bg = "#E00000",padx = 1920 , pady = 60)
            upperline11.pack()

            lowerline11 = Label(root_con,text="", bg = "#004b8f",padx= 1920, pady=60)        
            lowerline11.pack(side = BOTTOM)

            conversion_entry = Entry(root_con , width = 25 , bg = "#484848",fg = "white")
            conversion_entry.config(font=("copperplate",15))
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

            convert_button = Button(root_con , text = "Convert",height = 3, width = 18, bg = "#484848",fg = "white" ,command =convert)
            convert_button.config(font=("copperplate",15))
            convert_button.pack()

            L13 = Label(root_con , text = "       ",bg = "white")
            L13.pack()
        
            con_home_button = Button(root_con,text = "Home",height = 3 ,width = 18, bg = "#484848",fg = "white" ,command = con_home)
            con_home_button.config(font=("copperplate",15))
            con_home_button.pack(side = BOTTOM)
        
        Conversion_button = Button(root1,text = "Conversion",height = 3 , width = 18, bg = "#484848",fg = "white" ,command = conversion)
        Conversion_button.config(font=("copperplate",15))
        Conversion_button.pack()
        
        L7 = Label(root1 , text = "       ",bg = "white")
        L7.pack()

        def Dark_theme():
            root1.withdraw()
            pg3d()

        Dark_theme_button = Button(root1, text = "DARK MODE", height = 3, width = 18,bg = "#484848",fg = "white" , command=Dark_theme)
        Dark_theme_button.config(font=("copperplate",15))
        Dark_theme_button.pack()
        
        L11 = Label(root1 , text = "       ",bg = "white")
        L11.pack()

        def Back_to_home():
            root1.destroy()
            root.deiconify()
            
        Home_back = Button(root1,text="HOME" , height = 3, width = 18,bg = "#484848",fg = "white" , command=Back_to_home)
        Home_back.config(font=("copperplate",15))
        Home_back.pack()
        
    #--------------------------------------------------------------------------------------------------------------------------------------

    def pg1():
        def pg2_signup():
            Sign_up_button.destroy()
            Sign_in_button.destroy()
            Exit_out.destroy()
            
            l1.destroy()
            L1.destroy()
            L2.destroy()
            
            l_sup = Label(root, text = '''
            
                                    ''',bg = "white")
            l_sup.pack()

            l_sup1 = Label(root, bg = "white")
            l_sup1.pack(side = BOTTOM)

            sign_up_label = Label(root,text = "SIGN UP",bg = "white") #sign up (page 2)
            sign_up_label.config(font=("Copperplate",35))
            sign_up_label.pack()
            
            #Generating userID
            def userID_generator():
                from random import randint , choice , shuffle
                userID = []
                ID = ""
                noofuppercasechars = randint(2,3)
                for i in range(noofuppercasechars):
                    uppercasechar = randint(65,90)
                    userID.append(chr(uppercasechar))

                nooflowercasechars = randint(2,3)
                for i in range(nooflowercasechars):
                    lowercasechar = randint(97,122)
                    userID.append(chr(lowercasechar))

                noofdigits = randint(2,3)
                for i in range(noofdigits):
                    digit = randint(0,100)
                    userID.append(str(digit))

                x = ["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*"]
                noofspecialchars = randint(1,3)
                for i in range(noofspecialchars):
                    specialchar = choice(x)
                    userID.append(specialchar)

                shuffle(userID)
                for i in userID:
                    ID+=i
                return ID

            def signup_filling():
                
                l_sup2 = Label(root,bg = "white")
                l_sup2.pack()
                #username

                username_Label_signup = Label(root ,width = 18, text = "USERNAME" ,bg = "white" , fg = "#484848")
                username_Label_signup.config(font=("copperplate",15))
                username_Label_signup.pack()
                    
                username_signup = Entry(root ,width = 18, bg = "#484848" , fg = "white" )
                username_signup.config(font=("copperplate",15))
                username_signup.pack()

                blankline1_signup = Label(root , text = "" , bg = "white" )
                blankline1_signup.pack()

                #password
                password_Label_signup = Label(root ,width = 18, text = "PASSWORD" ,bg = "white" , fg = "#484848")
                password_Label_signup.config(font=("copperplate",15))
                password_Label_signup.pack()
                    
                password_signup = Entry(root ,width=15, bg = "#484848" , fg = "white")
                password_signup.config(font=("copperplate",15))
                password_signup.pack()

                blankline2_signup = Label(root , text = "" , bg = "white" )
                blankline2_signup.config(font=("copperplate",15))
                blankline2_signup.pack()

                #account balance
                balance_Label_signup = Label(root ,width = 18, text = "DEPOSIT" ,bg = "white" , fg = "#484848")
                balance_Label_signup.config(font=("copperplate",15))
                balance_Label_signup.pack()
                    
                balance_signup = Entry(root ,width = 18, bg = "#484848" , fg = "white")
                balance_signup.config(font=("copperplate",15))
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
                    l = []

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
                        
                        l = [encryption,username_signup.get(),password_signup.get(),balance_signup.get()]
                        pg2_up_pg3()
                        
                    else:
                        messagebox.showwarning("Oops!", "Username already exists")   
                      
                sign_up_access = Button(root,text ="Submit" , height = 3, width = 18,bg = "#484848",fg = "white" , command= signupcheck)
                sign_up_access.config(font=("copperplate",15))
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
                    
                    l_sup.destroy()
                    l_sup1.destroy()
                    l_sup2.destroy()
                    pg1()

                
                sign_up_back = Button(root,text="BACK" ,height = 3 , width =15 ,bg = "#484848",fg = "white" , command= pg2_sup_to_pg1)
                sign_up_back.config(font=("copperplate",15))
                sign_up_back.pack(side = BOTTOM)
                

            signup_filling()
        #---------------------------------------------------------------------------------------------------------------
        def pg2_signin():
            Sign_up_button.destroy()
            Sign_in_button.destroy()
            Exit_out.destroy()
            
            l1.destroy()
            L1.destroy()
            L2.destroy()            
            
            l_sin = Label(root, text = '''
                            
                                        ''',bg = "white")
            l_sin.pack()

            l_sin1 = Label(root , bg = "white")
            l_sin1.pack(side = BOTTOM)

            sign_in_label = Label(root , text = "SIGN IN",bg = "white") #pg2
            sign_in_label.config(font=("Copperplate",35))
            sign_in_label.pack()
            

            def signin_filling():
                
                l_sin2 = Label(root, bg = "white")
                l_sin2.pack()

                #username
                username_Label_signin = Label(root ,width = 18, text = "USERNAME" ,bg = "white" , fg = "#484848")
                username_Label_signin.config(font=("copperplate",15))
                username_Label_signin.pack()
                    
                username_signin = Entry(root ,width = 18, bg = "#484848" , fg = "white")
                username_signin.config(font=("copperplate",15))
                username_signin.pack()

                blankline4_signin = Label(root , text = "" , bg = "white" )
                blankline4_signin.pack()

                #password
                password_Label_signin = Label(root ,width = 18, text = "PASSWORD" ,bg = "white" , fg = "#484848")
                password_Label_signin.config(font=("copperplate",15))
                password_Label_signin.pack()
                    
                password_signin = Entry(root ,width = 18, bg = "#484848" , fg = "white")
                password_signin.config(font=("copperplate",15))
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
                    l = []

                    myobj.execute("SELECT * from users")
                    variable0 = myobj.fetchall()
                    check1 = True
                    for i in variable0:
                        if i[1:3] == (username_signin.get(),password_signin.get()):
                            check1 = False
                            l.append(i)
                            l = list(l[0])
                    if check1 == False:
                        pg2_in_pg3()
                    else:
                        messagebox.showerror("Failed to Sign In!", "Username or Password is incorrct")

                sign_in_access = Button(root,text ="Login" , height=3, width = 18,bg = "#484848",fg = "white" , command= signincheck)
                sign_in_access.config(font=("copperplate",15))
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
                    
                    l_sin.destroy()
                    l_sin1.destroy()
                    l_sin2.destroy()
                    pg1()

                sign_in_back = Button(root,text="BACK" ,height =3, width = 18, bg = "#484848",fg = "white" , command= pg2_sin_to_pg1 )
                sign_in_back.config(font=("copperplate",15)) 
                sign_in_back.pack(side = BOTTOM)

            signin_filling()    

        def exit_out():
            import sys
            root.destroy()
            sys.exit()
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

        
        l1 = Label(root, text = ''' 
                                
                            
                            
                            
                             
                            ''' , bg = "white")
        l1.pack()
        
        Sign_up_button = Button(root ,text ="Sign Up" ,width =15, height = 3,bg = "#484848",fg = "white" ,command= pg2_signup)#sign up (page 1)
        Sign_up_button.config(font=("Copperplate",15))
        Sign_up_button.pack()

        L1 = Label(root , text = "       ",bg = "white")
        L1.pack()

        Sign_in_button = Button(root, text ="Sign In" ,width =15, height = 3,bg = "#484848",fg = "white", command= pg2_signin) #sign in (page 1)
        Sign_in_button.config(font=("Copperplate",15))
        Sign_in_button.pack()

        L2 = Label(root , text = "       ",bg = "white")
        L2.pack(side = BOTTOM)

        Exit_out = Button(root,text = "Exit" ,width =15, height = 3,bg = "#484848",fg = "white", command= exit_out)
        Exit_out.config(font=("Copperplate",15))
        Exit_out.pack(side = BOTTOM)


    pg1()

l = []

root_splash_screen.after(3000, main)

mainloop()
