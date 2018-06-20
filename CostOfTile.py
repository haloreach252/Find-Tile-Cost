import string
import time
import math

costPerTile = float(input("Cost per tile: "))
widthOfFloor = float(input("Width of floor: "))
lengthOfFloor = float(input("Length of floor: "))

totalCost = (costPerTile * widthOfFloor * lengthOfFloor)

print("Total cost of tiles: " + str(totalCost))
time.sleep(20)