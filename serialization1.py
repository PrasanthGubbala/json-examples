import json
data={'rno':101,'name':'prasanth','marks':[45,55,65,75,85,95],'status':True}
file=open('json_ser1.json','w')
json.dump(data,file)