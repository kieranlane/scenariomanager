import PySimpleGUI as sg

def update_title(table, headings):
    for cid, text in zip(COL_HEADINGS, headings):
        table.heading(cid, text=text)

sg.theme("DarkBlue3")

newlist = [[f"Cell ({row+1}, {col+1})" for col in range(8)] for row in range(10)]
COL_HEADINGS = ["Date", "Ref", "ID", "Owner", "Customer", "Price", "Size"]
layout = [
    [sg.Table(values=newlist, headings=COL_HEADINGS, max_col_width=25,
        num_rows=10, alternating_row_color='green', key='-TABLE-',
        enable_events=True, justification='center',)],
    [sg.Button('Update')],
]

window = sg.Window('Table', layout, finalize=True)
table = window['-TABLE-'].Widget
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Update':
        update_title(table, ["Date", "Ref", "ID", "Owner", "Customer", "Price", "Size", "Path"])

window.close()