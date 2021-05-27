from ContactBookClass import ContactBook

MyContactBook = ContactBook()


def MainMenu():
    main_menu_active = True
    while main_menu_active == True:
        welcome_message = input(
            "Welcome to your address book! Would you like to add, find, or delete a contact (add/find/delete/close): ").lower()

        if welcome_message == "add":
            FirstName = input(
                "What is the first name of the contact: ").lower()
            LastName = input("What is the last name of the contact: ").lower()
            StreetAddress = input("What is the street address: ").lower()
            City = input("What is the city: ").lower()
            State = input("What is the state: ").lower()
            Zipcode = input("What is the zip code: ").lower()
            Number = input("What is the phone number: ").lower()
            Email = input("What is the email of the contact: ").lower()
            MyContactBook.createcontact(
                FirstName, LastName, StreetAddress, City, State, Zipcode, Number, Email)

        elif welcome_message == "find":
            fetchcontact = input(
                "Please input the first name of the contact you wish to find: ").lower()
            print(MyContactBook.contactlookup(fetchcontact))

        elif welcome_message == "delete":
            findcontact = input(
                "What is the first name of the contact you wish to delete: ")
            Contact = MyContactBook.contactlookup(findcontact)
            for i in range(len(Contact)):
                print(Contact[i][0], Contact[i][1], Contact[i]
                      [2], Contact[i][3], Contact[i][4], Contact[i][5], Contact[i][6], Contact[i][7], Contact[i][8])

            confirm_delete = input(
                "Are you sure you wish to delete the above contact: ").lower()

            if confirm_delete == 'yes':
                MyContactBook.deletecontact(
                    Contact[0][0])
            else:
                pass

        elif welcome_message == "close":
            main_menu_active = False

        else:
            print("We did not understand your input. Please try again")


MainMenu()
