from appJar import gui
from app import json_builder, get_input_data



def press(button):
    if button == 'Exit':
        app.stop()
    if button == 'Submit':
        if app.getRadioButton('creator') == 'Auto':
            json_builder(int(app.getEntry('E1')), app.getEntry('E3'), app.getEntry('E2'))










app = gui("Main Window", "500x400")
app.setBg(colour="yellow")
app.setFont(15)
app.addLabel("title", 'JSON creator')
app.setLabelBg("title","gray")

app.addEntry('E1')
app.addEntry('E2')
app.addEntry('E3')
app.setEntryDefault('E1','Number Of Items')
app.setEntryDefault('E2','Description')
app.setEntryDefault('E3','Name of Script' )





app.addButtons(["Submit", "Exit"], press)
app.addRadioButton('creator','Auto')
app.addRadioButton('creator', 'Manual')

app.addEntry("l1")
app.addEntry("l2")
app.addEntry("l3")
app.setEntryDefault('l1','ReturnEventType')
app.setEntryDefault('l2','Delay')
app.setEntryDefault('l3','ResponseString')




app.go()







