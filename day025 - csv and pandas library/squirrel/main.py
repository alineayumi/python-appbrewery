import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

counts = data["Primary Fur Color"].value_counts()
color_dict = {
    "Fur Colors": counts.keys(),
    "Count": counts.values,
}
df = pandas.DataFrame(color_dict)
df.to_csv("fur_color_count.csv")
