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

sqllist = {
    "tables":"SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';",
    "listcessna":"SELECT type FROM cessna;",
    "listpiper":"SELECT type FROM piper;",
    "listdiamond":"SELECT type FROM diamond;",
    "listall":"f'SELECT * FROM {type};'",
    "createAC":"CREATE TABLE {} (ac_id INTEGER PRIMARY KEY, registration TEXT NOT NULL UNIQUE, bew TEXT NOT NULL, cg TEXT NOT NULL, moment TEXT NOT NULL, year INTEGER NOT NULL);"

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
            if selection.capitalize() in listerino:
                system('clear')
                print("Success")
                return selection.lower()
            else:
                system('clear')
                print("\nInvalid option.\n")
        except Exception as x:
            print(x)
            break