# Importing the required modules
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup


def aip_html(path):

    # empty list
    data = []

    # for getting the header from
    # the HTML file
    list_header = []
    soup = BeautifulSoup(open(path + '.html'), 'html.parser')
    try:
        header = soup.find_all("table")[0].find("tr")
    except LookupError:
        return 'Invalid BAN'

    for items in header:
        try:
            list_header.append(items.get_text())
        except:
            continue

    # for getting the data
    html_data = soup.find_all("table")[0].find_all("tr")[1:]

    for element in html_data:
        sub_data = []
        for sub_element in element:
            try:
                sub_data.append(sub_element.get_text())
            except:
                continue
        data.append(sub_data)

    for item in data:
        i = 0
        while i < 19:
            if item[i] == '\xa0':
                item[i] = ''
            # print(item[i])
            i += 1

    # Storing the data into Pandas
    # DataFrame
    df_full = pd.DataFrame(data=data, columns=list_header)
    df_filter = df_full[df_full['Parent AIP ID'] == '']
    df_dupe = df_filter.drop(columns=['Parent AIP ID', 'Billing Site Id', 'Billing Site Name', 'Customer Number', 'Add-On Name', 'AIP Quantity', 'Start Bill Date', 'Stop Bill Date', 'AIP MRR', 'Currency', 'Option Definition Name', 'Option Value', 'Option MRR', 'SAVVIS Company'])
    df = df_dupe.drop_duplicates()


    # Converting Pandas DataFrame
    # into CSV file
    df.to_csv(path + '.csv', index=False)
    os.remove(path + '.html')

    return path + '.csv'
