#TODO add support for other manufacturers
from os import system
import math
import aclist
import helpers
import sqlite3

new = False
match = False

selection = ""
art = """
Art by Donovan Blake
__|__
\___/
 | |
 | |
_|_|______________
        /|\ 
      */ | \*
      / -+- \\
  ---o--(_)--o---
    /  0 " 0  \\
  */     |     \*
  /      |      \\
*/       |       \*

"""
print(art)
print("\nWeight and Balance Calculator")

#update databases
helpers.update()

#CONSTANT dictionary with database names
DATA = {
    0:"aircraft-ledger",
    1:"piper",
    2:"cessna",
    3:"diamond"
}
#inverse for easy key lookup
INVDATA = {v: k for k, v in DATA.items()}

#connects to aicraft-ledger
helpers.connection(DATA[0])

#generates list of manufacturers

make = list(result[0] for result in helpers.statement(DATA[0], "tables"))

#prompts user to select one of them
selection = helpers.selector(make)

#saves chosen make for later use
makedb = selection

#turns type into list for iteration
types = []
for i in helpers.statement(DATA[0], (f"list{selection}")):
    types += (i)

#selection variable to current selection
selection = helpers.selector(types)

#connect type database
cur = helpers.connection(DATA[INVDATA[makedb]])

#sets up table SELECT function
typetable = helpers.statement(DATA[INVDATA[makedb]], "tables")

#list of types
results = typetable.fetchall()

#types variable where only first result is in list
types = [result[0] for result in results]

#lists all aircraft from type table #TODO change to registration only
listall = helpers.sqllist["listall"]

if selection in types:
    match = True
    print("Found a match: \n")
    cur.execute(listall.format(selection))
    results = cur.fetchall()
    for row in results:
        print(row[1])
else:
    createAC = helpers.sqllist["createAC"]
    #print(createAC.format(selection))
    cur.execute(createAC.format(selection))
    cur.execute(listall.format(selection))
    results = cur.fetchall()
    for row in results:
        print(row[1])
    #print(cur.execute(listall.format(selection)))

#TODO PROMPT FOR INPUT
reg = ""
while True:
    try:
        reg = input("\nPlease input aircraft registration: ")
        if reg[0] == "N" or reg[0] == "n":
            reg = helpers.clean(reg)
            system("clear")
            break          
        print("\nOnly November A/C supported at this moment.")
        print("\nTo exit, press CTRL + C \n")
    except Exception as x:
        print(x)
        break

#TODO check database for A/C, add if not in there MAYBE: turn this into function
#if reg in (SELECT registration FROM type):
    pass
else:
    while True:
        try:
            BEW = float(input("Aircraft BEW? "))
            if BEW > 0:
                break
            print("Invalid Weight")
        except Exception as x:
            print(x)
    while True:
        try:
            ACInitCG = float(input("Aircraft CG? "))
            if ACInitCG > 0:
                break
            print("Invalid ARM")
        except Exception as x:
            print(x)
    while True:
        try:
            ACMoment = float(input("Aircraft Moment? "))
            if ACMoment > 0:
                break
            print("Invalid Moment")
        except Exception as z:
            print(z)
    print("Added A/C to database!")


#TODO Pull data from database, poke user for input, finish main

#if 1 == 2:
    while True:
        try:
            PWeight = float(input("Your weight? "))
            if PWeight > 0:
                break
            print("Invalid Weight")
        except Exception as y:
            print(y)

    MomentPilot = float(PWeight) * float(ArmPilotFront)
    print(MomentPilot)
    while True:
        try:
            BagWeight = float(input("Passenger Weight? "))
            if BagWeight > 0:
                break
            print("Invalid Weight")
        except Exception as a:
            print(a)
    MomentPassenger = BagWeight * ArmPassenger
    print(MomentPassenger)
    ZeroFuelWeight = [float(PWeight) + float(BEW) + float(BagWeight)]
    ZeroFuelMoment = [float(MomentPilot) + float(MomentPassenger) + float(ACMoment)]
    print("Your Zero Fuel Weight: ")
    print(ZeroFuelWeight)
    print("Your Zero Fuel Moment: ")
    print(ZeroFuelMoment)
    while True:
        try:
            Fuel = float(input("Fuel in Gallons? "))
            if 0 < Fuel <= 48:
                break
            print("Invalid Fuel")
        except Exception as f:
            print(f)
    FuelLbs = (float(Fuel) * 6)
    MomentFuel = FuelLbs * ArmFuel
    print(MomentFuel)
    RampWeight = float(FuelLbs) + float(PWeight) + float(BEW) + float(BagWeight)
    RampMoment = float(MomentFuel) + float(MomentPassenger) + float(MomentPilot) + float(ACMoment)
    print("Your ramp weight is: ")
    print(RampWeight)
    print("Your ramp ARM is: ")
    RampArm = float(RampMoment)/float(RampWeight)
    print(RampArm)
    print("Your ramp moment is: ")
    print(RampMoment)
    while True:
        try:
            RunUpFuel = float(input("Fuel in Lbs for Run-up? "))
            if RunUpFuel > 0:
                break
            print("Invalid Fuel")
        except Exception as f2:
            print(f2)
    TakeoffWeight = float(RampWeight) - float(RunUpFuel)
    TakeoffMoment = float(RampMoment) - float(float(RunUpFuel)*95)
    TakeoffArm: float = float(TakeoffMoment)/(TakeoffWeight)
    print("Your TakeOff Weight is: ")
    print(TakeoffWeight)
    print("Your TakeOff ARM is: ")
    print(TakeoffArm)
    print("Your TakeOff Moment is: ")
    print(TakeoffMoment)
    if TakeoffWeight > 2550:
        print(WindowsError)
        print(">>>>>>>>>>>> Aircraft Overweight <<<<<<<<<<<<")
