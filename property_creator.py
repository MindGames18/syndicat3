# Property Creator Application
import constants
import json

# import PySimpleGUI as sg
#
# sg.theme('BluePurple')
#
# layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
#           [sg.Input(key='-IN-')],
#           [sg.Button('Show'), sg.Button('Exit')]]
#
# window = sg.Window('Pattern 2B', layout)
#
# while True:
#     event, values = window.read()
#     print(event, values)
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break
#     if event == 'Show':
#         # Update the "output" text element to be the value of "input" element
#         window['-OUTPUT-'].update(values['-IN-'])
#
# window.close()
colour_list = ["Brown", "Cyan", "Pink", "Orange", "Red", "Yellow", "Green", "Blue"]
colour_dict = {
    "Brown": 2,
    "Cyan": 3,
    "Pink": 3,
    "Orange": 3,
    "Red": 3,
    "Yellow": 3,
    "Green": 3,
    "Blue": 2
}
default_properties = dict()

for item in colour_list:
    # Defining a list
    default_properties[item] = list()
    # Setting the iter count to 2 if its Brown orBlue property
    if item == "Brown" or item == "Blue":
        loop_iter = 2
    else:
        loop_iter = 3

    for i in range(loop_iter):
        # Temp dict to push into the list
        x = dict()

        x[constants.JSON_PROP_NAME] = input(f"Enter {i} {item} property name")
        x[constants.JSON_PROP_PRICE] = int(input(f"Enter {i} {item} property cost"))
        x[constants.JSON_PROP_MORTGAGE] = int(input(f"Enter {i} {item} property mortgage"))
        x[constants.JSON_RENT_SITE_ONLY] = int(input(f"Enter {i} {item} site only rent"))
        x[constants.JSON_RENT_ONE_HOUSE] = int(input(f"Enter {i} {item} rent with 1 house"))
        x[constants.JSON_RENT_TWO_HOUSE] = int(input(f"Enter {i} {item} rent with 2 house"))
        x[constants.JSON_RENT_THREE_HOUSE] = int(input(f"Enter {i} {item} rent with 3 house"))
        x[constants.JSON_RENT_FOUR_HOUSE] = int(input(f"Enter {i} {item} rent with 4 house"))
        x[constants.JSON_RENT_ONE_HOTEL] = int(input(f"Enter {i} {item} rent with 1 hotel"))
        x[constants.JSON_HOUSE_COST] = int(input(f"Enter {i} {item} Cost of  house"))
        x[constants.JSON_HOTEL_COST] = int(input(f"Enter {i} {item} cost of hotel"))

        default_properties[item].append(x)

with open("defaults.json", 'w')as outputfile:
    json.dump(default_properties, outputfile, indent=4)
