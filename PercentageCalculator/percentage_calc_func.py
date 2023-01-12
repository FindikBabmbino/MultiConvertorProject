
def calc(percentage,var):
    full_number_string = percentage_calculator(percentage)
    float_percentage = float(full_number_string)
    return_value = float(var) * float_percentage

    return return_value


def percentage_calculator(percentage_string):
    split_percentage = percentage_string.split()
    split_percentage.insert(0, "0.")
    full_number_string = ""
    for elements in split_percentage:
        full_number_string += elements
    return full_number_string