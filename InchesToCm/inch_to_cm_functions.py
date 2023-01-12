def conversion(bool_var,float_value):
    if bool_var:
        return float_value*2.54
    else:
        new_value = float_value * 0.393701
        new_value = round(new_value, 2)
        return new_value