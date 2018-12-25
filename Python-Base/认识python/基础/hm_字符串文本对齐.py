poem=["\t\nabc",
      "abcdefg",
      "abcdefghjklmn\t\n",
      "kijhgf",
      "huebf"]

for poem_str in poem:
    print("|%s|" %poem_str.center(20," "))
for poem_str in poem:
    print("|%s|" %poem_str.ljust(20," "))

for poem_str in poem:
    print("|%s|" %poem_str.strip().center(20," ")) #strip去掉\t\n\r和空格


poem_str.split() #拆分大字符串为小字符串，结果是list
poem_str.join() #合并小字符串