import pandas as pd

# data =[100,102,104,200,202]

# series = pd.Series(data,index=["a","b","c","d","e"])

# series.loc["c"]=300

# print(series.loc["a"])

# print(series[series>=200])

# calories={
#     "Day 1":1739,"Day 2":2100,"Day 3":1600
# }
# series =pd.Series(calories)
# print(series)

# data={"Name":["spongebob","patrik","squidward"],
#     "Age":[30,35,50]}

# df=pd.DataFrame(data)
# print(df)

# df["Job"]=["Cook","N/A","Cashier"]

# new_row=pd.DataFrame([{"Name":"Sandy","Age":28,"Job": "engineer"}],index=[3])
# df=pd.concat([df,new_row])
# print(df)

hello=pd.read_csv("pokemon1st.csv",index_col="Name")

#selcetion by column
# print(hello[["Name","Height","Weight"]].to_string())

# #selection by rows
# print(hello.loc["Charizard":"Blastoise",["Height","Weight"]])
# print(hello.iloc[0:10])

# pokemon=input("enter a pokemon name:")

# try:
#     print(hello.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} doesnt exist")

# #filtering
# tall_pokemon=hello[hello["Height"]>=2]
# print(tall_pokemon)

# heavy_pokemon=hello[hello["Weight"]>=100]
# print(heavy_pokemon)

# legendaray_pokemon=hello[hello["Legendary"]==1]
# print(legendaray_pokemon)

#aggregate functions
# print(hello.mean(numeric_only=True))
# print(hello.sum(numeric_only=True))
# print(hello.min(numeric_only=True))
# print(hello.max(numeric_only=True))
# print(hello.count())

#single column
# print(hello["Height"].mean())

# group=hello.groupby("Type1")
# print(group["Height"].mean())

#how to drop columns
# hello=hello.drop(columns=["Legendary"])

#Handle Missing data
# hello=hello.dropna(subset=["Type2"])
# hello=hello.fillna({"Type2":"None"})

#fix inconsistent values
# hello["Type1"]=hello["Type1"].replace({"Grass":"GRASS"})

#Standardize text
# hello["Type1"] = hello["Type1"].str.lower()

#fix data types
# hello["Legendary"]=hello["Legendary"].astype(bool)
# print(hello)

#remove duplicate data
hello=hello.drop_duplicates()
