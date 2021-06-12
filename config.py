import pandas as pd
import addresses as ad
import os


def get_files(filetype):
    cwd = os.getcwd()

    if filetype == 'theme':
        return cwd + '\\theme.png'

    elif filetype == 'aip':
        return cwd + '\\aip.csv'

    elif filetype == 'spcr':
        return cwd + '\\spcr.csv'

    else:
        print('Config.py - get_files, no matching "filetype"')
        return 'ERROR'


def get_aip(tabletype, mode='test'):

    if mode == 'test':
        df = pd.read_csv(get_files('aip'), sep=',', engine='python', header=None)
        header = df.iloc[0].tolist()
        value = df[1:].values.tolist()
    elif mode == 'prod':
        df = 1
        header = 1
        value = 1
    else:
        print('Config.py - get_aip, no matching "mode"')
        return 'ERROR'

    if tabletype == 'header':
        return header
    elif tabletype == 'value':
        return value
    elif tabletype == 'column':
        return [6, 30]
    elif tabletype == 'length':
        return 25
    else:
        print('Config.py - get_aip, no matching "tabletype"')
        return 'ERROR'


def get_addresses(tabletype, mode='initial'):

    if mode == 'initial':
        df = pd.DataFrame.from_dict({'DC': list(ad.gsm_dict().keys()), 'GSM': list(ad.gsm_dict().values())})
        value = df.values.tolist()
        header = ['DC', 'GSM']
    elif mode == 'filter':
        df = 1
        header = 1
        value = 1
    else:
        print('Config.py - get_addresses, no matching "mode"')
        return 'ERROR'

    if tabletype == 'header':
        return header
    elif tabletype == 'value':
        return value
    elif tabletype == 'column':
        return [6, 30]
    elif tabletype == 'length':
        return 25
    else:
        print('Config.py - get_addresses, no matching "tabletype"')
        return 'ERROR'


def get_spcr(tabletype, mode='test'):

    if mode == 'test':
        df = pd.read_csv(get_files('spcr'), sep=',', engine='python', header=None)
        header = df.iloc[0].tolist()
        value = df[1:].values.tolist()
    elif mode == 'prod':
        df = 1
        header = 1
        value = 1
    else:
        print('Config.py - get_spcr, no matching "mode"')
        return 'ERROR'

    if tabletype == 'header':
        return header
    elif tabletype == 'value':
        return value
    elif tabletype == 'column':
        return [6, 30]
    elif tabletype == 'length':
        return 25
    else:
        print('Config.py - get_spcr, no matching "tabletype"')
        return 'ERROR'
