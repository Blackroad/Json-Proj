import json
import random
from data import HandleSlotEventList

def json_builder(items_num,jsonname,description):
    returnitems = []
    scriptname = jsonname + '.json'
    if input('Set all values randomly (Y/N) = ') == 'Y' or 'y':
        [returnitems.append(get_random_data()) for i in range(items_num)]
    else:
        [returnitems.append(get_input_data()) for i in range(items_num)]
    compose = {"Description":description, "ReturnItems":returnitems}
    with open(scriptname, "w") as f:
        f.write(json.dumps((compose),sort_keys=False, indent=2))


def get_input_data():
    eventType = input("ReturnEventType = ")
    delay = int(input("Delay = "))
    responseString = input("ResponseString = ")
    compose = {"ReturnEventType": eventType, "Delay": delay, "ResponseString": responseString}
    return compose

def get_random_data():
    eventType = random.choice(HandleSlotEventList())
    delay = random.randrange(1,100)
    responseString = "{chamber = 1, item =2}"
    print (eventType,delay, responseString + '\n')
    compose = {"ReturnEventType": eventType, "Delay": delay, "ResponseString": responseString}
    return compose





























