import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

def show():
    font1 = ("impact",30)
    font2 = ("bahnschrift",15)
    font3 = ("bahnschrift light",12)
    font4 = ("bahnschrift",20)
    font5 = ("impact",20)
    font6 = ("bahnschrift light",11)
    
    def history():        
        rootA = Tk()
        rootA.title("History List")
        rootA.geometry("1200x480")
        rootA.config(bg="slategrey")
        
        topframe = Frame(rootA,bg="slategrey")
        topframe.pack(pady=20,side=TOP)

        middleframe = Frame(rootA,bg="slategrey")
        middleframe.place(relx=.5,rely=.4,anchor=CENTER)

        belowframe = Frame(rootA,bg="slategrey")
        belowframe.pack(side=BOTTOM,pady=15,anchor=CENTER)

        inFile = open("retrieve_history.txt", "rt")
        contents = inFile.read().split("\n")
        inFile.close()

        inFile = open("retrieve_history.txt", "rt")
        fill = inFile.read()
        inFile.close()

        amount = (len(contents)-1)/6
        amount_number = round(amount)

        history_label = Label(topframe,bg="slategrey",fg="white",text="Retrieve History (" + str(amount_number) + ")")
        history_label.pack()
        history_label.config(font=font5)

        if not fill:
            empty_label = Label(middleframe,text="Empty",bg="slategrey",fg="white")
            empty_label.pack(pady=60)
            empty_label.config(font=font4)
        else:
            canvas = Canvas(middleframe,bg="white")
            scrollbar = Scrollbar(middleframe,orient=VERTICAL,command=canvas.yview)

            frame = Frame(canvas)
            frame.config(bg="white")

            choice = IntVar()
            i=0
            item_no = 1
            row_no = 0
            
            while i < (len(contents)-1):
                empty_label = Label(frame,bg="white",text="                              ")
                empty_label.grid(row=row_no,column=0)
                empty_label.config(font=font3)

                empty_label2 = Label(frame,bg="white",text="                              ")
                empty_label2.grid(row=row_no,column=0)
                empty_label2.config(font=font3)
                        
                button = Radiobutton(frame,variable=choice,value=item_no,bg="white")
                button.grid(row=row_no+1,rowspan=5,column=1,sticky=E,pady=10)

                picture_name = contents[i+1]
                img = PhotoImage(file=str(picture_name) + ".png")
                img = img.subsample(35,35)
                label = Label(frame,image=img)
                label.image=img
                label.grid(row=row_no+1,column=2,columnspan=2,rowspan=5,pady=10,padx=5)

                item_label = Label(frame,bg="white",text="Item Type: "+ contents[i+4])
                item_label.grid(row=row_no+1,column=4,sticky=W)
                item_label.config(font=font6)
                        
                casecode_label = Label(frame,bg="white",text="Case Code: "+ contents[i+1])
                casecode_label.grid(row=row_no+2,column=4,sticky=W)
                casecode_label.config(font=font6)
                
                desc_label = Label(frame,bg="white",text="Description: " + contents[i+2])
                desc_label.grid(row=row_no+3,column=4,sticky=W)
                desc_label.config(font=font6)
                
                depositor_label = Label(frame,bg="white",text="Depositor: " + contents[i])
                depositor_label.grid(row=row_no+4,column=4,sticky=W)
                depositor_label.config(font=font6)
                
                retriever_label = Label(frame,bg="white",text="Retriever: " + contents[i+5])
                retriever_label.grid(row=row_no+5,column=4,sticky=W)
                retriever_label.config(font=font6)
                
                i += 6
                item_no += 1
                row_no += 6

            canvas.create_window(0,0,anchor=N+W,window=frame)
            canvas.update_idletasks()
            canvas.config(width=700,height=240,scrollregion=canvas.bbox("all"),yscrollcommand=scrollbar.set)
            canvas.pack(fill=BOTH,expand=True,side=LEFT)
            scrollbar.pack(fill=Y,side=RIGHT)

            box_report = Button(belowframe,bg="white",relief=FLAT,width=10,height=1,overrelief=SOLID,text="Report",command=lambda:check(choice,rootA))
            box_report.pack()
            box_report.config(font=font2)

        logout_button = Button(belowframe,bg="white",relief=FLAT,width=10,height=1,overrelief=SOLID,text="Log out",command=lambda:back(rootA))
        logout_button.pack(pady=20)
        logout_button.config(font=font2)

    def back(root):
        import Login
        root.destroy()
        Login.show()

    def check(choice,rootA):
        if not choice.get():
            messagebox.showerror("Error","Please select one item!")
        else:
            reportBox(choice,rootA)
               
    def reportBox(choice,rootA):
        caseCode_index = int(choice.get())*6-5

        inFile = inFile = open("retrieve_history.txt","rt")
        contents = inFile.read().split("\n")
        inFile.close()

        caseCode = contents[caseCode_index]
        
        box_question = messagebox.askquestion("Warning","Do you want to report this case?")
        if box_question == "yes":
            reportYes(caseCode,rootA)
            
    def reportYes(caseCode,rootA):
        rootA.destroy()
        rootB = Tk()
        rootB.geometry("1200x480")
        rootB.config(bg="slategrey")

        middleframe = Frame(rootB,bg="slategrey")
        middleframe.place(relx=.5,rely=.4,anchor=CENTER)

        belowframe = Frame(rootB,bg="slategrey")
        belowframe.pack(fill=X,side=BOTTOM,pady=60)

        reported_label = Label(middleframe,bg="slategrey",fg="white",text="Reported to STAD Office." + "\n" + "Visit STAD Office for further instructions.")
        reported_label.pack()
        reported_label.config(font=font4)
        
        casecode_label = Label(middleframe,bg="slategrey",fg="white",text="Case code: " + str(caseCode))
        casecode_label.pack(pady=20)
        casecode_label.config(font=font4)

        box_logout = Button(belowframe,bg="white",width=10,height=1,relief=FLAT,overrelief=SOLID,text="Log out",command=lambda:back(rootB))
        box_logout.pack()
        box_logout.config(font=font2)

    history()
