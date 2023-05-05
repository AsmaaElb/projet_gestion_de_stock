from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import *

db=Database("stock2.db")

window=Tk()
window.title("SQLite")
window.geometry("1920x1080")

frame1=Frame(window,padx=20,pady=20,bg="#636e72")
frame1.pack(side=TOP,fill=X)



name = StringVar() # Nom
description = StringVar() # Description
price = DoubleVar() # Prix unitaire
quantity = IntVar() # Quantité en stock
alert_threshold = IntVar() # Seuil d'alerte de stock
last_in = StringVar() # Date de dernière entrée en stock
last_out = StringVar() # Date de dernière sortie de stock
image = StringVar() # Image du produit


lblTitle=Label(frame1,bg="#636e72",text="PRODUCT DETAILS",font=("times",8,"bold"),fg="white",pady=10)
lblTitle.grid(columnspan=2)
lblName=Label(frame1,text="Nom",bg="#636e72",fg="white",font=("times",7,"bold"),pady=10)
lblName.grid(row=1,column=0)

txtName=Entry(frame1,textvariable=name,font=("times",10),width=43)
txtName.grid(row=1,column=1)

lblDesc=Label(frame1,text="Description",bg="#636e72",fg="white",font=("times",7,"bold"),pady=10)
lblDesc.grid(row=2,column=0)

txtDesc=Entry(frame1,font=("times",10),textvariable=description,width=43)
txtDesc.grid(row=2,column=1)

lblPrice=Label(frame1,text="Prix unitaire",bg="#636e72",fg="white",font=("times",7,"bold"),pady=10)
lblPrice.grid(row=3,column=0)

txtPrice=Entry(frame1,width=43,textvariable=price,font=("times",10))
txtPrice.grid(row=3,column=1)

lblQty=Label(frame1,text="Quantité en stock",bg="#636e72",fg="white",font=("times",7,"bold"),pady=10)
lblQty.grid(row=4,column=0)

txtQty=Entry(frame1,width=43,textvariable=quantity,font=("times",10))
txtQty.grid(row=4,column=1)

lblAlert=Label(frame1,text="Seuil d'alerte de stock",bg="#636e72",fg="white",font=("times",7,"bold"),pady=10)
lblAlert.grid(row=5,column=0)

txtAlert=Entry(frame1,width=43,textvariable=alert_threshold,font=("times",10))
txtAlert.grid(row=5,column=1)

lblLastIn=Label(frame1,text="Date de dernière entrée en stock",bg="#636e72",fg="white",font=("times",7,"bold"),pady=10)
lblLastIn.grid(row=6,column=0)

txtLastIn=Entry(frame1,width=43,textvariable=last_in,font=("times",10))
txtLastIn.grid(row=6,column=1)

lblLastOut=Label(frame1,text="Date de dernière sortie de stock",bg="#636e72",fg="white",font=("times",7,"bold"),pady=10)
lblLastOut.grid(row=7,column=0)

txtLastOut=Entry(frame1,width=43,textvariable=last_out,font=("times",10))
txtLastOut.grid(row=7,column=1)

lblImg=Label(frame1,text="Image du produit",bg="#636e72",fg="white",font=("times",7,"bold"),pady=10)
lblImg.grid(row=8,column=0)

txtImg=Entry(frame1,width=43,textvariable=image,font=("times",10))
txtImg.grid(row=8,column=1)


btn_frame=Frame(frame1,bg="#2d3436")
btn_frame.grid(row=9,column=1,columnspan=4)

def fecthData():
   table.delete(*table.get_children())
   count=0
   for row in db.fetch_records():
        count+=1
        table.insert("",END,values=(count,row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

def addData():
    if name.get()=="" or description.get()=="" or price.get()=="" or quantity.get()=="" or alert_threshold.get()=="" or last_in.get()=="" or last_out.get()=="" or image.get()=="":
        messagebox.showinfo("Message","Please Fill All Records")
    else:
        db.insert(name.get(),description.get(),price.get(),quantity.get(),alert_threshold.get(),last_in.get(),last_out.get(),image.get())
        fecthData()
        clearData()
        messagebox.showinfo("Message","Record Insert Successfully")

def getrecord(event):
    srow = table.focus()
    data = table.item(srow)
    global row
    row = data['values']
    name.set(row[2])
    description.set(row[3])
    price.set(row[4])
    quantity.set(row[5])
    alert_threshold.set(row[6])
    last_in.set(row[7])
    last_out.set(row[8])
    image.set(row[9])
   

def updateData():
  
    if name.get() == "" or description.get() == "" or price.get() == "" or quantity.get() == "" or alert_threshold.get() == "" or last_in.get() == "" or last_out.get() == "" or image.get() == "":
        messagebox.showinfo("Message", "Please Fill All Records")
    else:
        db.update_recordS(name.get(), description.get(), price.get(), quantity.get(), alert_threshold.get(), last_in.get(), last_out.get(), image.get(), (row[1]))
        fecthData()
        clearData()
        messagebox.showinfo("Message", "Record Update Successfully")

def deleteData():
    db.remove_record(row[1])
    fecthData()
    clearData()
    messagebox.showinfo("Message", "Record Delete Successfully")

def clearData():
    name.set("")
    description.set("")
    price.set("")
    quantity.set("")
    alert_threshold.set("")
    last_in.set("")
    last_out.set("")
    image.set("")


btnSub=Button(btn_frame,text="Insert",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=addData)
btnSub.grid(row=0,column=0)

btnUp=Button(btn_frame,text="Update",bg="#F79F1F",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=updateData)
btnUp.grid(row=0,column=1)

btnDel=Button(btn_frame,text="Delete",bg="#ee5253",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=deleteData)
btnDel.grid(row=0,column=2)

btnClr=Button(btn_frame,text="Clear",bg="#1289A7",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=clearData)
btnClr.grid(row=0,column=3)


myFrame=Frame(window)
myFrame.place(x=0,y=400,width=2000,height=500)

style=ttk.Style()
style.configure("Treeview",font=("times",8),rowheight=20)
style.configure("Treeview.Heading",font=("times",8,"bold"))

table = ttk.Treeview(myFrame, columns=(0,1,2,3,4,5,6,7,8,9))

table.column("0", anchor=CENTER)
table.column("1", stretch=NO, width=0)
table.column("3", anchor=CENTER)
table.column("4", anchor=CENTER)
table.column("5", anchor=CENTER)
table.column("6", anchor=CENTER)
table.column("7", anchor=CENTER)
table.column("8", anchor=CENTER)
table.column("9", anchor=CENTER)

table.heading("0", text="ID")
table.heading("1", text="Nom")
table.heading("2", text="Description")
table.heading("3", text="Prix unitaire")
table.heading("4", text="Quantité en stock")
table.heading("5", text="Seuil d'alerte de stock")
table.heading("6", text="Date de dernière entrée en stock")
table.heading("7", text="Date de dernière sortie de stock")
table.heading("8", text="Image du produit")

table["show"] = 'headings'
table.bind("<ButtonRelease-1>", getrecord)
table.pack(fill=X)














window.mainloop()