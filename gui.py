#!/usr/bin/env Python3      
import PySimpleGUI as sg
import pandas as pd
import addresses as ad
import config as cfg

sg.ChangeLookAndFeel('DarkGrey13')

# ------ Menu Definition ------ #      
menu_def = [
    ['File', ['Open', 'Save', 'Exit', 'Properties']],
    ['Help', 'About']
]

layout = [      

    # [sg.Menu(menu_def, tearoff=False)],

    [sg.Frame('', layout=[

        [
            sg.Text('     Scenario Manager SE Tools', size=(55, 1), justification='center', font=("Helvetica", 25)),
            sg.Button(image_filename=cfg.get_files('theme'), image_size=(30, 30), image_subsample=40, button_color=None, key='theme')
        ],

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

                [
                    sg.Text('Filter', size=(6, 1), auto_size_text=True, justification='left'),
                    sg.InputText('LO', size=(20, 1)), sg.Button(button_text='Search'), sg.Button(button_text='Reset')
                ],

                [
                    sg.Table(
                        values=cfg.get_addresses('value'),
                        headings=cfg.get_addresses('header'),
                        display_row_numbers=False,
                        auto_size_columns=False,
                        justification='center',
                        col_widths=cfg.get_addresses('column'),
                        num_rows=cfg.get_addresses('length')
                        # min(25, len(cfg.get_addresses('value')))
                    )
                 ],

                [sg.Button(button_text='Add', size=(25, 1))]

            ], element_justification='center', title_location=sg.TITLE_LOCATION_TOP, font=('', 15)),

            sg.Frame('Bulk Import AIPs', layout=[
                [
                    sg.Text('BAN #', size=(6, 1), auto_size_text=True, justification='left'),
                    sg.InputText('S123456', size=(20, 1)), sg.Button(button_text='Search')
                ],

                [
                    sg.Table(
                        values=cfg.get_aip('value'),
                        headings=cfg.get_aip('header'),
                        display_row_numbers=False,
                        auto_size_columns=False,
                        justification='center',
                        col_widths=cfg.get_aip('column'),
                        num_rows=cfg.get_aip('length')
                        # min(25, len(cfg.get_aip('value')))
                    )
                 ],

                [sg.Button(button_text='Import', size=(25, 1))]

            ], element_justification='center', title_location=sg.TITLE_LOCATION_TOP, font=('', 15)),

            sg.Frame('Bulk Add SPCR ID', layout=[

                [sg.Button(button_text='Load Quote', size=(25, 1))],

                [
                    sg.Table(
                        values=cfg.get_spcr('value'),
                        headings=cfg.get_spcr('header'),
                        display_row_numbers=False,
                        auto_size_columns=False,
                        justification='center',
                        col_widths=cfg.get_spcr('column'),
                        num_rows=cfg.get_spcr('length')
                        # min(25, len(cfg.get_aip('value')))
                    )
                ],

                [
                    sg.Text('SPCR #', size=(6, 1), auto_size_text=True, justification='left'),
                    sg.InputText('DSR123456', size=(20, 1)), sg.Button(button_text='Add SPCR')
                ]

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

event, values = window.read()

window.close()