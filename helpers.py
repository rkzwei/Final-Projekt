import aclist
layout = aclist.LAYOUT
import sqlite3
from os import system

#Creates new SQL table for AC
def createAC():
    Name = input("Aircraft Make/Model: ")
    Reg = input("What is the airctaft registration? ")
    ArmFront = input("What is the front Arm? ")
    ArmPax = input("What is the passenger's Arm? ")
    ArmFuel = input("What is the fuel Arm? ")

def update():
    # Connect to the aircraft-ledgers database
    conn = sqlite3.connect("./databases/aircraft-ledger.db")
    cur = conn.cursor()

    # Iterate over the list of manufacturers
    for manufacturer in aclist.ACMAKE:
        # Open the database for the current manufacturer
        manufacturer_db = sqlite3.connect(f"./databases/{manufacturer.lower()}.db")
        manufacturer_cur = manufacturer_db.cursor()

        # Get the list of tables in the manufacturer database
        manufacturer_cur.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
        tables = [table[0] for table in manufacturer_cur.fetchall()]

        # Iterate over the list of tables
        for table in tables:
            # Check if the table name is already present in the aircraft-ledgers database
            cur.execute(f"SELECT type FROM {manufacturer.lower()} WHERE type=?", (table,))
            if not cur.fetchone():
                # Insert the table name into the aircraft-ledgers database
                cur.execute(f"INSERT INTO {manufacturer.lower()} (type) VALUES (?)", (table,))

        # Close the manufacturer database
        manufacturer_db.close()

    # Commit the transaction
    conn.commit()

    # Close the aircraft-ledgers database
    conn.close()


sqllist = {
    "tables":"SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';",
    "listcessna":"SELECT type FROM cessna;",
    "listpiper":"SELECT type FROM piper;",
    "listdiamond":"SELECT type FROM diamond;",
    "listall":"SELECT * FROM {};",
    "createAC":"CREATE TABLE {}(ac_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, registration TEXT NOT NULL UNIQUE, bew TEXT NOT NULL, cg TEXT NOT NULL, moment TEXT NOT NULL, year INTEGER NOT NULL);"
}

def connection(database):
    try:
        conn = sqlite3.connect(f"./databases/{database}.db")
        cur = conn.cursor()
        return cur
    except:
        print(f"Could not connect to {database} database.")

def statement(db, state):
    conn = sqlite3.connect(f"./databases/{db}.db")
    cur = conn.cursor()
    sqlstate = (sqllist[state])
    query = cur.execute(sqlstate)
    return query

def selector(listerino):
    while True:
        try:
            print("\n",listerino,"\n")
            selection = input("Type choice from one from the above: ")
            selection.lower()
            if selection in listerino:
                system('clear')
                #print("Success")
                return selection
            else:
                system('clear')
                print("\nInvalid option.\n")
                choice = "y"
                if input("Would you like to create a new one? y/n\n") == choice:
                    system('clear')
                    return selection.lower()
                
        except Exception as x:
            print(x)
            break

def clean(string):
    string.strip()
    string.upper()
    return string