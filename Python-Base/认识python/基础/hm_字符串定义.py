str1="hello python"
str2='我的外号是"大西瓜"'

print(str1,str2)

for c in str2:
    print(c)


space_str="   "
print(space_str.isspace())# 是否只包含空格

num_str="\u00b2"  #\u转义UNIcode
print(num_str)
print(num_str.isdigit()) #包含unicode
print(num_str.isdecimal()) #纯数字
print(num_str.isnumeric()) #包含汉字

hello_str="hello python"
print(hello_str.startswith("hello"))
print(hello_str.endswith("python"))
print(hello_str.find("abc")) #找不到报-1

print(hello_str.replace("python","world")) #替换后产生新的字符串
print(hello_str)