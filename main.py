import units
from units import singular
from calc import calculate_cost


def input_str(prompt, valid_responses):
    while True:
        response = input(prompt + "\n").capitalize()

        if response not in valid_responses:
            print("Not a valid response, please try again.")
            continue
        else:
            return response


def request_distance_unit():
    distance_unit_prompt = "Enter M for miles or K for kilometres:"
    distance_unit_responses = ["M", "K"]
    return input_str(distance_unit_prompt, distance_unit_responses)


def request_volume_unit(volume_type, distance_unit):
    efficiency_volume_prompt = "If you use " + units.names[distance_unit] \
                               + " per gallon, enter G. If you use " \
                               + units.names[distance_unit] \
                               + " per litre, enter L."
    cost_volume_prompt = "If you buy fuel in gallons, enter G, if you buy fuel" + \
                         " in litres enter L."
    volume_responses = ["G", "L"]

    if volume_type == "efficiency":
        selected_prompt = efficiency_volume_prompt
    else:
        selected_prompt = cost_volume_prompt

    return input_str(selected_prompt, volume_responses)


def request_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue


def main():
    # Distance Prompt
    distance_unit = request_distance_unit()

    # Volume Prompts
    efficiency_volume_unit = request_volume_unit("efficiency", distance_unit)
    cost_volume_unit = request_volume_unit("cost", distance_unit)

    # Cost Prompt
    cost_unit = input("What is your currency?\n")

    # Calculation Prompts
    efficiency_prompt = "How many " + units.names[distance_unit] + " per " \
                        + singular(units.names[efficiency_volume_unit]) \
                        + " did you attain?\n"
    distance_prompt = "How many " + units.names[distance_unit] \
                      + " did you travel?\n"
    cost_prompt = "In " + cost_unit + ", how much does 1 " + \
                  singular(units.names[cost_volume_unit]) + " of fuel cost?\n"

    efficiency = request_float(efficiency_prompt)

    distance = request_float(distance_prompt)

    cost_per_unit = request_float(cost_prompt)

    # If the two volume units are different, we need to
    # convert the efficiency unit to the cost unit
    efficiency = units.equalise_volume_units(efficiency_volume_unit,
                                             cost_volume_unit, efficiency)

    # Printer
    total_cost = calculate_cost(efficiency, distance, cost_per_unit)
    print("\nYour journey cost a total of: ")
    print(str(round(total_cost, 2)) + " " + cost_unit)


main()
