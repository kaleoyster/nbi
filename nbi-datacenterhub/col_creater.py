import pandas as pd

df = pd.read_csv('Cases1992-2018.csv')
print(df)

base_headers = ['Case Id', 'Latitude', 'Longitude', 'Year Built', 'Material', 'Construction Type', 'ADT', 'ADTT', 'Deck', 'Superstructure', 'Substructure']

year = 2019
def create_colnames(year):
    repeat_headers = ['ADT', 'ADTT', 'Deck',
            'Superstructure', 'Substructure']
    
    headers = []
    for index, yr in enumerate(range(1992, year+1)):
        attr_cols = repeat_headers
        temp_cols = [attr + '.' + str(index+1) for attr in attr_cols]
        headers = headers + [str(yr)] + temp_cols

    return headers
print(create_colnames(year))
