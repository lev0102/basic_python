#/print('hello world')

import string


x=6 # 變數宣告
print(type(x)) # 性質確認
num=6
string="hello"
list=[3,3,3,4]
tuple=(3,3,3,4)
dictionary=("name","lastname")

for n in list:
    print(n)#值

for i in range(len(list)):
    print (list[i])#幾個

for index, element in enumerate(list):
    print(index, element)#值加其順序(以上功能相加)

