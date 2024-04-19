import pandas as pd 
tsv_file='imdb/name.basics.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('imdb/actors_imdb.csv',index=False)