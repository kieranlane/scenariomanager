# Application GUI
# Updated 12/06/2021 by Kieran Lane

# Change Log (v1.0)
# 1.0   Initial script creation

# Imports
import PySimpleGUI as sg
import config as cfg
import webauto as web

# Usage 'import gui'
# Examples
#       gui.start_interface()

# Interface Keys
# -BTN_PROFILE-
# -BTN_SETTINGS-
# -BTN_THEME-
#
# -IN_USERNAME-
# -IN_PASSWORD-
# -IN_TOKEN-
# -BTN_SFDETAILS-
#
# -IN_OPP-
# -IN_QUOTE-
# -CHK_SEAPPROVE-
# -BTN_QUOTEDETAILS-
#
# -IN_FILTER-
# -BTN_FILTER-
# -BTN_CLEARFILTER-
# -TBL_ADDRESSES-
# -BTN_ADDRESSES-
#
# -IN_BAN-
# -BTN_BANSEARCH-
# -TBL_AIPS-
# -BTN_AIPS-
#
# -BTN_LOADQUOTE-
# -TBL_QUOTELINES-
# -IN_DSR-
# -BTN_SPCR-
#
# -OUT_CONSOLE-

# SCRIPT START


# def start_interface():

settings_confirm = False
double_filter = False

sg.ChangeLookAndFeel('DarkGrey13')

# menu_def = [
    # ['File', ['Open', 'Save', 'Exit', 'Properties']],
    # ['Help', 'About']
