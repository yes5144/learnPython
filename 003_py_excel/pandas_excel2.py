import pandas as pd
import numpy as np

# numpy==1.19.2
# pandas==1.1.3
df = pd.read_excel("zzz_test_data/xxxx.xlsx", sheet_name=0,
                   header=2)  # sheet_name=0 指定第几个sheet
print(type(df), df)
print("---" * 30)
print(df[:1])
group_df = df.groupby(["区域"]).aggregate({
    "电脑价格": [sum],
    "姓名": [len, ",".join],
})
print(type(group_df), '\n', group_df)
## group_df write to excel
group_df.to_excel("res.xlsx")

# from sqlalchemy import create_engine

# conn = create_engine(
#     "mysql+pymysql://root:123qweQ@@192.168.5.49:3306/test2?charset=utf8")
# ## pd --> to_sql
# pd.io.sql.to_sql(df, "Sheet1", conn, schema="test2", if_exists="append")
