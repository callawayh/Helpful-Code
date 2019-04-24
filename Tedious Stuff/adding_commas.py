
## Really helpful for adding commas to a lot of rows of data from an excel sheet to be able to use in SQL or something 
## Note: Will automatically copy results to your clipboard

import pandas as pd

df = pd.read_excel(excel_sheet) 
        
def commas(df):
    length = len(df)-1
    dat = []
    for index,x in enumerate(df): 
        if index < length:
            com = f"'{x}',"
            dat.append(com)
        else:
            nocom = f"'{x}'"
            dat.append(nocom)
    d = pd.DataFrame(dat)
    d.to_clipboard(excel = False, index = False,header = None)
    return d

commas(df.column)
