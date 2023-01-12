from FeetToMeters.feet_to_meters_func import convert


def feet_to_meters_conversion(sg):

    sg.theme("DarkBrown5")

    feet_or_meters_text = sg.Text("Input feet or meters", key="Label1")
    feet_or_meters_input = sg.InputText(key="ConversionInput")

    to_meters_button = sg.Button("Convert To Meters", key="Meterscon", mouseover_colors="Pink")
    to_feet_button = sg.Button("Convert To Feet", key="Feetcon", mouseover_colors="Pink")

    layout = [[feet_or_meters_text, feet_or_meters_input], [to_meters_button, to_feet_button]]

    window = sg.Window("Feet/Meters Convertor",layout=layout)

    while True:
        event,values = window.read()
        match event:
            case "Meterscon":
                try:
                    result = convert(True,float(values["ConversionInput"]))
                    window["ConversionInput"].update(f"Meters: {result}")
                except ValueError:
                    window["ConversionInput"].update("Enter valid value")
            case "Feetcon":
                try:
                    result = convert(False, float(values["ConversionInput"]))
                    window["ConversionInput"].update(f"Feet: {result}")
                except ValueError:
                    window["ConversionInput"].update("Enter valid value")
            case sg.WIN_CLOSED:
                break
    window.close()