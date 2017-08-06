import units
from calc import calculate_cost


def main():

    # Unit Questions
    distance_unit = input(
        "Enter M for miles or K for kilometres:\n").capitalize()

    efficiency_volume_unit = input("If you use " + units.names[distance_unit]
                                   + " per gallon, enter G. If you use "
                                   + units.names[distance_unit]
                                   + " per litre, enter L.\n").capitalize()

    cost_volume_unit = input(
        "If you buy fuel in gallons, enter G, if you buy fuel"
        + " in litres enter L.\n").capitalize()

    cost_unit = input("What is your currency?\n")

    # Calculation Questions
    efficiency = int(input("How many " + units.names[distance_unit]
                           + " per " + units.names[efficiency_volume_unit]
                           + " did you attain?\n"))

    distance = int(input("How many " + units.names[distance_unit]
                         + " did you travel?\n"))

    cost_per_unit = float(input("In " + cost_unit
                                + ", how much does 1 " + units.names[
                                    cost_volume_unit]
                                + " of fuel cost?\n"))

    # If the two volume units are different, we need to
    # convert the efficiency unit to the cost unit
    efficiency = units.equalise_volume_units(efficiency_volume_unit,
                                             cost_volume_unit, efficiency)

    print(calculate_cost(efficiency, distance, cost_per_unit))

main()
