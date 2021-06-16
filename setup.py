# Web Automation Drive Setup
# Updated 09/06/2021 by Kieran Lane

# Change Log (v1.0)
# 1.0   Initial script creation

# Usage 'import webauto as wa'
# Examples
#       alt_dir = 'DRIVE:\\Users\\USERNAME\\DIRECTORY'
#       wa.latest_download()
#       wa.latest_download(alt_dir)

# Mac Changes
# Replace https with http
# Change backslashes

# SCRIPT START
import os
import requests
import wget
from zipfile import ZipFile
from sys import platform
import shutil

# Web Driver URL/File Parts
url_release = 'LATEST_RELEASE'

if platform == 'darwin':
    url_base = 'http://chromedriver.storage.googleapis.com/'
    iam = 'darwin (Mac OS X)'
    file_name = 'chromedriver_mac64.zip'
    plain_name = 'chromedriver'
    divider = '/'
elif platform == 'win32':
    url_base = 'https://chromedriver.storage.googleapis.com/'
    iam = 'win32 (Windows)'
    file_name = 'chromedriver_win32.zip'
    plain_name = 'chromedriver.exe'
    divider = '\\'

file_dir = 'driver'
down_dir = 'download'


def latest_driver():
    # Fetches the latest version number for download URL construction
    url_latest = url_base + url_release
    return requests.get(url_latest).text


def driver_unzip(file, directory):
    # Unzips downloaded driver file to specified directory
    # Inherits default directory from latest_download()
    # Removes remaining *.zip file
    with ZipFile(file, 'r') as zipObj:
        zipObj.extractall(directory + divider + file_dir)
    os.remove(file)


def latest_download(directory=os.getcwd()):
    # Constructs download URL of latest web driver using latest_driver()
    # Confirms download directory exists and initiates download
    # Downloaded file unzipped using driver_unzip()
    url_download = url_base + latest_driver() + '/' + file_name

    # Check if supplied directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Check if /driver folder already exists, if so, delete it
    if os.path.exists(directory + divider + file_dir):
        shutil.rmtree(directory + divider + file_dir)

    wget.download(url_download, out=directory, bar=False)
    driver_unzip(directory + divider + file_name, directory)


def driver_setup(directory=os.getcwd(), mode=''):
    if mode == 'path':
        return directory + divider + file_dir + divider + plain_name
    if mode == 'root':
        root = directory + divider + down_dir
        if not os.path.exists(root):
            os.mkdir(root)
        return root

    if os.path.exists(directory + divider + file_dir):
        return True
    else:
        return False


def what_am_i(returntype='fullos'):
    if returntype == 'fullos':
        return iam
    if returntype == 'divider':
        return divider
