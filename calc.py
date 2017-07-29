def calculateCost(mpg, distance, cost_per_gal):
    gals_used = distance / mpg
    return cost_per_gal * gals_used

mpg = int(input("What MPG did you attain?\n"))
distance = int(input("How far did you travel?\n"))
cost_per_gal = int(input("In pence, how much does 1 gallon of fuel cost?\n"))

print(calculateCost(mpg, distance, cost_per_gal))