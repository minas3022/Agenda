from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter import messagebox
import home

class LoginWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("MEUS CONTATOS")
        self.geometry("400x300")

        self.style = Style()

        self.style.configure('Header.TFrame', background='red')

        self.header_frame = Frame(self, style = 'Header.TFrame')
        self.header_frame.pack(fill=X)

        self.style.configure('Header.TLabel', background='red',
        foreground='yellow',font=(NONE, 25))

        self.header_label = Label(self.header_frame, text = "Login",
        style = 'Header.TLabel')
        self.header_label.pack(pady=10)

        self.style.configure('Content.TFrame', background='white')

        self.content_frame = Frame(self, style = 'Content.TFrame')
        self.content_frame.pack(side = TOP, fill = BOTH, expand = TRUE)

        self.login_frame = Frame(self.content_frame,
        height = 100, width = 200, style = 'Content.TFrame')
        self.login_frame.place(relx=.5,rely=.5,anchor=CENTER)

        self.style.configure('Login.TLabel', background='white',font=(NONE,15))

        self.username_label = Label(self.login_frame, text = "Usuário:",
        style='Login.TLabel')
        self.username_label.grid(row=0,column=0)

        self.username_entry = Entry(self.login_frame,
        font=(NONE,15),width=15)
        self.username_entry.grid(row=0,column=1,pady=10)
        self.username_entry.focus()

        self.password_label = Label(self.login_frame, text="Senha:",
        style='Login.TLabel')
        self.password_label.grid(row=1, column=0)

        self.password_entry = Entry(self.login_frame,
        font=(NONE,15),width=15, show = '*')
        self.password_entry.grid(row=1, column=1,pady=10)

        self.style.configure('Login.TButton',font=(NONE,15),width=15)

        self.login_button = Button(self.login_frame, style = 'Login.TButton',
        text = "Login", command = self.login_button_click)
        self.login_button.grid(row=2,column=1,pady=10)

        self.login_button.bind('<Return>', self.login_button_click)

    def login_button_click(self, event=None):
        con = sqlite3.connect('contacts.db')
        cur = con.cursor()
        cur.execute("""select * from Login where Username = '{0}'
        and Password = '{1}'""".format(
            self.username_entry.get(),
            self.password_entry.get()
        ))
        row = cur.fetchone()
        if row is not None:
            self.destroy()
            home.HomeWindow()
        else:
            messagebox.showerror("Error Message",
            "Usuário inválido ou senha")

if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
