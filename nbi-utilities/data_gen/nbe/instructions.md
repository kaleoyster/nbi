<h1 align='center'>
NBE Data Acquistion Guide 🗺
</h1>

## 📂 NBE survey files
- The NBE downloader and process scripts are is located at [here](https://github.com/kaleoyster/nbi/tree/b5fb41950ee0a44c1d8967a1a672c0e3ea47b07f/nbi-utilities/data_gen/nbe).
- The raw data NBE is in XML format and it is located at the [FHWA website](https://www.fhwa.dot.gov/bridge/nbi/element.cfm).

## 👉 Steps

1. Clone/Download the nbi repository.

```zsh
git clone https://github.com/kaleoyster/nbi
```

2. Within it `nbi` repository the scripts are located in `nbe` folder.

```zsh
cd nbi/nbi-utilities/data_gen/nbe/
```

3. Select NBE file by states and years for download within `main` function of `nbe_downloader.py`.

```python

def main():
    """
    Driver function
    """
    directory_name = 'nbe-data'
    try:
        os.mkdir(directory_name)
    except:
        pass

    # Select years
    years = [2015,
             2016,
             2017,
             2018,
             2019,
             2020,
             2021
            ]

    # Select states
    state = ['AK',
             'AL',
             'AR',
             'CO',
             'DE',
             'DC',
             'HI',
             'ID']

```

4. Run NBE downloader to download ZIP files with in the `nbe-data` folder.

```zsh
python nbe_downloader.py
```

5. Run NBE process to extract zip files and transform XML to CSV file.

```zsh
python process_nbe.py
```
The processed nbe CSV file will saved in `nbe-data-processed` folder.
