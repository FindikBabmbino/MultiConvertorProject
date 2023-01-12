from MphToKm.mph_to_km_func import convert

def mph_to_km_conversion(sg):
    sg.theme("LightGrey5")

    mph_or_km_text = sg.Text("Input Mph or Kmph", key="Label1")
    mph_or_km_input = sg.InputText(key="ConversionInput")

    to_km_button = sg.Button("Convert To Km", key="Kmcon", mouseover_colors="Red")
    to_mph_button = sg.Button("Convert To Mph", key="Mphcon", mouseover_colors="Red")


    layout = [[mph_or_km_text, mph_or_km_input], [to_km_button, to_mph_button]]

    window = sg.Window("Multi Convertor", layout=layout)

    while True:
        event,values = window.read()
        match event:
            case "Kmcon":
                try:
                    result = convert(True,float(values["ConversionInput"]))
                    window["ConversionInput"].update(f"{result}Mph")
                except ValueError:
                    window["ConversionInput"].update("Enter a valid value")

            case "Mphcon":
                try:
                    result = convert(False,float(values["ConversionInput"]))
                    window["ConversionInput"].update(f"{result}Kmph")
                except ValueError:
                    window["ConversionInput"].update("Enter a valid value")

            case sg.WIN_CLOSED:
                break
    window.close()