import pandas as pd
import urllib.request
from io import StringIO

url = "https://raw.githubusercontent.com/bluedack-space/OpenDataPublisherOnGithub/main/Prototyping/iris.csv"

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