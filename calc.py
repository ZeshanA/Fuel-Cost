def calculateCost(efficiency, distance, cost_per_unit):
    units_used = distance / efficiency
    return cost_per_unit * units_used

unit_names = {"M": "miles", "K": "kilometres", "G": "gallons", "L": "litres"}

# Unit Questions
distance_unit = input("Enter M for miles or K for kilometres:\n").capitalize()

efficiency_volume_unit = input("If you use " + unit_names[distance_unit]
                               + " per gallon, enter G. If you use "
                               + unit_names[distance_unit]
                               + " per litre, enter L.\n").capitalize()

cost_volume_unit = input("If you buy fuel in gallons, enter G, if you buy fuel"
                         + " in litres enter L.\n").capitalize()

cost_unit = input("What is your currency?\n")

# Calculation Questions
efficiency = int(input("How many " + unit_names[distance_unit]
                       + " per "+ unit_names[efficiency_volume_unit]
                       + " did you attain?\n"))

distance = int(input("How many " + unit_names[distance_unit]
                     + " did you travel?\n"))

cost_per_unit = float(input("In " + cost_unit
                      + ", how much does 1 " + unit_names[cost_volume_unit]
                      + " of fuel cost?\n"))

print(calculateCost(efficiency, distance, cost_per_unit))
