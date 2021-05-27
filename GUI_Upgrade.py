from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
from ContactBookClass import ContactBook

MyContactBook = ContactBook()


root = Tk()


def contact_add():
    FirstName = simpledialog.askstring(
        title='First Name', prompt="What is the first name of the contact: ").lower()
    LastName = simpledialog.askstring(
        title='Last Name', prompt="What is the last name of the contact: ").lower()
    Address = simpledialog.askstring(
        title='Address', prompt="What is the address: ").lower()
    Number = simpledialog.askstring(
        title='Number', prompt="What is the phone number: ").lower()
    Email = simpledialog.askstring(
        title='Email', prompt="What is the email of the contact: ").lower()
    MyContactBook.createcontact(
        FirstName, LastName, Address, Number, Email)


def contact_find():
    fetchcontact = simpledialog.askstring(
        title='Find', prompt="What is the name of the person you wish to find: ").lower()
    print(MyContactBook.contactlookup(fetchcontact))


def contact_delete():
    findcontact = simpledialog.askstring(
        title='Find', prompt="What is the first name of the contact you wish to delete: ").lower()
    Contact = MyContactBook.contactlookup(findcontact)
    for i in range(len(Contact)):
        print(Contact[i][0], Contact[i][1], Contact[i]
              [2], Contact[i][3], Contact[i][4], Contact[i][5])

        confirm_delete = input(
            "Are you sure you wish to delete the above contact: ").lower()

        if confirm_delete == 'yes':
            MyContactBook.deletecontact(
                Contact[0][0])
        else:
            pass


addContact = Button(root, text="Add Contact",
                    bg="green", font=('helvetica', 9, 'bold'), command=contact_add)
addContact.grid(row=5, sticky=W)
findContact = Button(root, text="Find Contact",
                     bg="yellow", font=('helvetica', 9, 'bold'), command=contact_find)
findContact.grid(row=6, sticky=W)
deleteContact = Button(root, text="Delete Contact",
                       bg="red", font=('helvetica', 9, 'bold'), command=contact_delete)
deleteContact.grid(row=7, sticky=W)

label_1 = Label(root, text="First Name", font=('helvetica', 9, 'bold'))
label_2 = Label(root, text="Last Name", font=('helvetica', 9, 'bold'))
label_3 = Label(root, text="Address", font=('helvetica', 9, 'bold'))
label_4 = Label(root, text="Phone Number", font=('helvetica', 9, 'bold'))
label_5 = Label(root, text="Email Address", font=('helvetica', 9, 'bold'))
entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
entry_4 = Entry(root)
entry_5 = Entry(root)


label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
label_3.grid(row=2, sticky=E)
label_4.grid(row=3, sticky=E)
label_5.grid(row=4, sticky=E)


entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)
entry_4.grid(row=3, column=1)
entry_5.grid(row=4, column=1)


def display_FN():
    print(First_Name)


display = Button(root, text="Click to print entry", font=(
    'helvetica', 9, 'bold'), command=display_FN)
display.grid(row=9, sticky=W)

root.mainloop()

# call function that doesn't have any parameters and set inputs


# FirstName = input(
#     "What is the first name of the contact: ").lower()
# LastName = input("What is the last name of the contact: ").lower()
# Address = input("What is the address: ").lower()
# Number = input("What is the phone number: ").lower()
# Email = input("What is the email of the contact: ").lower()
