import json
import random
from data import HandleSlotEventList


class RR_request:
    def __init__(self):
        pass

    def return_request_json_builder(self,items_num, jsonname, description):
        returnitems = []
        scriptname = jsonname + '.json'
        inputtype = input('Set all values randomly (Y/N) = ')
        if inputtype == 'Y':
            [returnitems.append(self.get_random_data()) for i in range(items_num)]
        elif inputtype == 'N':
            [returnitems.append(self.get_input_data()) for i in range(items_num)]
        else:
            print ('input coorect unswer')
        compose = {"Description":description, "ReturnItems":returnitems}
        with open(scriptname, "w") as f:
            f.write(json.dumps((compose),sort_keys=False, indent=2))
        print("\n%s" % scriptname + ' file created')


    def get_input_data(self):
        eventType = input("\nReturnEventType = ")
        delay = int(input("Delay = "))
        responseString = input("ResponseString = ")
        compose = {"ReturnEventType": eventType, "Delay": delay, "ResponseString": responseString}
        return compose

    def get_random_data(self):
        eventType = random.choice(HandleSlotEventList())
        delay = random.randrange(1,100)
        responseString = "{chamber = 1, item =2}"
        print (eventType,delay, responseString + '\n')
        compose = {"ReturnEventType": eventType, "Delay": delay, "ResponseString": responseString}
        return compose

    def return_request_jsoncreator(self):
        items = int(input("\n" + 'Input number of Return Items for automation json file = '))
        jsonname = input('Name for script = ')
        description = input('Description of test script = ')
        self.return_request_json_builder(items, jsonname, description)































