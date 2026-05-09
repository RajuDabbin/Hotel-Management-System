from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from hotel import HotelManagement

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel System - Login")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="#000000")

        # Main login container
        login_frame = Frame(self.root, bg="#1C1C1C", bd=2, relief=RIDGE)
        login_frame.place(x=525, y=150, width=500, height=500)

        Label(login_frame, text="WELCOME BACK", font=("times new roman", 28, "bold"), 
              fg="#D4AF37", bg="#1C1C1C").place(x=0, y=40, relwidth=1)

        # Email
        Label(login_frame, text="EMAIL ADDRESS", font=("arial", 11, "bold"), 
              fg="white", bg="#1C1C1C").place(x=70, y=130)
        self.txt_email = Entry(login_frame, font=("arial", 13), bg="#2C2C2C", 
                               fg="white", insertbackground="white", bd=0)
        self.txt_email.place(x=70, y=160, width=360, height=35)
        # Gold underline
        Frame(login_frame, bg="#D4AF37", height=2).place(x=70, y=195, width=360)

        # Password
        Label(login_frame, text="PASSWORD", font=("arial", 11, "bold"), 
              fg="white", bg="#1C1C1C").place(x=70, y=220)
        self.txt_pass = Entry(login_frame, font=("arial", 13), bg="#2C2C2C", 
                               fg="white", insertbackground="white", bd=0, show="*")
        self.txt_pass.place(x=70, y=250, width=360, height=35)
        # Gold underline
        Frame(login_frame, bg="#D4AF37", height=2).place(x=70, y=285, width=360)

        # Login Button
        btn_login = Button(login_frame, text="LOGIN", command=self.login, 
                           font=("arial", 13, "bold"), bg="#D4AF37", fg="black", 
                           activebackground="#B8860B", cursor="hand2", bd=0)
        btn_login.place(x=70, y=340, width=360, height=45)

        Button(login_frame, text="Register New Account?", command=self.register_window, 
               font=("arial", 10), bg="#1C1C1C", bd=0, fg="#D4AF37", cursor="hand2", 
               activebackground="#1C1C1C", activeforeground="white").place(x=0, y=410, relwidth=1)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                # DATABASE CONFIG: Ensure these match your local MySQL
                conn = mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="raju01", # Ensure this is your actual password
                    database="management"
                )
                cur = conn.cursor()
                cur.execute("select * from users where email=%s and password=%s", 
                            (self.txt_email.get(), self.txt_pass.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Email or Password")
                else:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagement(self.new_window)
                    self.root.withdraw()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Connection Error: {str(es)}")

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("450x550+550+150")
        self.root.config(bg="#1C1C1C")
        
        self.var_fname = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()

        Label(self.root, text="CREATE ACCOUNT", font=("times new roman", 22, "bold"), 
              bg="#1C1C1C", fg="#D4AF37").place(x=0, y=30, relwidth=1)
        
        # Manually placing to avoid .pack() errors
        Label(self.root, text="FIRST NAME", font=("arial", 10, "bold"), 
              bg="#1C1C1C", fg="white").place(x=50, y=100)
        Entry(self.root, textvariable=self.var_fname, font=("arial", 12), 
              bg="#2C2C2C", fg="white", bd=0, insertbackground="white").place(x=50, y=125, width=350, height=30)
        Frame(self.root, bg="#D4AF37", height=2).place(x=50, y=157, width=350)

        Label(self.root, text="EMAIL", font=("arial", 10, "bold"), 
              bg="#1C1C1C", fg="white").place(x=50, y=190)
        Entry(self.root, textvariable=self.var_email, font=("arial", 12), 
              bg="#2C2C2C", fg="white", bd=0, insertbackground="white").place(x=50, y=215, width=350, height=30)
        Frame(self.root, bg="#D4AF37", height=2).place(x=50, y=247, width=350)

        Label(self.root, text="PASSWORD", font=("arial", 10, "bold"), 
              bg="#1C1C1C", fg="white").place(x=50, y=280)
        Entry(self.root, textvariable=self.var_pass, font=("arial", 12), 
              bg="#2C2C2C", fg="white", bd=0, show="*", insertbackground="white").place(x=50, y=305, width=350, height=30)
        Frame(self.root, bg="#D4AF37", height=2).place(x=50, y=337, width=350)
        
        Button(self.root, text="REGISTER NOW", command=self.save_user, bg="#D4AF37", 
               fg="black", font=("arial", 12, "bold"), bd=0, cursor="hand2").place(x=50, y=400, width=350, height=45)

    def save_user(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="raju01", database="management")
            cur = conn.cursor()
            cur.execute("insert into users (fname, email, password) values(%s,%s,%s)", 
                        (self.var_fname.get(), self.var_email.get(), self.var_pass.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Account Registered Successfully!")
            self.root.destroy()
        except Exception as es:
            messagebox.showerror("Error", str(es))

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()