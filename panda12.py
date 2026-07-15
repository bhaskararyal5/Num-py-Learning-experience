import pandas as pd

# data =[100,102,104,200,202]

# series = pd.Series(data,index=["a","b","c","d","e"])

# series.loc["c"]=300

# print(series.loc["a"])

# print(series[series>=200])

calories={
    "Day 1":1739,"Day 2":2100,"Day 3":1600
}
series =pd.Series(calories)
print(series)