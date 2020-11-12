f = open("zzz_test_data/test_excel.txt")
line_list = []
for line in f.readlines():
    line_list.append(line.split(','))
f.close()

print("list1: ", line_list)

line_list2 = []
with open("zzz_test_data/test_excel.txt") as f2:
    for i in f2.readlines():
        line_list2.append(i.split(','))

print("list2: ", line_list2)
