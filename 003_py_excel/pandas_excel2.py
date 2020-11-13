import pandas as pd
import numpy as np

# numpy==1.19.2
# pandas==1.1.3
df = pd.read_excel(
    "zzz_test_data/xxxx.xlsx", sheet_name=0, header=2
)  # sheet_name=0 指定第几个sheet；names=["","",""] 重命名字段名；index_col=0 第一列为索引；usecols=[0, 1, 2] 选取指定列

## row 行数
print(df.shape[0])
## colum 列数
print(df.shape[1])
## values
print(type(df), df)
print("---" * 30)
print(df[:1])
## group 分组
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
# pd.io.sql.to_sql(df.fillna("未知"), "Sheet1", conn, schema="test2", if_exists="append")

## Pandas删除，替换并提取其中的缺失值 https://blog.csdn.net/qq_18351157/article/details/104993254
## Pandas.read_excel()全参数详解 https://zhuanlan.zhihu.com/p/142972462

# dframe1["sku"] ="#" #添加一列数据，初始化为"#"