from ReturnRequest.ReturnRequest_core import return_request_json_builder


def return_request_jsoncreator():
    items = int(input('Input number of Return Items for automation json file = '))
    jsonname = input('Name for script = ')
    description = input('Description of test script = ')
    return_request_json_builder(items, jsonname, description)

return_request_jsoncreator()








