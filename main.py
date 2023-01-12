import PySimpleGUI as sg
import time
from InchesToCm.inches_to_cm_convertor import inch_to_cm_conversion
from MphToKm.mph_to_km import mph_to_km_conversion
from FeetToMeters.feet_to_meters import feet_to_meters_conversion
from PercentageCalculator.percentage_calc import calculate_percentage

sg.theme("Topanga")


time_label = sg.Text("",key = "Time")
inch_cm_conversion_button = sg.Button("Inches/Cm conversion tool",key="InchCmCon")
mph_km_conversion_button = sg.Button("Kmph/Mph conversion tool",key="MphKmCon")
feet_to_meters_button = sg.Button("Feet/Meters conversion tool",key="FeetMetersCon")
percentage_window_button = sg.Button("Percentage Calculator",key="PercentageCalculatorWindow")


layout = [[time_label],[inch_cm_conversion_button,mph_km_conversion_button],[feet_to_meters_button,percentage_window_button]]

window = sg.Window("Multi Convertor",layout=layout)

while True:
    event, value = window.read(timeout = 10)
    window["Time"].update(value = time.strftime("%b %d, %Y %H.%M.%S"))
    match event:
        case "InchCmCon":
            inch_to_cm_conversion(sg)
        case "MphKmCon":
            mph_to_km_conversion(sg)
        case "FeetMetersCon":
            feet_to_meters_conversion(sg)
        case "PercentageCalculatorWindow":
            calculate_percentage(sg)
        case sg.WIN_CLOSED:
            break
window.close()