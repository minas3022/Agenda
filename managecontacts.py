from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter import messagebox

class ManageContactsFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.style = Style()
        self.style.configure('TFrame', background = 'white')

        self.pack(side=TOP,fill=BOTH,expand=TRUE)

        self.con = sqlite3.connect('contacts.db')
        self.cur = self.con.cursor()

        self.create_view_all_contacts_frame()

    def create_view_all_contacts_frame(self):
        self.view_all_contacts_frame = Frame(self)
        self.view_all_contacts_frame.place(relx=.5,rely=.5,anchor=CENTER)

        self.style.configure('TButton',font=(NONE, 15))

        self.add_new_contact_button = Button(self.view_all_contacts_frame,
        text="Add New Contact",command=self.add_new_contact_button_click)
        self.add_new_contact_button.grid(row=0,column=1,pady=10,sticky=E)

        self.style.configure('TLabel',background='white',font=(NONE,15))

        self.name_label = Label(self.view_all_contacts_frame,text="Nome:")
        self.name_label.grid(row=1,column=0)

        self.name_entry = Entry(self.view_all_contacts_frame,
        width=50,font=(NONE,15))
        self.name_entry.grid(row=1,column=1,pady=10)
        self.name_entry.bind('<KeyRelease>',
        self.name_entry_key_released)

        self.style.configure('Treeview.Heading', font=(NONE,13))
        self.style.configure('Treeview',font=(NONE,12))

        self.contacts_treeview = Treeview(self.view_all_contacts_frame,
        columns=("name","phone_number","email","city"),show="headings")
        self.contacts_treeview.grid(row=2,column=0,columnspan=2,pady=10)
        self.contacts_treeview.heading("name",text="Nome",anchor=W)
        self.contacts_treeview.heading("phone_number",text="Fone",anchor=W)
        self.contacts_treeview.heading("email", text="Email Id",anchor=W)
        self.contacts_treeview.heading("city", text="Cidade",anchor=W)
        self.contacts_treeview.column('name', width=250)
        self.contacts_treeview.column('phone_number', width=100)
        self.contacts_treeview.column('email', width=250)
        self.contacts_treeview.column('city', width=100)
        self.contacts_treeview.bind('<<TreeviewSelect>>',
        self.contacts_treeview_selection)

        self.fill_contacts_tree_view("select * from Contact")

    def add_new_contact_button_click(self):
        self.view_all_contacts_frame.destroy()
        self.create_add_new_contact_frame()

    def create_add_new_contact_frame(self):
        self.add_new_contact_frame = Frame(self)
        self.add_new_contact_frame.place(relx=.5,rely=.5,anchor=CENTER)

        self.style.configure('TLabel',background='white',font=(NONE,15))

        self.name_label = Label(self.add_new_contact_frame,text="Name:")
        self.name_label.grid(row=0,column=0,sticky=W)

        self.name_entry = Entry(self.add_new_contact_frame,
        font=(NONE,15),width=30)
        self.name_entry.grid(row=0,column=1,pady=10)

        self.phone_number_label = Label(self.add_new_contact_frame, text="Telefone:")
        self.phone_number_label.grid(row=1, column=0,sticky=W)

        self.phone_number_entry = Entry(self.add_new_contact_frame,
        font=(NONE, 15), width=30)
        self.phone_number_entry.grid(row=1, column=1,pady=10)

        self.email_label = Label(self.add_new_contact_frame, text="E-mail:")
        self.email_label.grid(row=2, column=0,sticky=W)

        self.email_entry = Entry(self.add_new_contact_frame,
        font=(NONE, 15), width=30)
        self.email_entry.grid(row=2, column=1,pady=10)

        self.city_label = Label(self.add_new_contact_frame, text="Cidade:")
        self.city_label.grid(row=3, column=0,sticky=W)

        self.city_combobox = Combobox(self.add_new_contact_frame,
        font=(NONE, 15), width=28, values=('Uberlandia','Araguari',
        'Uberaba','Mumbai','Banglore'))
        self.city_combobox.grid(row=3, column=1,pady=10)

        self.add_button = Button(self.add_new_contact_frame,text="Novo",
        width=30,command=self.add_button_click)
        self.add_button.grid(row=4, column=1,pady=10)

    def add_button_click(self):
        self.cur.execute("""select * from Contact 
        where EmailId = '{0}'""".format(
            self.email_entry.get()
        ))
        row = self.cur.fetchone()
        if row is None:
            self.cur.execute("""insert into Contact 
            values('{0}','{1}','{2}','{3}') """.format(
                self.name_entry.get(),
                self.phone_number_entry.get(),
                self.email_entry.get(),
                self.city_combobox.get()
            ))
            self.con.commit()
            messagebox.showinfo("Success Message",
            "Contact details are added successfully")
            self.add_new_contact_frame.destroy()
            self.create_view_all_contacts_frame()
        else:
            messagebox.showerror("Error Message",
            "Contact of {0} email id is already added".format(
            self.email_entry.get()))

    def fill_contacts_tree_view(self, query):
        for contact in self.contacts_treeview.get_children():
            self.contacts_treeview.delete(contact)

        self.cur.execute(query)
        contacts = self.cur.fetchall()

        for contact in contacts:
            self.contacts_treeview.insert("", END, values=contact)

    def name_entry_key_released(self,event):
        self.fill_contacts_tree_view("""select * from Contact 
        where Name like '%{0}%' """.format(
            self.name_entry.get()
        ))

    def create_update_delete_contact_frame(self, contact):
        self.update_delete_contact_frame = Frame(self)
        self.update_delete_contact_frame.place(relx=.5, rely=.5, anchor=CENTER)

        self.style.configure('TLabel', background='white', font=(NONE, 15))

        self.name_label = Label(self.update_delete_contact_frame, text="Name:")
        self.name_label.grid(row=0, column=0, sticky=W)

        self.name_entry = Entry(self.update_delete_contact_frame,
        font=(NONE, 15), width=30)
        self.name_entry.grid(row=0, column=1, pady=10)
        self.name_entry.insert(END, contact[0])

        self.phone_number_label = Label(self.update_delete_contact_frame, text="Phone Number:")
        self.phone_number_label.grid(row=1, column=0, sticky=W)

        self.phone_number_entry = Entry(self.update_delete_contact_frame,
        font=(NONE, 15), width=30)
        self.phone_number_entry.grid(row=1, column=1, pady=10)
        self.phone_number_entry.insert(END, contact[1])

        self.email_label = Label(self.update_delete_contact_frame, text="Email Id:")
        self.email_label.grid(row=2, column=0, sticky=W)

        self.email_entry = Entry(self.update_delete_contact_frame,
        font=(NONE, 15), width=30)
        self.email_entry.grid(row=2, column=1, pady=10)
        self.email_entry.insert(END, contact[2])
        self.old_email = contact[2]

        self.city_label = Label(self.update_delete_contact_frame, text="City:")
        self.city_label.grid(row=3, column=0, sticky=W)

        self.city_combobox = Combobox(self.update_delete_contact_frame,
        font=(NONE, 15), width=28, values=('Noida', 'Greater Noida',
        'Delhi', 'Mumbai', 'Banglore'))
        self.city_combobox.grid(row=3, column=1, pady=10)
        self.city_combobox.set(contact[3])

        self.update_button = Button(self.update_delete_contact_frame,
        text="Update",width=30,command=self.update_button_click)
        self.update_button.grid(row=4, column=1, pady=10)

        self.delete_button = Button(self.update_delete_contact_frame,
        text="Delete",width=30,command=self.delete_button_click)
        self.delete_button.grid(row=5,column=1,pady=10)

    def contacts_treeview_selection(self, event):
        contact = self.contacts_treeview.item(
        self.contacts_treeview.selection())['values']
        self.view_all_contacts_frame.destroy()
        self.create_update_delete_contact_frame(contact)

    def update_button_click(self):
        self.cur.execute("""update Contact set Name = '{0}',
        PhoneNumber = '{1}', EmailId = '{2}', City = '{3}'
        where EmailId = '{4}'""".format(
            self.name_entry.get(),
            self.phone_number_entry.get(),
            self.email_entry.get(),
            self.city_combobox.get(),
            self.old_email
        ))
        self.con.commit()
        messagebox.showinfo("Success Message",
        "Contact details are updated successfully")
        self.update_delete_contact_frame.destroy()
        self.create_view_all_contacts_frame()

    def delete_button_click(self):
        if messagebox.askquestion("Confirmation Message",
        "Are you sure to delete?") == 'yes':
            self.cur.execute("""delete from Contact where EmailId = '{0}'
            """.format(self.old_email))
            self.con.commit()
            messagebox.showinfo("Success Message",
            "Contact details are deleted successfully")
            self.update_delete_contact_frame.destroy()
            self.create_view_all_contacts_frame()



