book = {}
book['tom']={'name':'tom','address':'22,ny,usa','phone':2345678}
book['ben']={'name':'ben','address':'22,dy nza','phone':1111111}
import json
s = json.dumps(book)
with open('c:\\pythontraining\\book.txt',"w") as f:
    f.write(s)
f=open("c:\\pythontraining\\book.txt",'r')
s = f.read()
import json
book = json.loads(s)
book['ben']

