# National Bridge Inventory CSV to JSON Convertor

## About

National Bridge Inventory (NBI) represents bridge data submitted annually to FHWA by the States, Federal agencies, and Tribal governments.The data conforms to the [Recording and Coding Guide for the Structure Inventory and Appraisal of the Nations Bridges](https://www.fhwa.dot.gov/bridge/mtguide.pdf). Each data set is submitted in the spring, and may be corrected or updated throughout the year. The data is considered final and is published on this website at the end of each calendar year. [Source: [Federal Highway Administration](https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm)]

The Python script downloads CSV and zip file directly from the FHWA website. This features ensures that all transformations to the dataset are accounted for. 

## Addition information
This repository contains two versions of CSV to JSON convertor
1. `nbiCsvJsonConverter-1`
2. `nbiCsvJsonConverter-2`

The `nbiCsvJsonConverter-1` and `nbiCsvJsonConverter-2` will produce the same output, the only difference is the approach taken by each of these versions is different. The `nbiCsvJsonConverter-2` divides the task into two: Download and Conversion. Each of the subdivided tasks is run by separate scripts. The Conversion script also performs cross-check, item check, validations mentioned by [FHWA](https://www.fhwa.dot.gov/bridge/nbi/checks/), and populates JSON objects into MongoDB.

**Recommended version is `nbiCsvJsonConverter-2`**

## Prerequisites libraries used by the scripts
1. [io](https://docs.python.org/3.6/library/io.html)
2. [zipfile](https://docs.python.org/3.6/library/zipfile.html)
3. [csv](https://docs.python.org/3.6/library/csv.html)
4. [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
5. [requests](http://docs.python-requests.org/en/master/)
6. [json](https://docs.python.org/3.6/library/json.html)
7. [pymongo](https://api.mongodb.com/python/current/)
8. [ssl](https://docs.python.org/3.6/library/ssl.html)
9. [os](https://docs.python.org/3.6/library/os.html)

## Steps




###  `nbiCsvJsonConverter-1`
`nbiCsvJsonConverter-1` contains `NBIJsonFile` and `NBIMongo`.

```bash

python3 NbiCrawler.py

```
###  `nbiCsvJsonConverter-2`

This crawler creates a local copy of NBI files. This prevents uncessary requests to the server during the processing stage.
`
```bash

# Start NBI File Download for all years
python3 Downloadv1.py

# Decompress Zip files and convert CSV files to JSON
python3 ProcessMain.py

```
### Download Configuration

Downloadv1.py, contains two global lists to configure the states and years for which files are to downloaded. By default the  two lists includes all states and years.

```python
states = ['NE','AL','AK',...]
years = [1992,1993,1994,...]
```
Downloadv1.py output includes the following items:  
1. `NBIDATA` folder. This folder includes all bridge inspection files for all states and years in the configuration list. The files are renamed following this convention: `XXYYYY.txt`. `XX` representes the two digit state code and `YYYY` represents the year of reporting into NBI.


### Processing Configuration

ProcessMain.py, contains two global lists to configure the states and years for which files are to downloaded. To limit processing time, by default the states list only includes Nebraska ['NE']. The years list by default includes all years.

```python
states = ['NE']
years = [1992,1993,1994,...]
```
To connect to mongodb instance `dbConnect.txt` is required. you mayn create the file manually and add standard URI connection scheme given below:

```python
mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
```
To now know more about the schema, [Click Here](https://docs.mongodb.com/manual/reference/connection-string/)

ProcessMain.py output includes the following items:  
1. `missinggeo.txt` This text file will include all structure Number and year, where geo coordinates are invalid
2. `Summary.txt` This text file will include basic summary of this processing run
3. `mergedNBI.json` This text file includes JSON objects converted from csv rows
