# -*- coding: UTF-8 -*-
"""
字典的构造方法
"""
import pandas as pd
import numpy as np

person=dict(name="陈",age=23,height=170)

item1=zip("ABCDE","12345")
item2=dict(zip("ABCDE","12345"))
print(person,"\n",item1,"\n",item2)

# a=[1,2,3]
# b=[4,5,6]
# c=[7,8,9]
# zz=zip(a,b,c)
# print(zz)
for key in item2:
    print(key)

for key in person:
    print(f"{key} {person[key]}")

# 获取字典中的所有键.keys() .values() .items()

for key,value in person.items():
    print(key,"-->",value)

# 使用popitem方法删除字典中最后一组键值对

key,value=person.popitem()
print(key,value)

# 通过dict.update(dict1) 把两个字典合并
item2.update(person)
print(item2)