import PySimpleGUI as SG
import os

label = SG.Text("Type in a ToDo")
input_box = SG.InputText(tooltip="Enter ToDo", key="todo")
add_button = SG.Button("Add")
window = SG.Window("MyApp", layout=[[label], [input_box, add_button]], 
                   font=('Helvetica',10))

while True:
    events, values = window.read()
    print(events)
    print(values)
    match events:
        case "Add":
            todos = functions.get_todos()
            new_todos = values
            todos.append()

window.close()