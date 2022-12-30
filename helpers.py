import aclist
layout = aclist.LAYOUT
import sqlite3

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
    "listdiamond":"SELECT type FROM diamond;"

}


def statement(db, state):
    conn = sqlite3.connect(f"./databases/{db}.db")
    cur = conn.cursor()
    sqlstate = (sqllist[state])
    query = cur.execute(sqlstate)
    return query
