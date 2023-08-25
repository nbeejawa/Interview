import PySimpleGUI as SG

label1 = SG.Text("Select Files to compress")
input_box1 = SG.InputText(tooltip="Select Files")
add_button1 = SG.FileBrowse("Choose")

label2 = SG.Text("Type in a ToDo")
input_box2 = SG.InputText(tooltip="Compress Loc")
add_button2 = SG.FolderBrowse("Choose")

compress_button = SG.Button("Compress")

window = SG.Window("MyApp", layout=[[label1, input_box1, add_button1],[label2, input_box2, add_button2],[compress_button]])
window.read()
window.close()