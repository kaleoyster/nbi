# National Bridge Inventory CSV to JSON Convertor

## About

National Bridge Inventory (NBI) represents bridge data submitted annually to FHWA by the States, Federal agencies, and Tribal governments.The data conforms to the [Recording and Coding Guide for the Structure Inventory and Appraisal of the Nations Bridges](https://www.fhwa.dot.gov/bridge/mtguide.pdf). Each data set is submitted in the spring, and may be corrected or updated throughout the year. The data is considered final and is published on this website at the end of each calendar year. [Source: [Federal Highway Administration](https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm)]

The Python script downloads CSV and zip file directly from the FHWA website. This features ensures that all transformations to the dataset are accounted for. 

## Usage

```bash

python3 NbiCrawler.py

```
## Update
The nbiSeparateFiles folder contains two separate files.

1. Downloadv1.py, to download csv files
2. ProcessMain.py to convert csv into JSON.


##Usage
Change directory to:
/ProjectNBI/nbiSeparateFiles

##Configuration
Change directory to:
/ProjectNBI/nbiSeparateFiles

1.Downloadv1.py, contains two global lists
eg:
states = ['NE','AL','AK',..]
by defaults includes all states

eg:
years = [1992,1993,1994..]
by default includes all years

2.ProcessMain.py ,contains two global lists
eg:
states = ['NE']
by defaults includes only 'NE'

eg:
years = [1992,1993,1994..]
by default includes all years

##Usage
Change directory to:
/ProjectNBI/nbiSeparateFiles

#STEPS
RUN 1.Downloadv1.py 
```bash

python3 Downloadv1.py

```

RUN 2.ProcessMain.py

OUTPUT: 1. missinggeo.txt (This text file will include all structure Number and year, where geo coordinates are invalid)
        2. Summary.txt (This text file will include basic summary)
        3. mergedNBI.json (JSON FILE converted from csv)
        
```bash

python3 ProcessMain.py

```
