def calculate_cost(efficiency, distance, cost_per_unit):

    fuel_units_used = distance / efficiency

    return cost_per_unit * fuel_units_used
