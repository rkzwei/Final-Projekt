# Pre-Flight Weight and Balance Calculator
#### Video Demo:  <https://youtu.be/B5bAPj4-gGo>

# DO NOT USE THIS FOR ACTUAL FLIGHT, DATA MAY BE WILDLY INACCURATE AT PRESENT TIME
#### Description:
This project uses SQL and Python to perform pre-flight Weight and Balance calculations.

This is a proof of concept project, and is intended to be expanded upon as core features get developed.

It asks the user for input, compares input with currently available database, and then asks user for operational info.

When every information is taken into account, it outputs a calculation of weight and balance. It warns the user if weight is excessive, as well as out of bounds Center of Gravity.

As it stands, this project is a database management CLI software.
## Currently highly experimental.
# File Descriptions: 
## Databases
* aircraft-ledger[cessna, piper, diamond] schema = type_id, type
* cessna[c150, c152, c172] schema = ac_id, registration, bew, maxweight, cg, moment, year
* piper [TBA]
* diamond [TBA]

## Python Files
* main.py -- Main app, which calls upon various functions to execute calculator
* helpers.py -- Contains dictionaries and functions that maintain code readability in main
* aclist.py -- Contains prototyping for dictionaries which will eventually be used

# RUN-THROUGH:
keys:
* bg: running in the backgroung
* in: user input
* lg: logic gate

program starts with beautiful ASCII art

introduces itself

bg: updates the main database to act accordingly with the smaller databases

bg: connects to main database, iterates over it

prints the tables from the main database:

* piper
* cessna
* diamond

in: select manufacturer from the above

lg: IF in above list, continue // ELSE print invalid, prompt user if they want to add it to database

bg: takes user input, uses it to select database file, iterates over it

prints the types from manufacturer.db

in: select type

lg: ""

bg: takes user input, if not in the database, creates it in the manufacturer.db
bg: iterates over manufacturer.db, if found, prints registration column from all rows

prints registration columns

prompts user for Aircraft Registration. 

If A/C is in the list, it will pull it's data and begin prompting user for calculation values.
Else, it'll prompt users for the A/C values and return to the above line.

TODO: Finish calculating values

IF aircraft is overweight after all calculations, prints a warning to user.

TODO: Acquire METAR of requested airport

TODO: Integrate runway performance into calculation, based on METAR data above

Project was based off earlier version of same idea, where only the Piper Archer II was supported.

Acknowledgments to OpenAI for helping with debugging, to RaceCity for the aircraft data, and to my 2020 self who didn't give up.

# DO NOT USE THIS FOR ACTUAL FLIGHT, DATA MAY BE WILDLY INACCURATE AT PRESENT TIME

This is a WIP version of the calculator, as of Dec 31 2022. 

# Inspiration

I was a flight dispatcher for almost 2 years, and I always had a blast watching students complete their pre-flight sheets, because most of them would take a long time filling out just the W&B portion.

It requires some math, which you'd normally use a regular calculator and paper referencing for.
You needed to find the arm, the moment, the cg within the aircraft's Pilot Information Manual to complete it.

Somewhere towards the end of my stay at that flight school, I made a calculator in python, specifically for the archer. 

It was impractical and I never truly used it, but always dreamed of actually using it.

This is my pet project towards that small dream.