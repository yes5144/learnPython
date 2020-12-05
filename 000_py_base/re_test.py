import re
b = "<<p>我是测试文本<br/></p><p>我是测试文本\n  \n<br/></p>"
## 替换str内的html标签
c = re.sub('<[^<]+?>', '', b).replace('\n', '').strip()
print(c)

## 只匹配想要的内容
d = re.findall(r'p>(.*?)</p', b, re.S)
print(d)