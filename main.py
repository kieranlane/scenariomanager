# Scenario Manager Tools
# Updated 09/06/2021 by Kieran Lane

# Change Log (v1.0)
# 1.0   Initial script creation

# Imports
import addresses as ad
import webauto as wa
import gui

# Notes:
#   Add required addresses to quote
#       Automatically select these based on imported AIPs?
#   Importing multiple AIPs onto quote
#   Adding SPCR ID to each product line


# Variables
alt_dir = 'C:\\Users\\Kieran\\Python\\Work\\Test'

sf_username = ''
sf_password = ''
sf_key = ''
sf_opp = ''
sm_quote = ''
sm_spcr = ''
se_approve = ''
aip_ban = ''

gui.start_interface()
ad.gsm_dict()
