import pandas as pd
SAVE_AT = "/Users/AkshayKale/Google Drive/Data/sample/"

def sampler(df, name, sample=5, save_at=SAVE_AT):
    save_at = save_at + name
    return df.head(sample).to_csv(save_at)


def main():
    sample_df = pd.DataFrame({'Fruits':['Apple', 'Banana', 'Chiku', 'Orange', 'Peru'], 
                             'Price': [2, 1, 1.5, 2.1, 3]})
    sampler(sample_df, 'sample1.csv')

main()
