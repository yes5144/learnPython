# https://www.cnblogs.com/melonjiang/p/6536876.html
from pymongo import MongoClient

conn = MongoClient('192.168.204.222', 27017)
db = conn.mydb  #连接mydb数据库，没有则自动创建
my_set = db.test_set  #使用test_set集合，没有则自动创建
# 插入数据（insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入）
my_set.insert({"name": "zhangsan", "age": 18})  #
# my_set.save({"name":"zhangsan","age":18})

#添加多条数据到集合中
users = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 20}]
my_set.insert(users)
#查询全部
for i in my_set.find():
    print(i)
#查询name=zhangsan的
for i in my_set.find({"name": "zhangsan"}):
    print(i)
## update
my_set.update({"name": "zhangsan"}, {'$set': {"age": 20}})

## remove
#删除name=lisi的全部记录
my_set.remove({'name': 'zhangsan'})

#删除name=lisi的某个id的记录
id = my_set.find_one({"name": "lisi"})["_id"]
my_set.remove(id)

#例：查询集合中age大于25的所有记录
#    (>)  大于 - $gt
#    (<)  小于 - $lt
#    (>=)  大于等于 - $gte
#    (<= )  小于等于 - $lte
for i in my_set.find({"age": {"$gt": 25}}):
    print(i)
## 在MongoDB中使用sort()方法对数据进行排序 1 为升序，-1为降序
for i in my_set.find().sort([("age", 1)]):
    print(i)

#limit()方法用来读取指定数量的数据
#skip()方法用来跳过指定数量的数据
#下面表示跳过两条数据后读取6条
for i in my_set.find().skip(2).limit(6):
    print(i)

#找出age是20、30、35的数据
for i in my_set.find({"age": {"$in": (20, 30, 35)}}):
    print(i)

#找出age是20或35的记录
for i in my_set.find({"$or": [{"age": 20}, {"age": 35}]}):
    print(i)

#删除集合里的所有记录
db.users.remove()