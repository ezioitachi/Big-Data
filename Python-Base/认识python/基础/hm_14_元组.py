info_tuple=("zhangsan",18,1.75)

print(info_tuple[0])
print(info_tuple.index("zhangsan"))

print(info_tuple.count("zhangsan"))

print(len(info_tuple))

#遍历
for my_info in info_tuple:
    print(my_info)

print("%s 年龄是 %d 身高是%.2f" %info_tuple)  #格式化字符串就是元组


