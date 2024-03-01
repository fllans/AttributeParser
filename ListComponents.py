import json

class Util:
    def __init__(self, key, location=None, command=None):
        self.key = key
        self.location = location
        self.command = command

# js = '{"components": {"name": "ScadaArchive", "location": "Scada.Archive//Scada.Archive.exe", "command": ".VersionInfo.ProductVersion"}}'

# js2 = open('test.json',)
# test = Component(**json.loads(js))

# print(js["components"])

workKey = "-main"


with open('D:\\Проекты\\AttributeParser\\Components.json') as jsonFile:
   jsonParse = json.load(jsonFile)
# print(type(jsonParse))
# print(jsonParse)
# print(jsonParse.keys())
# print(type(jsonParse.keys()))
# print(*jsonParse)

listUtils = [*jsonParse]

print(listUtils)
if jsonParse[listUtils[0]]["key"] == workKey:
    print(jsonParse[listUtils[0]]["location"])
# print(jsonParse[listComponents[0]][0]["ScadaArchive"]["command"])



# Comp = Util(**json.loads(jsonFile))
print(Comp.name)


import json
from types import SimpleNamespace

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# js3 = '{"ScadaArchive": {"location": "Scada.Archive//Scada.Archive.exe", "command": ".VersionInfo.ProductVersion"}}'

# smartphone_dict = json.loads(js2)

# print(smartphone_dict["ScadaArchive"]["location"])





# js = '{"name": "david", "age": 14, "gender": "male"}'
# person = Person(**json.loads(js))
# # print(person.name)
# js = '{"name": "david", "age": 14, "gender": "male", "language": "English"}'
# person = Person(**json.loads(js))
# # print(person.language)



class components:
     def __init__(self, name=None, location=None, command=None):
         self.name = name
         self.location = location
         self.command = command


js = '{"name": "ScadaArchive", "location": "Scada.Archive//Scada.Archive.exe", "command": ".VersionInfo.ProductVersion"}'
Comp = components(**json.loads(js))
print(Comp.name)
# js = '{"name": "david", "age": 14, "gender": "male", "language": "English"}'
# Comp = components(**json.loads(js))
# print(Comp.location)
# print(Comp.command)
# # {       "name": "ScadaArchive",
# #             "location": "Scada.Archive//Scada.Archive.exe",
# #             "command": ".VersionInfo.ProductVersion"
# #           }
# js4 = open("E:\\Projects\\TA\\Utils\AttributeParser\\test.json")
# js3 = '{"components": {"name": "ScadaArchive", "location": "Scada.Archive//Scada.Archive.exe", "command": ".VersionInfo.ProductVersion"}}'

# # smartphone_dict = json.loads(js4)

# # print(smartphone_dict["components"]["name"])


 
# # Import JSON module
# import json
 
# # Define JSON string
# jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
 
# # Convert JSON String to Python
# student_details = json.loads(js4)
 
# # Print Dictionary
# # print(student_details)
 
# # Print values using keys
# # print(student_details["components"]["ScadaArchive"])
# # print(student_details['course'])