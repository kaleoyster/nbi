import csv
import pandas as pd
import numpy as np
import requests
import io

# step 1
url = 'https://www.fhwa.dot.gov/bridge/nbi/2018/delimited/NE18.txt'
s = requests.get(url).content
c = pd.read_csv(io.StringIO(s.decode('utf-8')))
        

# step 2
c.columns()