# ]
layout = [

    # UI Menu
    # [
    #     sg.Menu(
    #         menu_def,
    #         tearoff=False
    #     )
    # ],

    # UI Elements
    [
        # Centered UI
        sg.Frame(
            '',
            layout=[

                # Title and Theme Selector
                [
                    # Settings
                    sg.Button(
                        image_filename=cfg.get_files('settings'),
                        image_size=(30, 30),
                        image_subsample=40,
                        button_color=None,
                        key='-BTN_SETTINGS-'
                    ),

                    # Title
                    sg.Text(
                        'Scenario Manager SE Tools',
                        size=(50, 1),
                        justification='center',
                        font=("Helvetica", 25)
                    ),

                    # Theme Selector
                    sg.Button(
                        image_filename=cfg.get_files('theme'),
                        image_size=(30, 30),
                        image_subsample=40,
                        button_color=None,
                        key='BTN_THEME'
                    )
                ],

                # Section Divider
                [
                    sg.Text(
                        '',
                        size=(16, 2),
                        justification='center'
                    )
                ],

                # Salesforce Details and Quote Details Sections
                [
                    # Salesforce Details
                    sg.Frame(
                        layout=[
                            # Username
                            [
                                sg.Text(
                                    'Username',
                                    size=(8, 1),
                                ),

                                sg.InputText(
                                    '*@centurylink.com',
                                    size=(18, 1),
                                    key='-IN_USERNAME-'
                                )
                            ],

                            # Password
                            [
                                sg.Text(
                                    'Password',
                                    size=(8, 1)
                                ),

                                sg.InputText(
                                    'P@ssW0rd!',
                                    size=(18, 1),
                                    key='-IN_PASSWORD-'
                                )
                            ],

                            # API Token
                            [
                                sg.Text(
                                    'APIToken',
                                    size=(8, 1)
                                ),

                                sg.InputText(
                                    'ThnksFrThMmrs1',
                                    size=(18, 1),
                                    key='-IN_TOKEN-'
                                )
                            ],

                            # Save Button
                            [
                                sg.Button(
                                    button_text='Save Details',
                                    size=(25, 1),
                                    key='-BTN_SFDETAILS-'
                                )
                            ]
                        ],
                        title='Salesforce Details',
                        element_justification='center',
                        title_location=sg.TITLE_LOCATION_TOP,
                        font=('', 15)
                    ),

                    # Section Divider
                    sg.Text(
                        ' ',
                        size=(16, 2),
                        justification='center',
                        font=('', 10)
                    ),

                    # Quote Details
                    sg.Frame(
                        layout=[
                            # Opportunity
                            [
                                sg.Text(
                                    'Opportunity',
                                    size=(16, 1)
                                ),

                                sg.InputText(
                                    '1234567',
                                    size=(16, 1),
                                    key='-IN_OPP-'
                                )
                            ],

                            # Quote Details
                            [
                                sg.Text(
                                    'Scenario Manager #',
                                    size=(16, 1)
                                ),

                                sg.InputText(
                                    'SM123456',
                                    size=(16, 1),
                                    key='-IN_QUOTE-'
                                )
                            ],

                            # SE Approval
                            [
                                sg.Text(
                                    'Above information is needed for all sections',
                                    size=(31, 1)
                                )
                            ],

                            # Load Button
                            [
                                sg.Button(
                                    button_text='SE Approve',
                                    size=(30, 1),
                                    key='-BTN_SEAPPROVE-'
                                )
                            ]
                        ],
                        title='Quote Details',
                        element_justification='center',
                        title_location=sg.TITLE_LOCATION_TOP,
                        font=('', 15)
                    )
                ],

                # Section Divider
                [
                    sg.Text(
                        '',
                        size=(16, 2),
                        justification='center'
                    )
                ],

                # Add Addresses, Bulk Import of AIPs, Bulk Add SPCR ID
                [
                    # Add Address
                    sg.Frame(
                        'Add Addresses',
                        layout=[
                            # Address Filtering
                            [
                                sg.Text('Filter', size=(6, 1), auto_size_text=True, justification='left'),
                                sg.InputText('LO', size=(20, 1), key='-IN_FILTER-'),
                                sg.Button(button_text='Filter', key='-BTN_FILTER-'),
                                sg.Button(button_text='Reset', key='-BTN_CLEARFILTER-')
                            ],

                            # Address Table
                            [
                                sg.Table(
                                    values=cfg.get_addresses('value'),
                                    headings=cfg.get_addresses('header'),
                                    display_row_numbers=False,
                                    auto_size_columns=False,
                                    justification='center',
                                    # select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                                    col_widths=cfg.get_addresses('column'),
                                    num_rows=cfg.get_addresses('length'),
                                    key='-TBL_ADDRESSES-'
                                    # min(25, len(cfg.get_addresses('value')))
                                )
                             ],

                            # Address Submit
                            [
                                sg.Button(
                                    button_text='Add',
                                    size=(25, 1),
                                    key='-BTN_ADDRESSES-'
                                )
                            ]
                        ],
                        element_justification='center',
                        title_location=sg.TITLE_LOCATION_TOP,
                        font=('', 15)
                    ),

                    # Bulk Import AIPs
                    sg.Frame(
                        'Bulk Import AIPs',
                        layout=[
                            # BAN Search
                            [
                                sg.Text(
                                    'BAN #',
                                    size=(6, 1),
                                    auto_size_text=True,
                                    justification='left'
                                ),

                                sg.InputText(
                                    'S123456',
                                    size=(20, 1),
                                    key='-IN_BAN-'
                                ),

                                sg.Button(
                                    button_text='Search',
                                    key='-BTN_BANSEARCH-'
                                )
                            ],

                            # AIP Table
                            [
                                sg.Table(
                                    values=cfg.get_aip('value'),
                                    headings=cfg.get_aip('header'),
                                    display_row_numbers=False,
                                    auto_size_columns=False,
                                    justification='center',
                                    col_widths=cfg.get_aip('column'),
                                    num_rows=cfg.get_aip('length'),
                                    key='-TBL_AIPS-'
                                    # min(25, len(cfg.get_aip('value')))
                                )
                            ],

                            # Import Button
                            [
                                sg.Button(
                                    button_text='Import',
                                    size=(25, 1),
                                    key='-BTN_AIPS-'
                                )
                            ]

                        ],
                        element_justification='center',
                        title_location=sg.TITLE_LOCATION_TOP,
                        font=('', 15)
                    ),

                    # Bulk Add SPCR ID
                    sg.Frame(
                        'Bulk Add SPCR ID',
                        layout=[
                            # Load Quote Lines
                            [
                                sg.Button(
                                    button_text='Load Quote',
                                    size=(25, 1),
                                    key='-BTN_LOADQUOTE-'
                                )
                            ],

                            # SPCR Table
                            [
                                sg.Table(
                                    values=cfg.get_spcr('value'),
                                    headings=cfg.get_spcr('header'),
                                    display_row_numbers=False,
                                    auto_size_columns=False,
                                    justification='center',
                                    col_widths=cfg.get_spcr('column'),
                                    num_rows=cfg.get_spcr('length'),
                                    key='-TBL_QUOTELINES-'
                                    # min(25, len(cfg.get_aip('value')))
                                )
                            ],

                            # Add SPCR Button
                            [
                                sg.Text('SPCR #', size=(6, 1), auto_size_text=True, justification='left'),
                                sg.InputText('DSR123456', size=(20, 1), key='-IN_DSR-'),
                                sg.Button(button_text='Add SPCR', key='-BTN_SPCR-')
                            ]

                        ],
                        element_justification='center',
                        title_location=sg.TITLE_LOCATION_TOP,
                        font=('', 15)
                    )
                ],

                # Section Divider
                [
                    sg.Text(
                        '',
                        size=(16, 2),
                        justification='center'
                    )
                ],

                # Console
                [
                    sg.Frame(
                        'Console',
                        layout=[

                            # Console Element
                            [
                                sg.Output(
                                    size=(155, 10),
                                    key='-OUT_CONSOLE-'
                                )
                            ]
                        ],
                        element_justification='center',
                        title_location=sg.TITLE_LOCATION_TOP,
                        font=('', 15)
                    )
                ]

            ],
            element_justification='center',
            border_width=0
        )
    ]
]

