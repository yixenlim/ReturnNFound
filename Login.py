from tkinter import *
import tkinter.messagebox

def show():

    font1 = ("impact",30)
    font2 = ("bahnschrift",15)
    font3 = ("bahnschrift light",12)

    def deposit(rootA,i,username):
        import Deposit
        rootA.destroy()
        Deposit.show(i,username)

    def retrieve(rootA,username):
        rootA.destroy()
        import Retrieve
        Retrieve.show(username)

    def choose(i,username) :
        rootA = Tk()
        rootA.title("ReturnNFound")
        rootA.geometry("1200x480")
        rootA.config(bg="slategrey")

        topframe = Frame(rootA,bg="slategrey")
        topframe.pack(fill=X,pady=50,side=TOP)

        middleframe = Frame(rootA,bg="slategrey")
        middleframe.place(relx=.5,rely=.5,anchor=CENTER)

        question = Label(topframe,text="Do you want to deposit lost item or retrieve your belonging?",bg="slategrey",fg="white")
        question.config(font=font1)
        question.pack(fill=X)

        deposit_button = Button(middleframe,text="Deposit",height=2,width=20,relief=FLAT,overrelief=SOLID,bg="white",command=lambda:deposit(rootA,i,username))
        deposit_button.grid(row=0,column=0)
        deposit_button.config(font=font2)

        empty_label = Label(middleframe,text="                      ",bg="slategrey")
        empty_label.grid(row=0,column=1)

        retrieve_button = Button(middleframe,text="Retrieve",height=2,width=20,relief=FLAT,overrelief=SOLID,bg="white",command=lambda:retrieve(rootA,username))
        retrieve_button.grid(row=0,column=2)
        retrieve_button.config(font=font2)

        rootA.mainloop()

    def check(root,id_entry,password_entry):
        i=0
        username = id_entry.get()
        password = password_entry.get()

        file = open("id_password.txt","r")
        content = file.read().split(",")
        file.close()

        while True:
            if username == content[i] and password == content[i+1]:
                root.destroy()
                choose(i,username)
                token="yes"
            elif i<=8:
                i=i+2
                token="no"
            elif i==10:
                token="yes"
                tkinter.messagebox.showerror("Error","Incorrect ID or password.")  
            if token == "yes":
                break

    def login():
        root = Tk()
        root.title("ReturnNFound")
        root.geometry("1200x480")
        root.config(bg="slategrey")

        topframe = Frame(root,bg="slategrey")
        topframe.pack(fill=X,pady=50,side=TOP)

        middleframe = Frame(root,bg="slategrey")
        middleframe.place(relx=.5,rely=.5,anchor=CENTER)

        belowframe = Frame(root,bg="slategrey")
        belowframe.pack(fill=X,side=BOTTOM,pady=60)
        
        welcome_word = Label(topframe,text="Welcome to ReturnNFound!",bg="slategrey",fg="white")
        welcome_word.config(font=font1)
        welcome_word.pack(fill=X)

        id_label = Label(middleframe,text="Student / Staff ID:",bg="slategrey",fg="white")
        id_label.config(font=font2)
        id_label.grid(row=0,column=0,sticky=E,pady=10)
        id_entry = Entry(middleframe,relief=FLAT,bd=7)
        id_entry.grid(row=0,column=1,pady=10,padx=5)
        id_entry.config(font=font3)

        password_label = Label(middleframe,text="Password:",bg="slategrey",fg="white")
        password_label.config(font=font2)
        password_label.grid(row=1,column=0,sticky=E,pady=10)
        password_entry = Entry(middleframe,show="*",relief=FLAT,bd=7)
        password_entry.grid(row=1,column=1,pady=10,padx=5)
        password_entry.config(font=font3)
        
        login_button = Button(belowframe,text="Log in",bg="white",relief=FLAT,width=10,height=1,overrelief=SOLID,command=lambda:check(root,id_entry,password_entry))
        login_button.pack()
        login_button.config(font=font2)

        root.mainloop()
        
    login()
    
