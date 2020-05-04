import pandas as pd


d = {
    "Name" : ["Juhn", "Cat" , "Billy", "Zoe", "Jack"],
    "Cash" : [59, 2, 3, 4 ,18]
}

df = pd.DataFrame(d)

df2 = df[df["Cash"] > 3]

print(list(df2.index))
