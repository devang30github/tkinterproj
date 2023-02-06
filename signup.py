from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import font
import mysql.connector as mysql


signup_win = Tk()
signup_win.title("Signup")
signup_win.state('zoomed')


def reset():
    for widget in frame_1.winfo_children():
        if isinstance(widget, Entry):
            widget.delete(0, END)


def conn_database():
    if a1.get()=='' or a2.get()=='' or a3.get()=='' or a4.get()=='':
        messagebox.showerror('Error',' Entries are empty!')
    elif a3.get() != a4.get():
        messagebox.showerror('Error','Password doesnt matched!')
    else:
        try:
            conn=mysql.connect(user="root",password="pinkman",host="127.0.0.1")
            c=conn.cursor()
        except:
            messagebox.showerror('Error','Database issue')
            return
        try:
            query='use adp_project'
            c.execute(query)
            query="create table upin_data(ID int auto_increment primary key not null,EMAIL varchar(50),USERNAME varchar(100),PASSWORD varchar(20))"
            c.execute(query)
        except:
            c.execute('use adp_project')

            query='insert into upin_data(EMAIL,USERNAME,PASSWORD) values(%s,%s,%s)'
            c.execute(query,(a1.get() ,a2.get() ,a3.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Succes','Registration is succesfull')
            reset()
        
        
        

def signup_page():
    signup_win.destroy()
    import login
    
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label_1.config(image = photo)
    label_1.image = photo 

image = Image.open('bg3.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label_1 = ttk.Label(signup_win, image = photo)
label_1.bind('<Configure>', resize_image)
label_1.pack(fill=BOTH, expand = YES)


frame_1=Frame(signup_win,height=500,width=400,bg="white")

label_2=Label(frame_1,text="CREATE AN ACCOUNT",font=('helvetica' ,26 ,'bold '),fg="brown",bg="white").place(x=10,y=20)

label_3=Label(frame_1,text="Email",font=('helvetica' ,16 ,'bold '),fg="brown",bg="white").place(x=30,y=90)
a1=StringVar()
entry1=Entry(frame_1,bd=1,bg="#EADDCA",textvariable=a1,font=('helvetica' ,14 ,'bold '),width=30).place(x=30,y=120)

label_4=Label(frame_1,text="Username",font=('helvetica' ,16 ,'bold '),fg="brown",bg="white").place(x=30,y=160)
a2=StringVar()
entry2=Entry(frame_1,bd=1,bg="#EADDCA",textvariable=a2,font=('helvetica' ,14 ,'bold '),width=30).place(x=30,y=190)

label_5=Label(frame_1,text="Password",font=('helvetica' ,16 ,'bold '),fg="brown",bg="white").place(x=30,y=230)
a3=StringVar()
entry3=Entry(frame_1,bd=1,bg="#EADDCA",textvariable=a3,font=('helvetica' ,14 ,'bold '),width=30).place(x=30,y=260)

label_6=Label(frame_1,text="Confirm password",font=('helvetica' ,16 ,'bold '),fg="brown",bg="white").place(x=30,y=300)
a4=StringVar()
entry4=Entry(frame_1,bd=1,bg="#EADDCA",textvariable=a4,font=('helvetica' ,14 ,'bold '),width=30).place(x=30,y=330)

btn_1=Button(frame_1,text="SIGN UP",font=("helvetica 14 bold"),bg="#8B0000",fg="white",command=conn_database,
             activebackground="#EADDCA", activeforeground="black",width=27).place(x=30,y=390)

label_7=Label(frame_1,text="Already have an account?",font=('helvetica' ,14 ,'bold '),fg="brown",bg="white").place(x=30,y=460)



btn_2=Button(frame_1,text="Log In",font=('helvetica' ,14 ,'bold underline'),bg="white",bd=0,fg="blue",activebackground="white",
             activeforeground="blue",command=signup_page).place(x=275,y=455)

frame_1.place(x=600,y=80)
signup_win.mainloop()
