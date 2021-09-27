# import json
#
# #Some Json
# x = {'name':'John','age':30,'City':"New York"}
# s = json.dumps(x)
# y = json.loads(s)
# print(type(y))
#

#Convert python to json
# import json
# x = {'name':'john','age':30,'city':'newyork'}
# y = json.dumps(x)
# print(y)
# print(type(y))
#
# import json
# s = json.dumps(['apple','banana'])
# with open("c:\\pythontraining\\book1.txt",'w') as f:
#     f.write(s)
#

import json
x = {'name':'Hemanth','age':33,'Married':True,'Divorsed':False,"Children":('Ann','Billy'),"Pets":None,"Cars":[{
    'Model':'BMW 230','MPG':27.5},{"Model":"Ford Edge","MPG":24.1}]}

# s = json.dumps(x)
# with open("c:\\pythontraining\\book3.txt",'w') as f:
#     f.write(s)

l = json.dumps(x, indent=4, sort_keys=False)
with open("c:\\pythontraining\\book5.txt",'w') as f:
    f.write(l)
print(type(l))








