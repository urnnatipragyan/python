from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()

def data():
    user_id = userid.get().strip()
    password = pass_entery.get()
    print(f"User ID: {user_id}\nPassword: {password}")

    if not user_id or not password:
        messagebox.showwarning("Login", "Please enter both User ID and Password")
        return

    if user_id == "urnnati" and password == "1234":
        messagebox.showinfo("Login", "Login successful")
        print("Login successful")
    else:
        messagebox.showerror("Login", "Login failed")
        print("Login failed")



root.title("LOGIN PAGE")
root.minsize(200, 200)
root.geometry("400x400")
root.config(bg="white")


# image label
img=Image.open("facebook/Screenshot 2026-03-10 162536.png")
resize_img=img.resize((90, 90))
img=ImageTk.PhotoImage(resize_img)
img_label=Label(root,image=img)
img_label.pack(pady=(18,2))
img_label.config(bg="white")

#text label
text_label=Label(root,text="Facebook",font=("courier", 26))
text_label.pack(pady=(10,18))


#credentials label

userid_label=Label(root,text="Enter User ID",font=("courier", 16))
userid_label.pack(pady=(10,18))
userid_label.config(bg="white",fg="black")

userid=Entry(root,width=30)
userid.pack(ipady=8,pady=(0,18))


pass_label=Label(root,text="Enter Password",font=("Times New Roman", 16))
pass_label.pack(pady=(10,18))
pass_label.config(bg="white",fg="black")

pass_entery=Entry(root,width=30,show="*")
pass_entery.pack(ipady=8,pady=(0,18))

#button label

Btn=Button(root,text="Login",font=("italic", 16),command=data)
Btn.config(bg="white",fg="black",activebackground="blue",activeforeground="white",width=6,height=3)
Btn.pack(pady=(18,8))


exit=Button(root,text="EXIT",font=("italic", 16),command=root.destroy)
exit.config(bg="black",fg="white",activebackground="blue",activeforeground="white",width=6,height=3)
exit.pack(pady=(18,8))

check=Checkbutton(root,text="Remember me",bg="white",fg="black").pack(pady=(18,10))
              
root.mainloop()