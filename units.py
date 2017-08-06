names = {"M": "miles", "K": "kilometres", "G": "gallons", "L": "litres"}

gal_in_litres = 4.54609
litre_in_gals = 0.21997

mile_in_km = 1.60934
km_in_miles = 0.62137


def singular(word):
    return word[0:len(word) - 1]


def convert_volume(efficiency_volume_unit, efficiency):
    if efficiency_volume_unit == "G":
        return efficiency / gal_in_litres
    else:
        return efficiency
