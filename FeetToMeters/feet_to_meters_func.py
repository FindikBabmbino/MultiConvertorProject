
FEET_TO_METERS_FORMULA = 0.304
METERS_TO_FEET_FORMULA = 3.28084

def convert(bool_var,float_var):
    return_val = 0
    #feet to meters
    if bool_var:
        return_val = float_var*FEET_TO_METERS_FORMULA
    else:
        return_val = float_var*METERS_TO_FEET_FORMULA
    return return_val