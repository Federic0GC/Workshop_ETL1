import pandas as pd

candidates = 'Data/candidates.csv' 
candidates_df = pd.read_csv(candidates, delimiter=';') 

print(candidates_df.head())
print(candidates_df.info())
