#TODO add support for other manufacturers
from os import system
import math
import aclist
import helpers
import sqlite3


""" print("Weight and Balance Calculator\n\n")
try:
    conn = sqlite3.connect("./databases/aircraft-ledger.db")
    cur = conn.cursor()
except:
    print("Could not connect to Aircraft Ledger database.")

manufacturer =(helpers.sqllist["manufacturer"]) 

query = cur.execute(manufacturer)

print([result[0].capitalize() for result in query]) """


""" print([result[0].capitalize() for result in helpers.statement("aircraft-ledger", "manufacturer")]) """
DATA = {
    0:"aircraft-ledger",
    1:"piper",
    2:"cessna",
    3:"diamond"
}

make = list(result[0].capitalize() for result in helpers.statement(DATA[0], "manufacturer"))

while True:
    try:
        print("\n",make,"\n")
        selection= input("Type choice from one from the above: ")
        selection.lower()
        if selection.capitalize() in make:
            break
        else:
            system('clear')
            print("\nInvalid option.\n")
    except Exception as x:
        print(x)
        break



