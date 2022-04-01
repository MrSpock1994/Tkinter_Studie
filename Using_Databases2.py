from tkinter import *
import sqlite3


root = Tk()
root.title("Address database")

# create submit function


def submit():
    # creating a database
    conn = sqlite3.connect("address_book.db")
    # creating a cursor
    cursor = conn.cursor()
    # insert into table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                   {'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                    })
    # commit changes
    conn.commit()
    # close connection
    conn.close()
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    show_records = Toplevel()
    show_records.title("Records")
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(show_records, text=print_records)
    query_label.grid(row=10, column=0, columnspan=2)
    conn.commit()
    conn.close()
    return


def delete_record():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM addresses WHERE oid = " + del_record.get())
    conn.commit()
    conn.close()
    return


def update_record():
    global top
    top = Toplevel()
    top.title("Updating")
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    cursor.execute("SELECT *, oid FROM addresses Where oid = " + edit_record.get())
    record = cursor.fetchall()
    # query_label2 = Label(top, text=record)
    # query_label2.grid(row=0, column=1, columnspan=2)
    global l1top_name
    global l2top_lastname
    global l3top_address
    global l4top_city
    global l5top_state
    global l6top_zipcode
    l1top = Label(top, text="First Name ->")
    l1top.grid(row=1, column=0)
    l1top_name = Entry(top, width=30)
    l1top_name.insert(0, record[0][0])
    l1top_name.grid(row=1, column=1, padx=20)
    l2top = Label(top, text="Last Name ->")
    l2top.grid(row=2, column=0)
    l2top_lastname = Entry(top, width=30)
    l2top_lastname.insert(0, record[0][1])
    l2top_lastname.grid(row=2, column=1)
    l3top = Label(top, text="Address ->")
    l3top.grid(row=3, column=0)
    l3top_address = Entry(top, width=30)
    l3top_address.insert(0, record[0][2])
    l3top_address.grid(row=3, column=1)
    l4top = Label(top, text="City ->")
    l4top.grid(row=4, column=0)
    l4top_city = Entry(top, width=30)
    l4top_city.insert(0, record[0][3])
    l4top_city.grid(row=4, column=1)
    l5top = Label(top, text="State->")
    l5top.grid(row=5, column=0)
    l5top_state = Entry(top, width=30)
    l5top_state.insert(0, record[0][4])
    l5top_state.grid(row=5, column=1)
    l6top = Label(top, text="Zipcode->")
    l6top.grid(row=6, column=0)
    l6top_zipcode = Entry(top, width=30)
    l6top_zipcode.insert(0, record[0][5])
    l6top_zipcode.grid(row=6, column=1)

    adding_btn = Button(top, text="update", command=adding)
    adding_btn.grid(row=7, column=0, columnspan=2,  pady=10, padx=10, ipadx=100)
    conn.commit()
    conn.close()


def adding():
    conn = sqlite3.connect("address_book.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE addresses SET first_name = ?, last_name = ?, address = ?, city = ?, state = ?, zipcode = ? "
                   "WHERE oid = ?",
                    [l1top_name.get(), l2top_lastname.get(), l3top_address.get(), l4top_city.get(), l5top_state.get(),
                     l6top_zipcode.get(), edit_record.get()])
    conn.commit()
    conn.close()
    top.destroy()


L1 = Label(root, text="First Name ->")
L1.grid(row=0, column=0)
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

L2 = Label(root, text="Last Name ->")
L2.grid(row=1, column=0)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

L3 = Label(root, text="Address ->")
L3.grid(row=2, column=0)
address = Entry(root, width=30)
address.grid(row=2, column=1)

L4 = Label(root, text="City ->")
L4.grid(row=3, column=0)
city = Entry(root, width=30)
city.grid(row=3, column=1)

L5 = Label(root, text="State ->")
L5.grid(row=4, column=0)
state = Entry(root, width=30)
state.grid(row=4, column=1)

L6 = Label(root, text="Zipcode ->")
L6.grid(row=5, column=0)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

del_record = Entry(root, width=10)
del_record.grid(row=9, column=0, columnspan=2,  pady=10, padx=10, ipadx=100)

edit_record = Entry(root, width=10)
edit_record.grid(row=11, column=0, columnspan=2,  pady=10, padx=10, ipadx=100)

# create submit button

submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=129)

# create a query button

query_btn = Button(root, text="Show all Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=147)

# delete query button

delete_btn = Button(root, text="Delete a record, insert the ID below", command=delete_record)
delete_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# edit query button
edit_btn = Button(root, text="Edit a record, insert the ID below", command=update_record)
edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=107)

root.mainloop()
