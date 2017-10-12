import pandas as pd
import json
from json import JSONEncoder
import jsonpickle


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class RootNode:
    name = ""
    children = list()

    def __init__(self, name, children):
        self.name = name
        self.children = children

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class LeafNode:
    name = ""
    size = ""

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


df = pd.read_csv("../data/ElectricityGeneration.total.csv")

total_children = list()
col = df.columns
year = 1
for i in range(1, len(col)):
    year_children = list()
    year_data = df[['country', col[i]]]
    for country, value in year_data.iterrows():
        leaf_node = LeafNode(value['country'], value[col[i]])
        year_children.append(leaf_node)
    year = RootNode(col[i], year_children)
    total_children.append(year)

total = RootNode("Electricity generation total (million kilowatt-hours)", total_children)
# json_string = json.dumps(year.__dict__)
# json_string =  MyEncoder().encode(total)
json_string = total.toJSON()
# json_string = jsonpickle.encode(total)

# ln = LeafNode("a", "b")
