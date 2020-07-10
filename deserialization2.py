import json
file=open('json_ser2.json','r')
file=file.read()
data=json.loads(file)
for x in data:
    print(x)