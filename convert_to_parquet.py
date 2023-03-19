import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd


df = pd.read_csv("dataset/final_data.csv")
table = pa.Table.from_pandas(df)
pq.write_table(table, 'final_data.parquet')

# df1 = pd.read_csv("reviews_2.csv")
# table = pa.Table.from_pandas(df1)
# pq.write_table(table, 'review_2.parquet')

# print(pd.read_parquet('data.parquet'))
# print(pd.read_parquet('review.parquet'))
