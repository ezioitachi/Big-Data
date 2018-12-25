for num in (1,2,3,4,5):
    print(num)
    if num==4:
        break
else:
    print("会执行吗")


students=[
    {"name": "小明"},
    {"name": "小刚"}
]

find_name="小刚"

for stu_name in students:
    print(stu_name)
    if stu_name["name"]==find_name:
        print("找到 %s" % find_name)
        break
else:
    print("没找到")