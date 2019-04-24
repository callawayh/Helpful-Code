## a general way to stack files together that have the same columns which is easier than doing it in excel

import pandas as pd 

# load data 
df = pd.read_csv(r"filepath1")
df2 = pd.read_csv(r"filepath2")
df3 = pd.read_csv(r"filepath3")

# make a list of dfs 
frames = [df,df2,df3]

# stack 
df_final = pd.concat(frames, ignore_index = True)

# add schema if single client, if many clients with schema then ignore. if no schema, add one during import
idx = 0
new_col = 'client_schema'  # the client schema
df_final.insert(loc=idx, column='schema', value=new_col)

# check len of frames
for x in frames:
    print(len(x))
    print()
    
# check len of output   
print(len(df_final))

# write file
df_final.to_csv('file.csv', index = False)
