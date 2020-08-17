import os
import glob
import pandas as pd
os.chdir("/Users/evelynbaz/Documents/GitHub/COVID-19clone/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports");
extension = 'csv'
all_filenames = [file for file in glob.glob('08*.csv')];
print(all_filenames);
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv.to_csv( "/Users/evelynbaz/Documents/Projects/covid19/combined.csv", index=False, encoding='utf-8-sig');
