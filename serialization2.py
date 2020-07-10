data=[
    {'rno':101,'name':'prasanth','group':'computers','marks':[45,55,65,75,85,95],'status':True,'backlogs':None},
    {'rno':102,'name':'aswini','group':'computers','marks':[85,95,91,92,94,99],'status':True,'backlogs':None},
    {'rno':103,'name':'tulasi','group':'computers','marks':[45,55,65,75,85,95],'status':True,'backlogs':None},
    {'rno':104,'name':'gouri','group':'computers','marks':[45,55,65,75,85,95],'status':True,'backlogs':None},
    {'rno':105,'name':'lokesh','group':'computers','marks':[45,55,65,75,85,95],'status':True,'backlogs':None},
    {'rno':106,'name':'murali','group':'computers','marks':[45,55,65,75,85,95],'status':True,'backlogs':None}

]
import json
file=open('json_ser2.json','w')
json.dump(data,file)
#dump()--will use when data as an object
#dumps()--will use when data as a string
