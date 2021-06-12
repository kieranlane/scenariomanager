import PySimpleGUI as sg

layout = [[sg.T("")], [sg.T("        "), sg.Button('Hello World', size=(20, 4))], [sg.T("")],
          [sg.T("                   "), sg.Checkbox('Print On:', default=True, key="-IN-")]]

###Setting Window
window = sg.Window('Push my Buttons', layout, size=(300, 200))

###Showing the Application, also GUI functions can be placed here.

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif values["-IN-"] == True:
        print("Hello World")

window.close()