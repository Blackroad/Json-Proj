def HandleSlotEventList():
    list = ['HandleSystemEvent','HandleChamberEvent','HandleSocketEvent',
            'HandlePinEvent','HandleSystemFault','HandleChamberFault',
            'HandleSlotFault','HandleChamberSamples','HandleSlotPowerSamples',
            'HandleSlotPinSamples']
    return list

def ForwardCalls():
    list = ['StartService','StopService','LoadSlots',
            'StartSlots','StopSlots','ClearSlots','SetSocketInfo','GetSystemInfo']
    return list


def Responses():
    list = ['{"Status": "OK", "Reason": "Request processed successfully"}', '{"Status": "OK", "Reason": "Request is correct"}']
    return list