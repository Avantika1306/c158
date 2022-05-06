from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 
root=Tk()
root.title("Credit Card")
root.geometry("600x600")
root.configure(background="yellow")
img=ImageTk.PhotoImage(Image.open("card.jpg"))
input1=Entry(root)
input1.place(relx=0.5,rely=0.2,anchor=CENTER)
def check():
    try:
        inputname=int(input1.get())
        messagebox.showinfo("credit card accepted")
    except(ValueError):
        messagebox.showinfo("error","invalid pin code credit card not accepted")
        
    
    
button1=Button(root,text="check credit card",command=check)
button1.place(relx=0.5,rely=0.3,anchor=CENTER)

label1=Label(root,image=img)
label1.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()
