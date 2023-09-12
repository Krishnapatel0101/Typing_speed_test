from tkinter import *
from tkinter import messagebox

base = Tk()  

base.geometry('500x500')
base.title("Typing Speed Test")
 
labl_0 = Label(base, text="Login form",width=20,font=("bold", 20))  
labl_0.place(x=90,y=53)  

labl_1 = Label(base, text="FullName",width=20,font=("bold", 10))  
labl_1.place(x=80,y=130)  

entry_1 = Entry(base)  
entry_1.place(x=240,y=130)  

labl_2 = Label(base, text="password",width=20,font=("bold", 10))  
labl_2.place(x=68,y=180)  
  
entry_02 = Entry(base)  
entry_02.place(x=240,y=180)  

labl_3 = Label(base, text="Gender",width=20,font=("bold", 10))  
labl_3.place(x=70,y=230)  
Radiobutton(base, text="Male",padx = 5, value=1).place(x=235,y=230)  
Radiobutton(base, text="Female",padx = 20, value=2).place(x=290,y=230)  


# function for check the data is already present or not
def check_text():
    a = entry_1.get()
    b = entry_02.get()
    c=a+" "+b+"\n"
    f=0
    with open("test.txt","r") as f:
        f1=f.readlines()
        for i in f1:
            if i==c:
                # found_user = Label(base,width=20,font=("bold", 20)).place(x=100,y=500) 
                f=0
                messagebox.showinfo("Valid","Sign In successfully")
                base.destroy()
                import game
                break
            else:
                f=1
        if f==1:
            messagebox.showerror("Inalid","Account not found")

# function for save data of user
def save_text():
    a = entry_1.get()
    b = entry_02.get()
    global params
    params = [a,b]
    with open("test.txt","a") as f:
        f.write(params[0]+" ")
        f.write(params[1]+"\n")
    messagebox.showinfo("Sign up","Your data is saved")
    
  
Button(base, text='Login',width=20,bg='brown',command=check_text,fg='white').place(x=180,y=380)  
new_user = Label(base, text="If you are new user\n than Press Sign Up button",width=20,font=("bold", 20)).place(x=100,y=300) 
Button(base, text='Sign Up',width=20,bg='brown',command=save_text,fg='white').place(x=180,y=410)  
base.mainloop()