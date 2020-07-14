import base64

text="英文：waht is the base64, How can you uset it"
x=base64.b64encode(text.encode("utf-8")) # 将text编码成byte
print(x)
print(type(base64.b64decode(x)))  # 解码出来时byte格式
print(base64.b64decode(x)) # 不解码直接输出的格式为byte
y=base64.b64decode(x).decode("utf-8") # 将byte
print(y)