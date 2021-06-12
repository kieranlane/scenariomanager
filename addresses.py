# Address Information for frequently used locations
# Updated 09/06/2021 by Kieran Lane

# Change Log (v0.1)
# 0.1   Initial script creation
# 1.0   Script created, gsm_code populated

# Usage 'import addresses as gsm'
# Examples
#       filter_one = gsm.filter_sites('LO1')
#       gsm_codes = gsm.get_all_gsm(filter_one)
#       filter_two = gsm.filter_sites('AA', filter_one)

# SCRIPT START


def gsm_dict():
    # Returns the full default GSM dictionary
    gsm_code = {
        'ZZLO1': 'WKNHEN07',
        'AALO1': 'WKNHEN06',
        'ZZLO4': 'test',
        'ZZLO6': 'test'
    }
    return gsm_code


def get_all_sites(site_dict=gsm_dict()):
    # Returns a list of all sites, within specified dictionary
    # Dictionary defaults to gsm_dict if none specified
    return list(site_dict.keys())


def get_gsm_code(site_name, site_dict=gsm_dict()):
    # Returns the GSM code for a specified site, within specified dictionary
    # Dictionary defaults to gsm_dict if none specified
    return site_dict.get(site_name)


def get_all_gsm(site_dict=gsm_dict()):
    # Returns a list of all GSM codes, within specified dictionary
    # Dictionary defaults to gsm_dict if none specified
    all_gsm = []
    for site in get_all_sites(site_dict):
        all_gsm.append(get_gsm_code(site, site_dict))
    return all_gsm


def filter_sites(search, site_dict=gsm_dict()):
    # Returns a list of all sites matching search, within specified dictionary
    # Dictionary defaults to gsm_dict if none specified
    return dict(filter(lambda item: search in item[0], site_dict.items()))

# SCRIPT END
