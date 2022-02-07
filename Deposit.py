import random
from tkinter import *
from collections import OrderedDict
import tkinter.messagebox
import shutil
            
def show(i,username):

    font1 = ("impact",30)
    font2 = ("bahnschrift",15)
    font3 = ("bahnschrift light",12)
    font4 = ("bahnschrift",20)

    def deposit_item_type(i,username):
        root = Tk()
        root.title("Deposit Module")
        root.geometry("1200x480")
        root.config(bg="slategrey")

        topframe = Frame(root,bg="slategrey")
        topframe.pack(fill=X,pady=50,side=TOP)

        middleframe = Frame(root,bg="slategrey")
        middleframe.place(relx=.5,rely=.5,anchor=CENTER)

        belowframe = Frame(root,bg="slategrey")
        belowframe.pack(fill=X,pady=60,side=BOTTOM)

        question_label = Label(topframe, text="What have you found dear?",bg="slategrey",fg="white")
        question_label.pack(pady=10,fill=X)
        question_label.config(font=font1)

        selection = StringVar(root)
        selection.set("Please select an item")
        
        choice = OrderedDict([ ("Bottle",0), ("Electronics",1),("Keys",2),("Wallet",3),("Others",4)])

        arraywords = ["A","b","C","d","y","z","S","o","h","q","k","2","3","5","6","7","8","9","1","4","E","e","F","f","g","G","m","N","R","T","t","W","X","a"]
        casecode_no = random.choice(arraywords) + random.choice(arraywords) + random.choice(arraywords) + random.choice(arraywords) + random.choice(arraywords) + random.choice(arraywords)        
        casecode_label = Label(middleframe, text="Case code: " + casecode_no,bg="slategrey",fg="white")
        casecode_label.grid(row=0,column=0,columnspan=2)
        casecode_label.config(font=font2)
        
        item = Label(middleframe, text="Item type:",bg="slategrey",fg="white")
        item.grid(row=1,column=0,sticky=E,pady=10)
        item.config(font=font2)
        
        option = OptionMenu(middleframe,selection,*choice)
        option.grid(row=1,column=1,pady=10,sticky=W,padx=5)
        option.config(relief=FLAT,bg="white",font=font3)

        desc = Label(middleframe, text="Description:",bg="slategrey",fg="white")
        desc.grid(row=2,column=0,sticky=E,pady=10)
        desc.config(font=font2)

        desc_entry = Entry(middleframe,relief=FLAT,bd=8)
        desc_entry.grid(row=2,column=1,pady=10,padx=5)
        desc_entry.config(font=font3)
        
        done_button = Button(belowframe, text="Done",relief=FLAT,bg="white",command=lambda:check(selection,desc_entry,casecode_no,i,username,root),overrelief=SOLID,width=10,height=1)
        done_button.pack()
        done_button.config(font=font2)

    def check(selection,desc_entry,casecode_no,i,username,root):
        if selection.get() == "Please select an item":
            tkinter.messagebox.showerror("Error","Please select an item!")
        elif not desc_entry.get():
            tkinter.messagebox.showerror("Error","Please provide some information!")
        else:
            write(selection,desc_entry,casecode_no,i,username,root)

    def write(selection,desc_entry,casecode_no,i,username,root):
        with open ("locker.txt","r+") as file:
            content = file.read().split(",")
            locker = len(content)-1
            new_locker = locker + 1
            file.write((str(new_locker)) + ",")

        description = desc_entry.get()
        item = selection.get()
        locker_no = str(locker)
        
        with open("data.txt","a") as file:
            file.write(username + "\n" + casecode_no + "\n" + description + "\n" + locker_no + "\n" + item + "\n")
        
        capture(i,casecode_no,locker_no,root)

    def capture(i,casecode_no,locker_no,root):
        root.destroy()
        rootA = Tk()
        rootA.title("Deposit Module")
        rootA.geometry("1200x480")
        rootA.config(bg="slategrey")

        middleframe = Frame(rootA,bg="slategrey")
        middleframe.place(relx=.5,rely=.5,anchor=CENTER)
        
        photo_label = Label(middleframe,bg="slategrey",fg="white",text="Place the item in front of the camera and click 'Capture' to take a photo of the item.")
        photo_label.pack()
        photo_label.config(font=font4)
        
        capture_button = Button(middleframe,text="Capture",relief=FLAT,width=10,bg="white",height=1,overrelief=SOLID,command=lambda:move(i,casecode_no,locker_no,rootA))
        capture_button.pack(pady=30)
        capture_button.config(font=font2)

    def move(i,casecode_no,locker_no,rootA):#file_location#
        shutil.move("C:/Users/Asus/Desktop/" + str(casecode_no) + ".png","C:/Users/Asus/Desktop/MiniIT1820/" + str(casecode_no) + ".png")
        locker(i,locker_no,rootA)

    def locker(i,locker_no,rootA):
        rootA.destroy()
        rootB = Tk()
        rootB.title("Deposit Module")
        rootB.geometry("1200x480")
        rootB.config(bg="slategrey")

        middleframe = Frame(rootB,bg="slategrey")
        middleframe.place(relx=.5,rely=.5,anchor=CENTER)

        locker_no = "Please place the item in Locker " + locker_no
        locker_label = Label(middleframe, text=locker_no,bg="slategrey",fg="white")
        locker_label.pack()
        locker_label.config(font=font4)

        locker_button = Button(middleframe, text="Done",command=lambda:tq(i,rootB),overrelief=SOLID,bg="white",relief=FLAT,width=10,height=1)
        locker_button.pack(pady=30)
        locker_button.config(font=font2)

    def tq(i,rootB):
        rootB.destroy()
        rootC = Tk()
        rootC.title("Deposit Module")
        rootC.geometry("1200x480")
        rootC.config(bg="slategrey")

        topframe = Frame(rootC,bg="slategrey")
        topframe.pack(fill=X,pady=50,side=TOP)

        middleframe = Frame(rootC,bg="slategrey")
        middleframe.place(relx=.5,rely=.5,anchor=CENTER)
        
        belowframe = Frame(rootC,bg="slategrey")
        belowframe.pack(fill=X,pady=60,side=BOTTOM)

        with open("merit_point.txt","r") as file:
            content = file.read().split(",")

            index = int(i/2)
            current_point = int(content[index])
            new_point = current_point + 1
            content[index] = new_point

        with open("merit_point.txt","w") as file_A:
            counter = 0
            while counter < 6:
                if counter != 5:
                    file_A.write(str(content[counter]) + ",")
                else:
                    file_A.write(str(content[counter]))
                counter += 1
            
            
        tq_label = Label(topframe, text="Thank you for your kindness!" + "\n" + "You have gained 1 merit point.",bg="slategrey",fg="white")
        tq_label.pack(pady=10)
        tq_label.config(font=font2)
        
        merit_point = "You now have " + str(new_point) + " points in total!"
        merit_point_label = Label(middleframe, text=merit_point,bg="slategrey",fg="white")
        merit_point_label.pack()
        merit_point_label.config(font=font4)

        merit_point_button = Button(belowframe,text="Log out",relief=FLAT,bg="white",width=10,height=1,overrelief=SOLID,command=lambda:back(rootC))
        merit_point_button.pack()
        merit_point_button.config(font=font2)

    def back(rootC):
        import Login
        rootC.destroy()
        Login.show()

    deposit_item_type(i,username)
