# Pre-Flight Weight and Balance Calculator
#### Video Demo:  <URL HERE>

# DO NOT USE THIS FOR ACTUAL FLIGHT, DATA MAY BE WILDLY INACCURATE AT PRESENT TIME
#### Description:
This project uses SQL and Python to perform pre-flight Weight and Balance calculations.

This is a proof of concept project, and is intended to be expanded upon as core features get developed.

It asks the user for input, compares input with currently available database, and then asks user for operational info.

When every information is taken into account, it outputs a calculation of weight and balance. It warns the user if weight is excessive, as well as out of bounds Center of Gravity.

## Currently highly experimental.
# File Descriptions: 
## Databases
* aircraft-ledger[cessna, piper, diamond] schema = type_id, type
* cessna[c150, c152, c172] schema = ac_id, registration, bew, cg, moment, year
* piper [TBA]
* diamond [TBA]

## Python Files
* main.py -- Main app, which calls upon various functions to execute calculator
* helpers.py -- Contains dictionaries and functions that maintain code readability in main
* aclist.py -- Contains prototyping for dictionaries which will eventually be used
