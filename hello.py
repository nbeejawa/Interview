import functions
import PySimpleGUI as SG
import os

label = SG.Text("Type in a ToDo")
input_box = SG.InputText(tooltip="Enter ToDo", key="todo")
add_button = SG.Button("Add")
window = SG.Window("MyApp", layout=[[label], [input_box, add_button]], 
                   font=('Helvetica',10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    
    if event == "Add":
        todos = functions.get_todos()
        new_todos = values['todo'] + '\n'
        todos.append(new_todos)
        functions.write_todos(todos)
       
    elif SG.WIN_CLOSED:
        break


window.close()
