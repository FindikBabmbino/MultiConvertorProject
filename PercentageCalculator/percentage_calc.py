from PercentageCalculator.percentage_calc_func import calc


def calculate_percentage(sg):

    sg.theme("DarkPurple")

    what_is_percent_of_label = sg.Text("What is")
    percentage_input = sg.InputText("Enter Percentage",tooltip="Enter Percentage",key="Percentage")
    percent_label = sg.Text("Percent of?")

    number_input = sg.InputText("Enter Number",tooltip="Input Number",key="Number")

    calculate_button = sg.Button("Calculate",key="CalculateButton",button_color="Pink")

    result_text = sg.Text("",key="ResultText")

    layout=[[what_is_percent_of_label,percentage_input,percent_label,number_input,calculate_button],[result_text]]

    window = sg.Window("Percentage Calculator",layout=layout)

    while True:
        event,values = window.read()
        match event:
            case "CalculateButton":
                try:
                    return_value = calc(values["Percentage"],values["Number"])
                    window["ResultText"].update(f"Result: {return_value}")
                except ValueError:
                    window["Percentage"].update("Please Enter A Valid Percentage")
                    window["Number"].update("Please Enter A Valid Number")
            case sg.WIN_CLOSED:
                break
    window.close()