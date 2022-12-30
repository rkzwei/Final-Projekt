#TODO add support for other manufacturers

import math
import aclist
import helpers
import sqlite3


print("Weight and Balance Calculator\n\n")
try:
    conn = sqlite3.connect("./databases/aircraft-ledger.db")
    cur = conn.cursor()
except:
    print("Could not connect to Aircraft Ledger database.")

manufacturer =(helpers.sqllist["manufacturer"]) 

query = cur.execute(manufacturer)

print([result[0].capitalize() for result in query])


