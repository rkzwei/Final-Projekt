import aclist
layout = aclist.LAYOUT

#Creates new SQL table for AC
def createAC():
    Name = input("Aircraft Make/Model: ")
    Reg = input("What is the airctaft registration? ")
    ArmFront = input("What is the front Arm? ")
    ArmPax = input("What is the passenger's Arm? ")
    ArmFuel = input("What is the fuel Arm? ")

sqllist = {
    "manufacturer":"SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"

}