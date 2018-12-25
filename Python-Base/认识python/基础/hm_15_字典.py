
#每个键值对各占一行,输出无序
xiaoming_dict={"name":"小明",
          "age":18,
          "height":1.75,
          "weight":75.5}

xiaoming_dict["color"]="白"
xiaoming_dict["name"]="大明"
xiaoming_dict.pop("weight")


temp_dict={"qq":"12345678",
           "phone": "10086"}
xiaoming_dict.update(temp_dict)

print(xiaoming_dict)

print(xiaoming_dict["name"])

#应用

card_list=[
    {"a":"a",
     "b":"b",
     "c":"c"},
    {"d":"d",
     "e":"e",
     "f":"f"}
]
for card_info in card_list:
    print(card_info)

