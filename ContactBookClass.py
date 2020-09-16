# from ContactClass import Contact
import mysql.connector


class ContactBook:
    def __init__(self):
        self.contactList = []
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="contact_schema"
        )
        self.mycursor = self.mydb.cursor()

    def createcontact(self, FirstName, LastName, StreetAddress, City, State, Zipcode, Number, Email):
        sql = "INSERT INTO contact_book (first_name, last_name, street_address, city, state, zip_code, number, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (FirstName, LastName, StreetAddress,
               City, State, Zipcode, Number, Email)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("1 Record Added to Contact Book")

    def contactlookup(self, lookup):
        query_string = "SELECT * FROM contact_book WHERE first_name = \'" + lookup + "\'"
        self.mycursor.execute(query_string)
        myresult = self.mycursor.fetchall()
        return myresult

    def deletecontact(self, contact_id):
        sql = "DELETE FROM contact_book WHERE Id = " + str(contact_id)
        self.mycursor.execute(sql)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) deleted")
