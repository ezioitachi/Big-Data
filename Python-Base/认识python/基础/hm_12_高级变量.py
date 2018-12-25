#列表


name_list=["zhangsan","lisi","wangwu"]

print(name_list)
#append
name_list.append("王小二")
#insert
name_list.insert(1,"meimei")

temp_list=["sunwukong","zhubajie","shashidi"]
#extend
name_list.extend(temp_list)
print(name_list)
#remove
name_list.remove("wangwu")
#pop
name_list.pop(3)
#clear
name_list.clear
print(name_list)

#del 从内存中删除变量

#.sort 列表升序
#.sort(reverse=True) 降序
#.reverse 逆序