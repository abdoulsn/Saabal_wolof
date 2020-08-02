# read csv raccourci
from utils import *
def readcsv(path, sep):
    df = pd.read_csv(path, sep, encoding='iso-8859-1', index_col=0)
    print('Your data are ready in {}'.format(df))
    return df

# ecrire en scv rapide
def tocsv(df, path):
    df = pd.DataFrame(df)
    df.to_csv(path, sep=';', encoding='iso-8859-1', index=False)
    return 'csv file saved into {} '.format(path)
