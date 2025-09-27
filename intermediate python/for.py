# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for height in areas:
    print(height)


# Change for loop to use enumerate() and update print()
for index,area in enumerate(areas) :
    print("room" + str(index) + ": " + str(area))    


# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x,y in house:
    print("the " + str(x) + " is " + str(y) +" sqm")