window = sg.Window('Scenario Manager Tools', layout, default_element_size=(40, 1), grab_anywhere=False, finalize=True)

# Updating default values from saved configuration
window['-IN_USERNAME-'].update(cfg.config_file('username', 'read', ''))
window['-IN_PASSWORD-'].update(cfg.config_file('password', 'read', ''))
window['-IN_TOKEN-'].update(cfg.config_file('token', 'read', ''))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    # print(event, values)
    # sg.Print(window['-TBL_ADDRESSES-'].get())

    # Setup Details
    if event == '-BTN_SFDETAILS-':
        cfg.config_file('username', 'write', values['-IN_USERNAME-'])
        cfg.config_file('password', 'write', values['-IN_PASSWORD-'])
        cfg.config_file('token', 'write', values['-IN_TOKEN-'])
        print("Details have been successfully saved to " + cfg.config_file('path', 'read', ''))
        print("These values will be loaded at next launch!")
        print("Please note, manually editing this file may cause issues, delete if you encounter issues.")
        print("")
    if event == '-BTN_SEAPPROVE-':
        test = cfg.se_approve(values['-IN_OPP-'], values['-IN_QUOTE-'])
        print(test)
    if event == '-BTN_SETTINGS-':
        if not web.driver_setup() or settings_confirm:
            if not web.driver_setup():
                print("Chrome Web Driver appears to be missing, please wait...")
            print("Starting download of latest chrome driver")
            print("OS identified as " + web.what_am_i())
            web.latest_download()
            settings_confirm = False
            print("Setup complete")
            print("")
        elif web.driver_setup():
            print("Chrome Web Driver appears to be present, you can update by clicking the 'Settings' button again")
            print("")
            settings_confirm = True

    # Add Addresses
    if event == '-BTN_FILTER-':
        if not double_filter:
            window['-TBL_ADDRESSES-'].update(
                values=cfg.get_addresses('value', 'filter', values['-IN_FILTER-'], '')
            )
            double_filter = True

        elif double_filter:
            window['-TBL_ADDRESSES-'].update(
                values=cfg.get_addresses('value', 'filter', values['-IN_FILTER-'], window['-TBL_ADDRESSES-'].get())
            )
    if event == '-BTN_CLEARFILTER-':
        window['-TBL_ADDRESSES-'].update(
            values=cfg.get_addresses('value')
        )
        double_filter = False
    if event == '-BTN_ADDRESSES-':
        selected_values = []

        full_table = window['-TBL_ADDRESSES-'].get()
        selected = values['-TBL_ADDRESSES-']

        for i in selected:
            selected_values.append(full_table[i][1])

        print(selected_values)
        print("INSERT FUNCTION TO USE THESE VALUES TO ADD ADDRESSES")
        print("")

    # Import AIPs
    if event == '-BTN_BANSEARCH-':
        ban = values['-IN_DSR-']
        print("INSERT FUNCTION TO GET AIPs UNDER BAN " + ban + " AND ADD TO TABLE")
        print("")
    if event == '-BTN_AIPS-':
        selected_values = []

        full_table = window['-TBL_AIPS-'].get()
        selected = values['-TBL_AIPS-']

        for i in selected:
            selected_values.append(full_table[i][0])

        print(selected_values)
        print("INSERT FUNCTION TO USE THESE VALUES TO IMPORT AIPS")
        print("")

    # Add SPCR
    if event == '-BTN_LOADQUOTE-':
        quote = values['-IN_QUOTE-']
        print("INSERT FUNCTION TO GET LINE ITEMS IN QUOTE " + quote + " AND ADD TO TABLE")
        print("")
    if event == '-BTN_SPCR-':
        selected_values = []
        spcr = values['-IN_DSR-']

        full_table = window['-TBL_QUOTELINES-'].get()
        selected = values['-TBL_QUOTELINES-']

        for i in selected:
            selected_values.append(full_table[i][0])

        print(selected_values)
        print("INSERT FUNCTION TO ADD " + spcr + " SPCR ID TO THESE SELECTED LINES")
        print("")

window.close()
