import json
import random
from data import ForwardCalls, Responses, HandleSlotEventList



def set_future_response_json_builder(jsonname):
    set:None
    scriptname = jsonname + '.json'
    inputtype = input('Set all values randomly (Y/N) = ')
    if inputtype == 'Y':
        set = get_random_data()
    elif inputtype == 'N':
        set = get_input_data()
    with open(scriptname, "w") as f:
        f.write(json.dumps(set, sort_keys=False, indent=2))


def get_random_data():
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


def get_input_data():
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




