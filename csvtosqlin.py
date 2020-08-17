import sqlite3
import pandas as pd
cnx = sqlite3.connect('combined.sqlite3')
df = pd.read_csv('/Users/evelynbaz/Documents/Projects/covid19/combined.csv')
df.to_sql('Combined', cnx)
