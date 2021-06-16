import pandas as pd
import addresses as ad
import setup
import os
import json
import automation as at
import process as pr


def config_create(path, directory):
    new_cfg = {
        'sf_username': '',
        'sf_password': '',
        'sf_token': ''
    }

    cfg_json = json.dumps(new_cfg)

    if not os.path.exists(directory):
        os.mkdir(directory)

    with open(path, 'w') as cfg_file:
        cfg_file.write(cfg_json)
        cfg_file.close()


def config_file(config='path', mode='read', value=''):

    divider = setup.what_am_i('divider')

    cwd = os.getcwd()
    path = cwd + divider + 'cfg' + divider + 'config.cfg'
    directory = cwd + divider + 'cfg'

    # If no configuration file, create one
    if not os.path.exists(path):
        config_create(path, directory)

    # Return configuration path
    if config == 'path':
        return path

    # Load JSON file
    with open(path, 'r') as cfg_file:
        cfg = json.load(cfg_file)
        cfg_file.close()

    # Return configuration values
    if mode == 'read':
        if config == 'username':
            return cfg['sf_username']
        if config == 'password':
            return cfg['sf_password']
        if config == 'token':
            return cfg['sf_token']

    # Write configuration values
    elif mode == 'write':
        if config == 'username':
            cfg['sf_username'] = value
        if config == 'password':
            cfg['sf_password'] = value
        if config == 'token':
            cfg['sf_token'] = value

        with open(path, 'w') as cfg_file:
            json.dump(cfg, cfg_file)
            cfg_file.close()


def get_files(filetype):

    divider = setup.what_am_i('divider')
    cwd = os.getcwd()

    if filetype == 'theme':
        return cwd + divider + 'img' + divider + 'theme.png'

    elif filetype == 'aip':
        return cwd + divider + 'csv' + divider + 'aip.csv'

    elif filetype == 'spcr':
        return cwd + divider + 'csv' + divider + 'spcr.csv'

    elif filetype == 'profile':
        return cwd + divider + 'img' + divider + 'profile.png'

    elif filetype == 'settings':
        return cwd + divider + 'img' + divider + 'settings.png'

    else:
        print('Config.py - get_files, no matching "filetype"')
        return 'ERROR'


def get_aip(tabletype='', mode='test', ban='641045'):

    if mode == 'test':
        source = get_files('aip')
    elif mode == 'prod':
        cgi_file = at.bssapp(at.start_driver(), ban)
        source = pr.aip_html(cgi_file)
        if source == 'Invalid BAN':
            return source

    else:
        print('Config.py - get_aip, no matching "mode"')
        return 'ERROR'

    df = pd.read_csv(source, sep=',', engine='python', header=None)
    header = df.iloc[0].tolist()
    value = df[1:].values.tolist()

    if mode == 'prod':
        aips = {'header': header, 'value': value, 'column': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                'length': 25}
        return aips

    else:
        if tabletype == 'header':
            return header
        elif tabletype == 'value':
            return value
        elif tabletype == 'column':
            if mode == 'test':
                # return [6, 30]
                return [8, 8, 20, 8, 8]
        elif tabletype == 'length':
            return 25
        else:
            print('Config.py - get_aip, no matching "tabletype"')
            return 'ERROR'


def get_addresses(tabletype, mode='initial', filters='', dataframe=''):

    if mode == 'initial':
        source = ad.gsm_dict()
    elif mode == 'filter':
        if dataframe == '':
            source = ad.filter_sites(filters)
        else:
            new_dataframe = {}
            for key, loc in dataframe:
                new_dataframe[key] = loc
            source = ad.filter_sites(filters, new_dataframe)
    else:
        print('Config.py - get_addresses, no matching "mode"')
        return 'ERROR'

    df = pd.DataFrame.from_dict({'DC': list(source.keys()), 'GSM': list(source.values())})
    value = df.values.tolist()
    header = ['DC', 'GSM']

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


def se_approve(opportunity, quote):
    return opportunity + quote
