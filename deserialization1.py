import json
file=open('json_ser1.json','r')
file=file.read()
data=json.loads(file)
print(data)
