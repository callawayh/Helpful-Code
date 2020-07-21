## Code to help my girlfriend with mass - spec (chemistry) data

import pandas as pd
import numpy as np

# use glob https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/Sys.glob
list_of_paths = [path,path,path]


def read_special_data(path,number):
    data = pd.read_csv(path, 
                    header = None,
                    skiprows = 20,# might want to adjust
                    delimiter = " ", 
                    names = [f'MZ_{number}', f'Intensity_{number}', 'Marker','Num'])
    data['badrow'] = data[f"MZ_{number}"].str.slice(0,1) 
    dat = data[data.badrow.isin(['S','I'])==False] # grab rows where row badrow isnt s or i
    dat = dat.iloc[:, 0:2]
    agg = dat.groupby([f'MZ_{number}']).mean()
    return agg.reset_index()
   
#create blank dataframe/matrix
bigdata = pd.DataFrame()

for number,path in enumerate(list_of_paths):
    data = read_special_data(path,number)
    print(number)
    if number == 0:
        print('set',number)
        bigdata = data
    else:
        print('merged',number)
        bigdata = pd.merge(bigdata,
                           data, 
                           left_on = "MZ_0",
                           right_on = f"MZ_{number}", how = 'left')
        
        bigdata =  bigdata.drop(columns = [f"MZ_{number}"])



