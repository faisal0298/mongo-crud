import os

path = '/home/diycam/Downloads/'

with os.scandir(path) as it:
    for entry in it:
        if entry.name.endswith(".jpg") and entry.is_file():
            print(entry.name, entry.path)