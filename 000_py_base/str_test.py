# str = '\xbe\xdc\xbe\xf8\xb7\xc3\xce\xca\xa1\xa3'
# b = repr(str)
# print(unicode(eval(b), "gbk"))

input_name = "sz; drop databases demo"
params = [input_name]
print(params)

sql = 'select * from goods where name="%s"' % params
print(sql)