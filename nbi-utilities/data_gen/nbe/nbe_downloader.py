"""
Description:
    Downloads zip file from FHWA and saves zipfiles in data
"""
import os
import requests
from tqdm import tqdm
import zipfile

__author__ = "Akshay Kale"
__copyright__ = "GPL"
__email__ = "akale@unomaha.edu"

def download_zipfiles(directory, url):
    """
    Description:
        Downloads zip files
    Args:
        url (string)
    Returns:
        status
    """
    response = requests.get(url, stream=True)
    print("Response:", response)
    print('Downloading: ', url[49:])
    filename = directory + '/' + url[49:]
    with open(filename, 'wb') as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    return response

def main():
    """
    Driver function
    """
    directory_name = 'nbe-data'
    try:
        os.mkdir(directory_name)
    except:
        pass

    years = [2015,
             2016,
             2017,
             2018,
             2019,
             2020,
             2021
            ]

    state = ['AK',
             'AL',
             'AR',
             'CO',
             'DE',
             'DC',
             'HI',
             'ID',
             'KS',
             'KY',
             'LA',
             'MD',
             'MA',
             'MI',
             'MN',
             'MS',
             'MO',
             'MT',
             'NH',
             'NJ',
             'NM',
             'NY',
             'ND',
             'OK',
             'OR',
             'PR',
             'RI',
             'SD',
             'TN',
             'TX',
             'UT',
             'VT',
             'VA',
             'WV',
             'WY']
    for year in years:
         for statename in state:
             zipfilename = str(year)+statename+'_ElementData.zip'
             url = 'https://www.fhwa.dot.gov/bridge/nbi/element/'\
                 + str(year)\
                 + '/'\
                 + zipfilename
             status = download_zipfiles(directory_name, url)
if __name__ == '__main__':
    main()
