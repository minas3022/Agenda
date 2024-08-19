from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter import messagebox

class ChangePasswordFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.style = Style()

        self.style.configure('TFrame', background='white')

        self.place(relx=.5, rely=.5, anchor=CENTER)

        self.style.configure('TLabel',background='white',font=(NONE,15))

        self.old_password_label = Label(self,text="Old Password:")
        self.old_password_label.grid(row=0,column=0)

        self.old_password_entry = Entry(self,font=(NONE,15),show='*')
        self.old_password_entry.grid(row=0,column=1,pady=10)

        self.new_password_label = Label(self, text="New Password:")
        self.new_password_label.grid(row=1,column=0)

        self.new_password_entry = Entry(self,font=(NONE,15),show='*')
        self.new_password_entry.grid(row=1,column=1,pady=10)

        self.confirm_password_label = Label(self, text="Confirm Password:")
        self.confirm_password_label.grid(row=2, column=0)

        self.confirm_password_entry = Entry(self,font=(NONE,15),show='*')
        self.confirm_password_entry.grid(row=2,column=1,pady=10)

        self.style.configure('TButton',width=20,font=(NONE,15))

        self.change_password_button = Button(self,text="Change",
        command=self.change_password_button_click)
        self.change_password_button.grid(row=3,column=1,pady=10)

        self.change_password_button.bind('<Return>', self.change_password_button_click)

    def change_password_button_click(self, event=None):
        con = sqlite3.connect('contacts.db')
        cur = con.cursor()
        cur.execute("""select * from Login where Password = '{0}'
        """.format(self.old_password_entry.get()))
        row = cur.fetchone()
        if row is not None:
            new_password = self.new_password_entry.get()
            confirm_password = self.confirm_password_entry.get()
            if new_password == confirm_password:
                cur.execute("""update Login set Password = '{0}'
                where Password = '{1}'
                """.format(
                    self.new_password_entry.get(),
                    self.old_password_entry.get()
                ))
                con.commit()
                messagebox.showinfo("Success Message",
                "Your password is changed successfully")
            else:
                messagebox.showerror("Error Message",
                "New password and confirm password didn't match")
        else:
            messagebox.showerror("Error Message",
            "Incorrect Old Password")


