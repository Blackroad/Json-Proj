from appJar import gui
from app import json_builder

def press(button):
    if button == 'Cancel':
        app.stop()
    else:
        item =int(app.getEntry("Number of Items"))
        script =app.getEntry("Name of Script")
        des = app.getEntry("Description")
        json_builder(item,script,des)
        print("Number of Items:", item, "Name of Script:", script, "Description:", des)


def check(rb):
    if rb =='Auto':
        app.hideWidgetType('Entry','ReturnEventType')
    else:
        rb = 'Manual'





app = gui("Main Window", "400x200")
app.setBg(colour="yellow")
app.setFont(15)
app.addLabel("title", 'JSON creator')
app.setLabelBg("title","gray")
app.addLabelEntry('Number of Items')
app.addLabelEntry('Name of Script')
app.addLabelEntry('Description')
app.addLabelEntry('ReturnEventType')
app.addLabelEntry('Delay')
app.addLabelEntry('ResponseString')



app.addButtons(["Submit", "Cancel"], press)
app.addRadioButton('creator','Auto')
app.addRadioButton('creator','Manual')
app.setRadioButtonChangeFunction("creator", check)


app.go()







