import pandas as pd
import numpy as np

# numpy==1.19.2
# pandas==1.1.3
data = pd.read_excel("zzz_test_data/salary22.xlsx")
print(data)
print(data.groupby(["人事", "驻点"])["sum", "rmb", "rmb3", "rmb2"].sum())
print(data.groupby(["驻点", "人事"])["sum", "rmb", "rmb3", "rmb2"].sum())

print(
    data.groupby(["驻点", "人事"]).aggregate({
        "姓名": [len],
        "rmb": [sum],
        "rmb2": [sum],
        "rmb3": [sum],
        "sum": [sum],
    }))

# print(data.groupby("驻点")["sum"].agg({
#     "mean": np.mean,
# }))

# {'B': [np.mean, 'sum'], 'C': ['count', np.std]}
