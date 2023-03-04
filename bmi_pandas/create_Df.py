import pandas as pd

column = ["Mariyah", "Batman", "Spongebob"]
titled_columns = {"name": column, "height": [1.67, 1.9, 0.25], "weight": [54, 100, 1]}

data = pd.DataFrame(titled_columns)

# select values from dataframe
select_column = data["weight"][1]
select_row = data.iloc[1]["weight"]

# manipulate dataframe values
bmi = []
# weight / (height**2)
for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

# insert manipulated data to a new dataframe column
data["bmi"] = bmi

# save dataframe to a file
data.to_csv("bmi.csv", index=False)
print(data)
