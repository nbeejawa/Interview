import PySimpleGUI as SG
from zip_extractor import extract_archive


label1 = SG.Text("Select File to Extract")
input_box1 = SG.Input()     
add_button1 = SG.FileBrowse("Choose", key="archive")

label2 = SG.Text("Select Destination Folder")
input_box2 = SG.Input()
add_button2 = SG.FolderBrowse("Choose", key="folder")

extract_button = SG.Button("Extract")
output_label = SG.Text(key="output")

window = SG.Window("MyApp", layout=[[label1, input_box1, add_button1],
                                    [label2, input_box2, add_button2],
                                    [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(filepath, dest_dir)
    window["output"].update(value="Extraction Completed")


window.close()