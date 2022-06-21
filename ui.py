import string
import tkinter as tk
import numpy as np
import machine
import plugBoard
import rotorWheel
import Enigma_1_properties
import PySimpleGUI as sg
# prepare the machine components:

propertyPairs = [(Enigma_1_properties.wheel1, Enigma_1_properties.wheel1Notch),
                 (Enigma_1_properties.wheel2, Enigma_1_properties.wheel2Notch),
                 (Enigma_1_properties.wheel3, Enigma_1_properties.wheel3Notch),
                 (Enigma_1_properties.wheel4, Enigma_1_properties.wheel4Notch),
                 (Enigma_1_properties.wheel5, Enigma_1_properties.wheel5Notch)]

reflectorA = Enigma_1_properties.reflectorA
reflectorB = Enigma_1_properties.reflectorB
reflectorC = Enigma_1_properties.reflectorC

reflectors = [reflectorA, reflectorB, reflectorC]

sg.theme('DarkBlack1')

wheelNames =["I", "II", "III", "IV", "V"]
wheelPositions = list(string.ascii_uppercase)

column_to_be_centered = [
        [sg.Text("Text to be encrypted:"),
           sg.Multiline(size=(40,10), font='Tahoma 13', key='-IN-', autoscroll=True)
           ],
          [sg.Text("Select Rotors : ")
              , sg.Combo(wheelNames, default_value='I', key='-WHEEL1-')
              , sg.Combo(wheelNames, default_value='II', key='-WHEEL2-')
              , sg.Combo(wheelNames, default_value='III', key='-WHEEL3-')],
          [sg.Text("Select Rotor Settings : ")
              , sg.Combo(wheelPositions, default_value='A', key='-SETTING1-')
              , sg.Combo(wheelPositions, default_value='A', key='-SETTING2-')
              , sg.Combo(wheelPositions, default_value='A', key='-SETTING3-')],
          [sg.Text("Pick a Reflector : "),
           sg.Combo(["A", "B", "C"], default_value='A', key='-Reflector-')],
          [sg.Button("Encode"), sg.Button("Plug Board")],
          [sg.Text("Output of Enigma:"),
              sg.Multiline(size=(40, 10), disabled=True, font='Tahoma 13', key='-OUTPUT-', autoscroll=True)],
          [sg.Button("Exit")]
]


layout = [
          [sg.Push(), sg.Column(column_to_be_centered,element_justification='c'), sg.Push()]
          ]




def stringToValue(input):
    converter = {
        'I': 0,
        'II': 1,
        'III': 2,
        'IV': 3,
        'v': 4
    }

    if input in ['I', 'II', 'III', 'IV', 'V']:
        return converter.get(input)
    else:
        return ord(input.lower()) - 97


def open_window():
    plugLayout = [[sg.Text("Nothing here yet!", key='-plugMessage-')],[sg.Button("Exit")]
    ]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()





# Create the window
window = sg.Window("Enigma", layout, finalize=True)
window['-IN-'].bind("<Return>", "_Enter")



while True:  # Event Loop
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Plug Board':
        open_window()

    if event == 'Encode' or event == "-IN-" + "_Enter":
        position1 = stringToValue(values['-WHEEL1-'])
        position2 = stringToValue(values['-WHEEL2-'])
        position3 = stringToValue(values['-WHEEL3-'])

        wheel1 = rotorWheel.RotorWheel(stringToValue(values['-SETTING1-']), propertyPairs[position1][0],
                                       propertyPairs[position1][1])
        wheel2 = rotorWheel.RotorWheel(stringToValue(values['-SETTING3-']), propertyPairs[position2][0],
                                       propertyPairs[position2][1])
        wheel3 = rotorWheel.RotorWheel(stringToValue(values['-SETTING3-']), propertyPairs[position3][0],
                                       propertyPairs[position3][1])

        reflector = reflectors[stringToValue(values['-Reflector-'])]

        # create plugboard!!!

        EnigmaEncode = machine.Machine([wheel1, wheel2, wheel3], None, reflector)

        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(EnigmaEncode.encryptText(values['-IN-']))


window.close()
