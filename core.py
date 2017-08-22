from app import json_builder


def jsoncreator():
    items = int(input('Input number of Return Items for automation json file = '))
    jsonname = input('Name for script = ')
    description = input('Description of test script = ')
    json_builder(items,jsonname,description)

jsoncreator()








