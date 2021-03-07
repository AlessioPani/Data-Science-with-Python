import pandas as pd

path_data = "dataset/imports-85.data"
path_header = "dataset/imports-85.names"

data = pd.read_csv(path_data, header=None)
# header = pd.read_csv(path_header)

data.head(5)
# data.tail(5)