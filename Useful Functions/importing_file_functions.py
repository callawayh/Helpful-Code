def readcsv(file):
    df = pd.read_csv(file)
    df.columns = map(str.lower, df.columns)
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('/', '_')
    df.columns = df.columns.str.replace('-', '_')
    return df
    
# use when data is | delimiated coming right out of SQuireL
def ReadBarDelim(file):
    df = pd.read_csv(filename,delimiter='|')
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('/', '_')
    df.columns = df.columns.str.replace('-', '_')
    return df
