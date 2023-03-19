import pandas as pd
toclean = pd.read_csv('data.csv')
deduped = toclean.drop_duplicates('title')
deduped.to_csv('data_1.csv')