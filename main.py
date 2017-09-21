from rr_module.ReturnRequest_core import RR_request
from sfr_module.SetFutereResponse_core import SFR_Response

s,r = SFR_Response(),RR_request()
print("1. SetFutureResponse Json", "\n2. Return Request json", "\n3. EXIT")
while True:
    js = input("\n" + 'Select option = ')
    if js == '1':
        s.return_request_jsoncreator()
    elif js == '2':
        r.return_request_jsoncreator()
    elif js == '3':
        break
    else:
        print('select 1 or 2')






