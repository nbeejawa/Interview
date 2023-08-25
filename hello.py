import functions
import PySimpleGUI as SG
import os

label = SG.Text("Type in a ToDo")
input_box = SG.InputText(tooltip="Enter ToDo", key="todo")
add_button = SG.Button("Add")
list_box = SG.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
edit_button = SG.Button("Edit")


window = SG.Window("MyApp", layout=[[label], [input_box, add_button], 
                    [list_box, edit_button]], font=('Helvetica',10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    
    if event == "Add":
        todos = functions.get_todos()
        new_todos = values['todo'] + '\n'
        todos.append(new_todos)
        functions.write_todos(todos)

    elif event == "Edit":
        todo_to_edit = values['todos'][0]
        new_todo = values['todo']
        
        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        
    elif event =="todos":
        window['todo'].update(value=values['todos'][0])
        
    elif SG.WIN_CLOSED:
        break


window.close()
