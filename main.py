import units
from units import singular
from calc import calculate_cost
from fetch import fetch_price


def input_str(msg, valid_responses):
    while True:
        response = input(msg + "\n").capitalize()

        if response not in valid_responses:
            print("Not a valid response, please try again.")
            continue
        else:
            return response


def request_distance_unit():
    distance_unit_msg = "Type M for miles or K for kilometres:"
    distance_unit_responses = ["M", "K"]
    return input_str(distance_unit_msg, distance_unit_responses)


def request_volume_unit(distance_unit):
    eff_vol_msg = ("For {0} per gallon, type G. For {0} per litre, type L."
                   .format(units.names[distance_unit]))

    volume_responses = ["G", "L"]

    return input_str(eff_vol_msg, volume_responses)


def request_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Please type a number.")
            continue


def print_cost(cost):
    cost_string = "£{0}".format(round(cost, 2))
    print("\nYour journey cost a total of: ")
    print(cost_string)


def main():
    # Distance msg
    distance_unit = request_distance_unit()

    # Volume msgs
    efficiency_volume_unit = request_volume_unit(distance_unit)

    # Calculation msgs
    efficiency_msg = "How many {0} per {1} did you attain?\n".format(
        units.names[distance_unit],
        singular(units.names[efficiency_volume_unit]))
    distance_msg = "How many {0} did you travel?\n".format(
        units.names[distance_unit])

    efficiency = request_float(efficiency_msg)

    distance = request_float(distance_msg)

    cost_per_litre = fetch_price()

    # If efficiency volume is in gallons, convert to litres
    efficiency = units.convert_volume(efficiency_volume_unit, efficiency)

    total_cost = calculate_cost(efficiency, distance, cost_per_litre)

    print_cost(total_cost)


main()
