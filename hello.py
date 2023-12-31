import functions
import PySimpleGUI as SG
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

SG.theme("LightBlue6")

label = SG.Text("Type in a ToDo")

input_box = SG.InputText(tooltip="Enter ToDo", key="todo")

# add_button = SG.Button("Add", size=10)
add_button = SG.Button(size=2, image_source="add.png", 
                       mouseover_colors="Black", 
                       tooltip="Add todo", key="Add")

list_box = SG.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[45,10])

edit_button = SG.Button("Edit")

# complete_button = SG.Button("Complete")
complete_button = SG.Button(size=6, image_source="complete.png", 
                            mouseover_colors="Black", 
                            tooltip="Complete todo", key="Complete")

exit_button = SG.Button("Exit")

clock = SG.Text('', key='clock')


window = SG.Window("MyApp", layout=[[clock],[label], [input_box, add_button], 
                    [list_box, edit_button, complete_button], 
                    [exit_button]], font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d %y %H:%M:%S'))
    print(event)
    print(values)
    
    if event == "Add":
        todos = functions.get_todos()
        new_todos = values['todo'] + '\n'
        todos.append(new_todos)
        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        
        except IndexError:
            SG.popup("Select an item first", font=('Helvetica', 10))
            #print("Select an item first")
        
    elif event == "Complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete) 
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
            
        except IndexError:
            SG.popup("Select an item first", font=('Helvetica', 10))
            #print("Select an item first")
            
    elif event == "Exit":
        break
        
    elif event =="todos":
        window['todo'].update(value=values['todos'][0])
        
    elif SG.WIN_CLOSED:
        exit()
        #break


window.close()
