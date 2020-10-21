import pandas as pd

mapDict = {True : "Heavy", False : "Light"}

d = {
    "name" : ["A", "B", "C"],
    "weight" : [3.14, 15, 1]
}

df = pd.DataFrame(d)
newCol = (df["weight"] > 3).map(mapDict)
df.insert(2, 'Impression', newCol)

print(df)