import PySimpleGUI as SG
import os

label = SG.Text("Type in a ToDo")
input_box = SG.InputText(tooltip="Enter ToDo")
add_button = SG.Button("Add")
window = SG.Window("MyApp", layout=[[label, input_box, add_button]])
window.read()
window.close()