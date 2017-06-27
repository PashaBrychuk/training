import json
pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)
print type(pythonDictionary)
print type(dictionaryToJson)