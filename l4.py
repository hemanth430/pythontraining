import json
with open("c:\\pythontraining\\test1.json") as f:
    data = json.load(f)
print(data)
print(type(data))