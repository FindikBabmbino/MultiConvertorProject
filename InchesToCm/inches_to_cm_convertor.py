from InchesToCm.inch_to_cm_functions import conversion

def inch_to_cm_conversion(sg):
    sg.theme("Green")
    inch_or_cm_label = sg.Text("Input inches or cm", key="Label1")
    inch_or_cm_input = sg.InputText(key="ConversionInput")

    to_cm_button = sg.Button("Convert To Cm", key="Cmcon", mouseover_colors="Green")
    to_inch_button = sg.Button("Convert To Inches", key="Inchcon", mouseover_colors="Green")


    layout = [[inch_or_cm_label, inch_or_cm_input], [to_cm_button, to_inch_button]]

    window = sg.Window("Multi Convertor", layout=layout)

    while True:
        event, values = window.read()
        match event:
            case "Cmcon":
                try:
                    results = conversion(True,float(values["ConversionInput"]))
                    window["ConversionInput"].update(f"{results}cm")
                except ValueError:
                    window["ConversionInput"].update(value="Please write a number")
            case "Inchcon":
                try:
                    results = conversion(False,float(values["ConversionInput"]))
                    window["ConversionInput"].update(f"{results}feet")
                except ValueError:
                    window["ConversionInput"].update(value="Please write a number")
            case sg.WIN_CLOSED:
                break
    window.close()

