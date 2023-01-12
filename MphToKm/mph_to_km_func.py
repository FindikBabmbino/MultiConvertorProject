KMP_CONVERSION = 1.60934
MPH_CONVERSION = 1.609344

def convert(bool_var,float_var):
    #mph to kmh conversion
    return_val = 0
    if bool_var:
        return_val = float_var * KMP_CONVERSION
    #kmh to mph
    else:
        return_val = float_var / MPH_CONVERSION
        return_val = round(return_val,2)

    return return_val
