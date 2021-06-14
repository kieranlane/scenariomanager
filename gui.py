# Application GUI
# Updated 12/06/2021 by Kieran Lane

# Change Log (v1.0)
# 1.0   Initial script creation

# Imports
import PySimpleGUI as sg
import config as cfg

# Usage 'import gui'
# Examples
#       gui.start_interface()

# SCRIPT START


def start_interface():
    sg.ChangeLookAndFeel('DarkGrey13')

    menu_def = [
        ['File', ['Open', 'Save', 'Exit', 'Properties']],
        ['Help', 'About']
    ]
    layout = [

        # UI Menu
        [
            sg.Menu(
                menu_def,
                tearoff=False
            )
        ],

        # UI Elements
        [
            # Centered UI
            sg.Frame(
                '',
                layout=[

                    # Title and Theme Selector
                    [
                        # Theme Selector
                        sg.Button(
                            image_filename=cfg.get_files('profile'),
                            image_size=(30, 30),
                            image_subsample=40,
                            button_color=None,
                            key='profile'
                        ),

                        sg.Button(
                            image_filename=cfg.get_files('settings'),
                            image_size=(30, 30),
                            image_subsample=40,
                            button_color=None,
                            key='settings'
                        ),

                        # Title
                        sg.Text(
                            'Scenario Manager SE Tools     ',
                            size=(45, 1),
                            justification='center',
                            font=("Helvetica", 25)
                        ),

                        # Theme Selector
                        sg.Button(
                            image_filename=cfg.get_files('theme'),
                            image_size=(30, 30),
                            image_subsample=40,
                            button_color=None,
                            key='theme'
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
                                        size=(8, 1)
                                    ),

                                    sg.InputText(
                                        '*@centurylink.com',
                                        size=(18, 1)
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
                                        size=(18, 1)
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
                                        size=(18, 1)
                                    )
                                ],

                                # Save Button
                                [
                                    sg.Button(
                                        button_text='Save Details',
                                        size=(25, 1)
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
                                        size=(16, 1)
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
                                        size=(16, 1)
                                    )
                                ],

                                # SE Approval
                                [
                                    sg.Text(
                                        'SE Approve Quote',
                                        size=(16, 1)
                                    ),

                                    sg.Checkbox(
                                        '',
                                        size=(11, 1),
                                        key="-IN-",
                                        default=False
                                    )
                                ],

                                # Load Button
                                [
                                    sg.Button(
                                        button_text='Load',
                                        size=(30, 1)
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
                                    sg.InputText('LO', size=(20, 1)),
                                    sg.Button(button_text='Search'),
                                    sg.Button(button_text='Reset')
                                ],

                                # Address Table
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

                                # Address Submit
                                [
                                    sg.Button(
                                        button_text='Add',
                                        size=(25, 1)
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
                                        size=(20, 1)
                                    ),

                                    sg.Button(
                                        button_text='Search'
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
                                        num_rows=cfg.get_aip('length')
                                        # min(25, len(cfg.get_aip('value')))
                                    )
                                ],

                                # Import Button
                                [
                                    sg.Button(
                                        button_text='Import',
                                        size=(25, 1)
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
                                        size=(25, 1)
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
                                        num_rows=cfg.get_spcr('length')
                                        # min(25, len(cfg.get_aip('value')))
                                    )
                                ],

                                # Add SPCR Button
                                [
                                    sg.Text('SPCR #', size=(6, 1), auto_size_text=True, justification='left'),
                                    sg.InputText('DSR123456', size=(20, 1)), sg.Button(button_text='Add SPCR')
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
                                        size=(155, 10)
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

    window = sg.Window('Scenario Manager Tools', layout, default_element_size=(40, 1), grab_anywhere=False)
    event, values = window.read()
    window.close()