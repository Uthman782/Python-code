import os
print(os.getcwd())
os.chdir("C://")
print(os.getcwd())

import json
dict1 = '{"var1": "ASAD","var2": "Usman","var3": "Haroon"}'
dict2 = {"var1": "ASAD", "var2": "Usman", "var3": "Haroon"}
data1 = json.loads(dict1)
print(dict2)
print(dict2['var1'])
print(data1)
# print(type(data1))
print(data1['var1'])

dict3 = {"var1": "ASAD",
         "var2": "Usman",
         "var3": "Haroon",
         'bool': False
         }
jscomp = json.dumps(dict3)
print(jscomp)
