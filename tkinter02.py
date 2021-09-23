from tkinter import*

splash_root= Tk()
splash_root.title("oh yeah")
splash_root.geometry("300x200+-1500+250")

splash_label= Label(splash_root, text="omg", font=("Helvetica",18))
splash_label.pack()

splash_root.mainloop()

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
    
    x = ["X100Y","Y100X"]
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
