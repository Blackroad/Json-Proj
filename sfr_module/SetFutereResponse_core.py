import json
import random
from data import ForwardCalls, Responses, HandleSlotEventList

class SFR_Response:
    def __init__(self):
        pass

    def set_future_response_json_builder(self,jsonname):
        set:None
        scriptname = jsonname + '.json'
        inputtype = input('Set all values randomly (Y/N) = ')
        if inputtype == 'Y':
            set = self.get_random_data()
        elif inputtype == 'N':
            set = self.get_input_data()
        with open(scriptname, "w") as f:
            f.write(json.dumps(set, sort_keys=False, indent=2))
        print ("\n%s"%scriptname + ' file created' )


    def get_random_data(self):
        items = []
        forwardCall = random.choice(ForwardCalls())
        response = random.choice(Responses())
        responseItem = random.randrange(1,5)
        for i in range (responseItem):
            eventType = random.choice(HandleSlotEventList())
            delay = random.randrange(1,5)
            responseString = "{'test'}"
            items.append({"ReturnEventType": eventType, "Delay": delay, "ResponseString": responseString})
        compose = {'ForwardCall': forwardCall, 'Response': response, 'ReturnItems': items}
        return compose


    def get_input_data(self):
        items = []
        forwardCall = input("\nForwardCall = ")
        response = input("Response = ")
        responseItem = int(input("Number of Response Items = "))
        for i in range (responseItem):
            eventType = input("\nReturnEventType = ")
            delay = int(input("Delay = "))
            responseString = input("ResponseString = ")
            items.append({"ReturnEventType": eventType, "Delay": delay, "ResponseString": responseString})
        compose = {'ForwardCall':forwardCall,'Response':response,'ReturnItems':items}
        return compose

    def return_request_jsoncreator(self):
        jsonname = input('\nName for script = ')
        self.set_future_response_json_builder(jsonname)



