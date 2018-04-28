Bay1 = ["Missionary","Cannibal","Missionary","Cannibal","Cannibal","Missionary"]
Boat = []
Bay2 = []
Boat_Trips = []
print("Bay One:",Bay1)
while True:
    if len(Bay1) != 0:
       Boat.append("Missionary")
       Boat.append("Cannibal")
       print(Boat)
       Bay1.remove("Missionary")
       Bay1.remove("Cannibal")
       Bay2.append("Missionary")
       Boat.remove("Missionary")
       Bay1.append("Cannibal")
       print(Boat)
    if Bay1.count("Cannibal") >= Bay1.count("Missionary"):
       Boat.remove("Cannibal")
       Boat.append("Missionary")
       Boat.append("Missionary")
       print(Boat)
       Bay1.remove("Missionary")
       Bay1.remove("Missionary")
       Bay2.append("Missionary")
       Bay2.append("Missionary")
       Boat.remove("Missionary")
       print(Boat)
    if Boat.count("Missionary") == 1:
       Bay1.append("Missionary")
       Boat.remove("Missionary")
       Boat.append("Cannibal")
       Boat.append("Cannibal")
       print(Boat)
       Bay2.append("Cannibal")
       Bay2.append("Cannibal")
       Boat.remove("Cannibal")
       Boat.remove("Cannibal")
    if len(Bay2) <= 5:
       Boat.append("Cannibal")
       Boat.append("Missionary")
       print(Boat)
       Boat.remove("Cannibal")
       print(Boat)
       Boat_Trips.append(Boat)
       Boat.remove("Missionary") 
    if Bay1.count("Cannibal") >= 2:
       Boat.append("Cannibal")
       Boat.append("Cannibal")
       print(Boat)
       Bay2.append("Cannibal")
       Boat.remove("Cannibal")
       Boat.remove("Cannibal")
    if len(Bay2) == 6:
        print("Bay Two:",Bay2)
        break