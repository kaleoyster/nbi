"""
Description: Downloads zip file from FHWA and saves zipfiles in data
"""
import requests
from tqdm import tqdm
import zipfile

__author__ = "Akshay Kale"
__copyright__ = "GPL"
__email__ = "akale@unomaha.edu"

def download_zipfiles(url):
    """
    Downloads zip files
    args: url (string)
    returns: status
    """
    response = requests.get(url, stream=True)
    print("printing the response:", response)
    filename = '../../data/nbe/' + url[49:]
    with open(filename, 'wb') as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)
    return response

def main():
   years = [2015, 2016, 2017, 2018, 2019]
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
            status = download_zipfiles(url)

if __name__ == '__main__':
    main()
