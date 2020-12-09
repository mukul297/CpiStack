
import pandas as pd
import numpy as np
import seaborn as sb

#reading raw data file 
RawFile = 'benchmark_rawdatafile.txt'

data_txt = pd.read_csv(RawFile, sep="\t")
cols = data_txt.columns

#pre processing the data 

final_cols = set()
time_data = {}
for index, row in data_txt.iterrows():
  
  if row[0].find('time') != -1:
    continue

  lst = []
  txt = ""

  for i in range(len(row[0])):
    if row[0][i] not in [' ', ',']:
      txt += row[0][i]
    if row[0][i] == ' ' and txt != "":
      lst.append(txt)
      txt = ""

  lst[2] = lst[2].split(':')[0]
  final_cols.add(lst[2])
  if not time_data.get(lst[0]):
    time_data[lst[0]] = []
  time_data[lst[0]].append([lst[2], lst[1]])

df = {}
df['time'] = []
for col in final_cols:
  df[col] = []

cpi_poss = 0
if "instructions" in final_cols and "cycles" in final_cols:
  df['cpi'] = []
  cpi_poss = 1
else:
  print("cpi does not exist")
  
token = {}
for col in final_cols:
  token[col] = 1
for key, val in time_data.items():
  for col in final_cols:
    token[col] = 1 
  df['time'].append(key)
  instr = 0
  cycle = 0
  for v in val:
    if v[0] == "instructions":
      instr = v[1]
    if v[0] == "cycles":
      cycle = v[1]

  if instr == 0:
    print(key, val)

  for v in val:
    if token[v[0]]:
      psh = float(v[1])/float(instr)
      df[v[0]].append(psh)
      
    token[v[0]] = 0

  if cpi_poss:
    cpi = float(cycle)/float(instr)
    df["cpi"].append(cpi)

df = pd.DataFrame.from_dict(df)

df.head()

#saving the data in .csv file

df.to_csv("Bench_data.csv")
