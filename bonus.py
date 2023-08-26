import PySimpleGUI as SG
from zip_creator import make_archive

label1 = SG.Text("Select Files to compress")
input_box1 = SG.Input()     
add_button1 = SG.FileBrowse("Choose", key="files")

label2 = SG.Text("Select Destination Folder")
input_box2 = SG.Input()
add_button2 = SG.FolderBrowse("Choose", key="folder")

compress_button = SG.Button("Compress")
output_label = SG.Text(key="output")

window = SG.Window("MyApp", layout=[[label1, input_box1, add_button1],
                                    [label2, input_box2, add_button2],
                                    [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed")
        

window.close()
