#!/usr/bin/env Python3      
import PySimpleGUI as sg
import pandas as pd
import addresses as ad
import os

cwd = os.getcwd()
file = '\\test.csv'
df = pd.read_csv(cwd + file, sep=',', engine='python', header=None)
header_list = df.iloc[0].tolist()
data = df[1:].values.tolist()
column_lengths = [6, 30]
button_name = "Load"
address = pd.DataFrame.from_dict({'DC': list(ad.gsm_dict().keys()), 'GSM': list(ad.gsm_dict().values())})
address_list = address.values.tolist()
address_headers = ['DC', 'GSM']

sg.ChangeLookAndFeel('DarkGrey13')

# ------ Menu Definition ------ #      
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
            ['Help', 'About...'], ]      

# ------ Column Definition ------ #      
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

layout = [      

    [sg.Menu(menu_def, tearoff=True)],

    [sg.Frame('', layout=[

        [sg.Text('Scenario Manager SE Tools', size=(60, 1), justification='center', font=("Helvetica", 25))],
        [sg.Text('', size=(16, 2), justification='center')],
        [
            sg.Frame(layout=[
                [sg.Text('Username', size=(8, 1)), sg.InputText('*@centurylink.com', size=(18, 1))],
                [sg.Text('Password', size=(8, 1)), sg.InputText('P@ssW0rd!', size=(18, 1))],
                [sg.Text('APIToken', size=(8, 1)), sg.InputText('ThnksFrThMmrs1', size=(18, 1))],
                [sg.Button(button_text='Save Details', size=(25, 1))]
            ], title='Salesforce Details', element_justification='center', title_location=sg.TITLE_LOCATION_TOP, font=('', 15)
            ),

            sg.Text(' ', size=(16, 2), justification='center', font=('', 10)),

            sg.Frame(layout=[
                [sg.Text('Opportunity', size=(16, 1)), sg.InputText('1234567', size=(16, 1))],
                [sg.Text('Scenario Manager #', size=(16, 1)), sg.InputText('SM123456', size=(16, 1))],
                [sg.Text('SE Approve Quote', size=(16, 1)), sg.Checkbox('', size=(11, 1), key="-IN-", default=False)],
                [sg.Button(button_text='Load', size=(30, 1))]
            ], title='Quote Details', element_justification='center', title_location=sg.TITLE_LOCATION_TOP, font=('', 15))
        ],
        [sg.Text('', size=(16, 2), justification='center')],
        [
            sg.Frame('Add Addresses', layout=[
                [sg.Table(values=address_list,
                          headings=address_headers,
                          display_row_numbers=False,
                          auto_size_columns=False,
                          justification='center',
                          col_widths=column_lengths,
                          num_rows=min(25, len(data)))
                 ],

                [sg.Button(button_text='Add', size=(25, 1))]

            ], element_justification='center', title_location=sg.TITLE_LOCATION_TOP, font=('', 15)),

            sg.Frame('Bulk Import AIPs', layout=[
                [
                    sg.Text('BAN #', size=(6, 1), auto_size_text=True, justification='left'),
                    sg.InputText('S123456', size=(20, 1)), sg.Button(button_text='Search')
                ],

                [sg.Table(values=data,
                          headings=header_list,
                          display_row_numbers=False,
                          auto_size_columns=False,
                          justification='center',
                          col_widths=column_lengths,
                          num_rows=min(25, len(data)))
                 ],

                [sg.Button(button_text='Import', size=(25, 1))]

            ], element_justification='center', title_location=sg.TITLE_LOCATION_TOP, font=('', 15)),

            sg.Frame('Bulk Add SPCR ID', layout=[
                [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(50, 10))]
            ], element_justification='center', title_location=sg.TITLE_LOCATION_TOP, font=('', 15))
        ],

        [sg.Text('', size=(16, 2), justification='center')],

        [sg.Frame('Console', layout=[
            [sg.Output(size=(155, 10))]
        ], element_justification='center', title_location=sg.TITLE_LOCATION_TOP, font=('', 15))
        ]

    ], element_justification='center', border_width=0)]
]


window = sg.Window('Scenario Manager Tools', layout, default_element_size=(40, 1), grab_anywhere=False)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif values["-IN-"] == True:
        button_name = "Load & Approve"

window.close()    

sg.popup('Title',      
            'The results of the window.',      
            'The button clicked was "{}"'.format(event),      
            'The values are', values)