import pandas as pd
import urllib.request
from io import StringIO

url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

#Routine for reading the csv file on the Web
def read_csv(url):
    print(url)
    res = urllib.request.urlopen(url)
    res = res.read().decode("utf-8")
    df = pd.read_csv(StringIO(res) )
    print(df)
    return df

#Execute 
read_csv(url)