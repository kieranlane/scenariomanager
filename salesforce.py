from simple_salesforce import Salesforce
import requests
import pandas as pd
import csv
from io import StringIO

# Sign into Salesforce
sf = Salesforce(username='kieran.lane@centurylink.com',
password='!PNSpEjKRDaWfoiD5@uZ4E^#',
security_token='otjrW8rJv6I9z4I92bD6Dpf5G')
# Set report details
sf_org = 'https://lumn.lightning.force.com/'
report_id = '00O5d000007fwPCEAY'
export_params = '?isdtp=p1&export=1&enc=UTF-8&xf=csv'
expor_paramas2 = '?csv=1&exp=1&enc=UTF-8&isdtp=p1'
# Download report
# sf_report_url = sf_org + report_id + export_params
# response = requests.get(sf_report_url, headers=sf.headers, cookies={'sid': sf.session_id})
# new_report = response.content.decode('utf-8')
# report_df = pd.read_csv(StringIO(new_report))

response = requests.get(sf_org + report_id + expor_paramas2, headers=sf.headers, cookies={'sid': sf.session_id})

response.contents