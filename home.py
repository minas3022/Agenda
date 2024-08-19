from tkinter import *
from tkinter.ttk import *
import login
import changepassword
import managecontacts

class HomeWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Home")
        self.state("zoomed")

        self.style = Style()

        self.style.configure('Header.TFrame', background = 'blue')

        self.header_frame = Frame(self, style = 'Header.TFrame')
        self.header_frame.pack(side=TOP,fill=X)

        self.style.configure('Header.TLabel',background='blue',
        foreground='white',font=(NONE,25))

        self.header_label = Label(self.header_frame,text="Meu livro de contatos",
        style='Header.TLabel')
        self.header_label.pack(pady=10)

        self.navigation_frame = Frame(self, style = 'Header.TFrame')
        self.navigation_frame.pack(side=LEFT,fill=Y)

        self.style.configure('Navigation.TButton',width=15,font=(NONE,15))

        self.manage_contacts_button = Button(self.navigation_frame,
        text="Manage Contacts",style='Navigation.TButton',
        command = self.manage_contacts_button_click)
        self.manage_contacts_button.pack(ipady=10,pady=1)

        self.change_password_button = Button(self.navigation_frame,
        text="Change Password",style='Navigation.TButton',
        command=self.change_password_button_click)
        self.change_password_button.pack(ipady=10,pady=1)

        self.logout_button = Button(self.navigation_frame,
        text = "Logout",style='Navigation.TButton',
        command=self.logout_button_click)
        self.logout_button.pack(ipady=10,pady=1)

        self.style.configure('Content.TFrame',background='white')

        self.content_frame = Frame(self,style='Content.TFrame')
        self.content_frame.pack(side=TOP,fill=BOTH,expand=TRUE)

        managecontacts.ManageContactsFrame(self.content_frame)

    def logout_button_click(self):
        self.destroy()
        login.LoginWindow()

    def change_password_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        changepassword.ChangePasswordFrame(self.content_frame)

    def manage_contacts_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        managecontacts.ManageContactsFrame(self.content_frame)
