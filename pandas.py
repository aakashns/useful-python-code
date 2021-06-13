
# How to load a URL using Pandas
import pandas as pd
url = 'https://example.com'
pd.read_csv(url)

# How to create a pivot table
import seaborn as sns
flights_raw_df = sns.load_dataset("flights")
# Decide the x axis, y axis and value
flights_df = flights_raw_df.pivot("year", "month", "passengers")


# 
