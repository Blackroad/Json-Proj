import json
import random
from data import HandleSlotEventList

def json_builder(items_num,jsonname,description):
    returnitems = []
    scriptname = jsonname + '.json'
    inputtype = input('Set all values randomly (Y/N) = ')
    if inputtype == 'Y':
        [returnitems.append(get_random_data()) for i in range(items_num)]
    elif inputtype == 'N':
        [returnitems.append(get_input_data()) for i in range(items_num)]
    else:
        print ('input coorect unswer')
    compose = {"Description":description, "ReturnItems":returnitems}
    with open(scriptname, "w") as f:
        f.write(json.dumps((compose),sort_keys=False, indent=2))


def get_input_data():
    eventType = input("\nReturnEventType = ")
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































