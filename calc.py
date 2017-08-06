import units


def calculate_cost(efficiency, efficiency_volume_unit,
                   distance, cost_per_unit, cost_volume_unit):

    fuel_units_used = distance / efficiency

    return cost_per_unit * fuel_units_used
