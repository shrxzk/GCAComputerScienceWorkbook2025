#Libarys
import sqlite3
from time import sleep

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

#Functions
def append_data(table_name, name_data, lcp_data):
    data_tuple = (name_data, lcp_data)

    if table_name == "undereleven":
        cursor.execute("INSERT INTO undereleven (name, lcp) VALUES (?, ?)", data_tuple)
    elif table_name == "eleventosixteen":
        cursor.execute("INSERT INTO eleventosixteen (name, lcp) VALUES (?, ?)", data_tuple)
    else:
        print("Table name not found")
        return
    print("User Added Successfully")

def delete_data(table_name, name_data):
    data_tuple = (name_data, )

    if table_name == "undereleven":
        cursor.execute("DELETE FROM undereleven WHERE name = ?", data_tuple)
    elif table_name == "eleventosixteen":
        cursor.execute("DELETE FROM eleventosixteen WHERE name = ?", data_tuple)

    print("User Deleted Successfully")

def list_data(table_name):
    try:
        cursor.execute("SELECT * FROM " + table_name)
        rows = cursor.fetchall()

        if not rows:
            print("No data found in table")
        else:
            print(f"Data from {table_name}:")
            for row in rows:
                print(row)

    except sqlite3.Error as error:
        print("Error while connecting to database", error)

def asses_input():
    print("0 - Exit")
    print("1 - Create entry")
    print("2 - Delete entry")
    print("3 - List database\nPlease use unique usernames\n")

    choice :str = input("Enter your choice: ")

    if choice == "1":
        name_data: str = input("Name: ")
        lcp_data: int = int(input("LCP: "))
        yorn: str = input("Under 11? y/n ").lower()
        if yorn == "y":
            append_data("undereleven", name_data, lcp_data)
        elif yorn == "n":
            append_data("eleventosixteen", name_data, lcp_data)

    elif choice == "2":
        name_data: str = input("Name: ")
        yorn: str = input("Under 11? y/n ").lower()
        if yorn == "y":
            delete_data("undereleven", name_data)
        elif yorn == "n":
            delete_data("eleventosixteen", name_data)

    elif choice == "3":
        table_name: str = input("\nTable number\n1. Under 11\n2. 11 - 16\n")
        if table_name == "1":
            list_data("undereleven")
        elif table_name == "2":
            list_data("eleventosixteen")

    else:
        exit()


#Runtime
print("Tennis Managment System")
asses_input()

sleep(5)

conn.commit()
conn.close()

