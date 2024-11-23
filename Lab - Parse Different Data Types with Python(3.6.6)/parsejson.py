# Fill in this file with the code from parsing JSON exercise


### JSON parsing 
import json
import yaml

with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)

print(ourjson)

