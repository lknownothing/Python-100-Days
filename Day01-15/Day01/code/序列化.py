# -*- coding:UTF-8 -*-
"""
+ dump 序列化到文件中
+ dumps 处理成字符串 dict -> list
+ load 文件中数据反序列化成对象
+ loads 字符串反序列化成对象 list -> dict
"""
import json
import os
print(os.getcwd())
my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
with open('.\\Day01-15\\Day01\\res\data.json', 'w',encoding="UTF-8") as file:
    json.dump(my_dict, file,ensure_ascii=False)
print('字典已经保存到res下的data.json文件中')

with open(".\\Day01-15\\Day01\\res\data.json","r",encoding="UTF-8") as f: 
    dict1=json.load(f)
    print(dict1)
