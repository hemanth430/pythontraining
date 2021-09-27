# import json
# person = '{"name":"Hemanth","Languages":["English","Hindi"]}'

#
# import json
#
# person_dict = {'name': 'Bob','age': 12,'children': None}
#
# person_json = json.dumps(person_dict)
#
# print(type(person_json))
#

#writing json to a file

import json
person_dict = {'name':'Bob','Languages':['English','French'],'married':True,'age':32}

with open('person.txt','w') as json_file:
    json.dump(person_dict,json_file)

