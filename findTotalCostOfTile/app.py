def calculateTileArea(w,h):
    return w * h;

def calculateTotalCost(w, h):
    area = w * h
    totalCost = (area / tile) * tileCost
    return totalCost

while True:
    try:
        tileWidth = int(input('Please enter the width of the tile'))
        tileHeight = int(input('Please enter the height of the tile'))
        tileCost = int(input('Please enter the cost per tile'))

        floorWidth = int(input('Please enter the width of the floor'))
        floorHeight = int(input('Please enter the height of the floor'))



        break
    except:
        print('Please enter a correct value')
        continue

tile = calculateTileArea(tileWidth, tileHeight)

cost = calculateTotalCost(floorWidth, floorHeight)

print('Total cost: ' , cost);
# width = float(input("Width of floor: "))
# length = float(input("Length of floor: "))
# cost = float(input("Cost of Tile: "))
#
# print "Cost to tile a %.2f x %.2f floor is: $%.2f" % (width, length, width * length * cost)
