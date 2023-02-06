from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import font

login_win = Tk()
login_win.title("login")
login_win.state('zoomed')

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
label_1 = ttk.Label(login_win , image = photo)
label_1.bind('<Configure>', resize_image)
label_1.pack(fill=BOTH, expand = YES)


frame_1=Frame(login_win ,height=550,width=400,bg="white").place(x=600,y=70)
label_2=Label(frame_1,text="USER LOGIN",font=('helvetica' ,26 ,'bold '),fg="brown",bg="white").place(x=690,y=90)

label_3=Label(frame_1,text="Username",font=('helvetica' ,16 ,'bold '),fg="brown",bg="white").place(x=635,y=160)
entry_1=Entry(frame_1,bd=1,bg="#EADDCA",font=('helvetica' ,14 ,'bold '),width=30).place(x=635,y=190)

label_4=Label(frame_1,text="Password",font=('helvetica' ,16 ,'bold '),fg="brown",bg="white").place(x=635,y=240)
entry_2=Entry(frame_1,bd=1,bg="#EADDCA",font=('helvetica' ,14 ,'bold '),width=30,show="*").place(x=635,y=270)


def grade_card():
    login_win.destroy()
    import Gradecard

btn_1=Button(frame_1,text="LOGIN",font=("helvetica 14 bold"),bg="#8B0000",fg="white",activebackground="#EADDCA",command=grade_card,
             activeforeground="black",width=27).place(x=635,y=350)

label_7=Label(frame_1,text="Don't have an account?",font=('helvetica' ,14 ,'bold '),fg="brown",bg="white").place(x=635,y=550)

def login_page():
    login_win.destroy()
    import signup

btn_2=Button(frame_1,text="Sign Up",font=('helvetica' ,14 ,'bold underline'),bg="white",bd=0,fg="blue",activebackground="white",
             activeforeground="blue",command=login_page).place(x=860,y=545)


login_win.mainloop()
