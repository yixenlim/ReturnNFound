from tkinter import *
import tkinter as tk
from tkinter import messagebox
from collections import OrderedDict

def show(username):

    font1 = ("impact",30)
    font2 = ("bahnschrift",15)
    font3 = ("bahnschrift light",12)
    font4 = ("bahnschrift",20)
    font5 = ("impact",20)

    def retrieve_item_type (username):
        root = Tk()
        root.title("Retrieve Module")
        root.geometry("1200x480")
        root.config(bg="slategrey")

        topframe = Frame(root,bg="slategrey")
        topframe.pack(fill=X,pady=50,side=TOP)

        middleframe = Frame(root,bg="slategrey")
        middleframe.place(relx=.5,rely=.5,anchor=CENTER)

        belowframe = Frame(root,bg="slategrey")
        belowframe.pack(fill=X,side=BOTTOM,pady=60)
        
        selection = StringVar(root)
        dropDown_list = OrderedDict([("Bottle",0),("Electronics",1),("Keys",2),("Wallet",3),("Others",4)])
        selection.set("Please select an item")

        question_label = Label(topframe,text="What have you lost dear?",bg="slategrey",fg="white")
        question_label.pack()
        question_label.config(font=font1)

        drop_down = OptionMenu(middleframe,selection,*dropDown_list)
        drop_down.pack()
        drop_down.config(bg="white",relief=FLAT,font=font3)
                
        search_button = Button(belowframe,text="Search",relief=FLAT,bg="white",width=10,height=1,overrelief=SOLID,command = lambda:select(selection,username,root))
        search_button.pack()
        search_button.config(font=font2)

    def select(selection,username,root):
        if selection.get() == "Please select an item":
            messagebox.showerror("Error","Please select an item")
        else:
            result(selection,username,root)
    
    def result(selection,username,root):
        root.destroy()
        rootA = Tk()
        rootA.title("Results")
        rootA.geometry("1200x480")
        rootA.config(bg="slategrey")

        topframe = Frame(rootA,bg="slategrey")
        topframe.pack(pady=25,side=TOP)

        middleframe = Frame(rootA,bg="slategrey")
        middleframe.place(relx=.5,rely=.4,anchor=CENTER)

        belowframe = Frame(rootA,bg="slategrey")
        belowframe.pack(side=BOTTOM,pady=15,anchor=CENTER)

        with open("data.txt","r") as database:
            content = database.read().split("\n")

        with open("data.txt","r") as database:
            fill = database.read()

        if not fill or selection.get() not in content:
            result_label = Label(topframe,bg="slategrey",fg="white",text="Result (0)")
            result_label.pack()
            result_label.config(font=font5)

            empty_label = Label(middleframe,text="Empty",bg="slategrey",fg="white")
            empty_label.pack()
            empty_label.config(font=font4)
            
            logout_button = Button(middleframe,text="Log out",bg="white",relief=FLAT,overrelief=SOLID,width=10,height=1,command=lambda:back(rootA))
            logout_button.pack(pady=30)
            logout_button.config(font=font2)
            
        else:
            canvas = Canvas(middleframe,bg="white")
            scrollbar = Scrollbar(middleframe,orient=VERTICAL,command=canvas.yview)

            frame = Frame(canvas)
            frame.config(bg="white")
            
            choice = IntVar()
            i=0
            item_no = 1
            row_no = 0
            
            while i < (len(content)-1):
                if selection.get() == content[i+4]:
                    empty_label = Label(frame,bg="white",
                                        text="                              ")
                    empty_label.grid(row=row_no)
                    empty_label.config(font=font3)
                    
                    button = Radiobutton(frame,variable=choice,value=item_no,bg="white")
                    button.grid(row=row_no,rowspan=2,column=0,sticky=E,pady=5)

                    picture_name = content[i+1]
                    img = PhotoImage(file=str(picture_name) + ".png")
                    img = img.subsample(35,35)
                    label = Label(frame,image=img,bg="white")
                    label.image=img
                    label.grid(row=row_no,column=1,columnspan=2,rowspan=2,pady=10)

                    desc_label = Label(frame,bg="white",text="Description: "+ content[i+2])
                    desc_label.grid(row=row_no,column=3,sticky=W+S)
                    desc_label.config(font=font3)
                    
                    case_label = Label(frame,bg="white",text="Case Code:" + content[i+1])
                    case_label.grid(row=row_no+1,column=3,sticky=W+N)
                    case_label.config(font=font3)
                    
                    i += 5
                    item_no += 1
                    row_no += 2
                else:
                    i += 5

            result_label = Label(topframe,bg="slategrey",fg="white",text="Result (" + str(item_no-1) + ")")
            result_label.pack()
            result_label.config(font=font5)

            canvas.create_window(0,0,anchor=N+W,window=frame)
            canvas.update_idletasks()
            canvas.config(width=700,height=240,yscrollcommand=scrollbar.set,scrollregion=canvas.bbox("all"))
            canvas.pack(fill=BOTH,expand=True,side=LEFT)
            scrollbar.pack(fill=Y,side=RIGHT)
            
            retrieve_button = Button(belowframe,bg="white",text="Retrieve",relief=FLAT,width=10,height=1,overrelief=SOLID,command = lambda:check(choice,selection,username,rootA))
            retrieve_button.grid(row=0,column=0,columnspan=2,pady=5)
            retrieve_button.config(font=font2)

        question_label = Label(belowframe, text="Did not see your item here?",bg="slategrey",fg="white")
        question_label.grid(row=1,column=0,columnspan=2,pady=5)
        question_label.config(font=font2)

        try_label = Label(belowframe,text="Try to see:",bg="slategrey",fg="white")
        try_label.grid(row=2,column=0,pady=5)
        try_label.config(font=font2)

        history_button = Button(belowframe,bg="white",text="Retrieve History",relief=FLAT,width=15,overrelief=SOLID,height=1,command=lambda:retrieve_history(rootA))
        history_button.grid(row=2,column=1,pady=5,padx=5)
        history_button.config(font=font2)

    def retrieve_history(rootA):
        rootA.destroy()
        import Retrieve_history
        Retrieve_history.show()

    def check(choice,selection,username,rootA):
        if not choice.get():
            messagebox.showerror("Error","Please select one item or check retrieve history!")
        else:
            retrieve_conf(choice,selection,username,rootA)

    def retrieve_conf(choice,selection,username,rootA):
        MsgBox = messagebox.askquestion("Warning" , "Are you sure you want to retrieve this item?" , icon = "warning")
        if MsgBox == "yes":
            rootA.destroy()
            rootB = Tk()
            rootB.title("Location")
            rootB.geometry("1200x480")
            rootB.config(bg="slategrey")

            middleframe = Frame(rootB,bg="slategrey")
            middleframe.place(relx=.5,rely=.5,anchor=CENTER)

            with open("data.txt","r")as file:
                content = file.read().split("\n")

            i=0
            time=1
            loop=1

            while i < (len(content)-1):
                if selection.get() == content[i+4]:
                    if str(time) == str(choice.get()):
                        i += 5
                        time += 1
                        
                        locker = int(loop)*5-2
               
                        locker_label = Label(middleframe,bg="slategrey",fg="white",text="Your item is at Locker " + str(content[locker]))
                        locker_label.pack()
                        locker_label.config(font=font4)
                        
                        done_button = Button(middleframe,text="Done",bg="white",relief=FLAT,width=10,overrelief=SOLID,height=1,command=lambda:careful_logout(rootB))
                        done_button.pack(pady=30)
                        done_button.config(font=font2)
                    else:
                        time += 1
                        i += 5
                        loop += 1
                else:
                    i += 5
                    loop += 1
                    
            rewrite(selection,choice,username)

    def rewrite(selection,choice,username):
        file = open("data.txt","r")
        content = file.read().split("\n")
        file.close()

        i=0
        time=1

        while i < (len(content)-1):
            if selection.get() == content[i+4]:
                if str(time) == str(choice.get()):
                    
                    index_content=0
                    index_array=0

                    array = [None]*(len(content)-6)

                    while index_content < (len(content)-1):
                        if index_content != i and index_content != i+1 and index_content != i+2 and index_content != i+3 and index_content != i+4:
                            array[index_array] = content[index_content]
                            index_content += 1
                            index_array += 1
                        else:
                            file = open("retrieve_history.txt","a")
                            item = content[index_content]
                            file.write(item + "\n")
                            file.close()
                            index_content += 1
                    i += 5
                    time += 1
                else:
                    time += 1
                    i += 5
            else:
                i += 5

        file = open("retrieve_history.txt","a")
        file.write(username + "\n")
        file.close()

        index_newarray = 0

        file = open("data.txt","w")
        while index_newarray < len(array):
            depositor = array[index_newarray]
            caseCode = array[index_newarray+1]
            description = array[index_newarray+2]
            locker = array[index_newarray+3]
            item_type = array[index_newarray+4]
            file.write(depositor + "\n" + caseCode + "\n" + description + "\n" + locker + "\n" + item_type + "\n")
            index_newarray += 5
        file.close()

    def careful_logout(rootB):
        rootB.destroy()
        rootC = Tk()
        rootC.title("Exit")
        rootC.geometry("1200x480")
        rootC.config(bg="slategrey")

        middleframe = Frame(rootC,bg="slategrey")
        middleframe.place(relx=.5,rely=.5,anchor=CENTER)

        careful_label = Label(middleframe,text="Be careful next time!",bg="slategrey",fg="white")
        careful_label.pack()
        careful_label.config(font=font4)
        
        logout_button = Button(middleframe,relief=FLAT,bg="white",width=10,height=1,overrelief=SOLID,text="Log Out",command=lambda:back(rootC))
        logout_button.pack(pady=30)
        logout_button.config(font=font2)

    def back(root):
        import Login
        root.destroy()
        Login.show()

    retrieve_item_type(username)
