import pandas as p 
import plotly.express as px 
import csv 
import numpy as np 
def getdatasource(datapath):
    Rollno=[]
    Marks=[]
    with open(datapath) as f:
        df=csv.DictReader(f)
        for row in df:
            Rollno.append(float(row["Roll No"]))
            Marks.append(float(row["Marks"]))
    return{"x":Rollno,"y":Marks}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def main():
    datapath="attendance.csv"
    datasource=getdatasource(datapath)
    findcorrelation(datasource)
main()