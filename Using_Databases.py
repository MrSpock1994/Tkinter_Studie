from tkinter import *
import sqlite3


root = Tk()
root.title("Learning Tkinter")

# creating a database
conn = sqlite3.connect("address_book.db")

# creating a cursor
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer )
    """)


# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()
