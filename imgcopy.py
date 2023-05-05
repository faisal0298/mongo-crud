import os
import time
from datetime import datetime



origin = '/home/diycam/Desktop/img1/'
target = '/home/diycam/Desktop/img2/'

# while True:
#     def moveimg():
#         files = os.listdir(origin)

#         for file_name in files:
#             shutil.copy(origin+file_name, target+file_name)
#             os.remove(origin+file_name)
#             time.sleep(10)
#             print("Files are copied successfully")

#     moveimg()
# def moveimg():
        # file = [entry.name for entry in sorted(os.scandir(origin),
        # key=lambda x: time.time() - x.stat().st_mtime > 20, reverse=True)]
        # file = [entry.name for entry in sorted(os.scandir(origin),
        # key=lambda x: x.stat().st_mtime, reverse=True)]
        # print(((os.scandir(file)).stat()).st_mtime)
        # for filename in file:
        #     time.sleep(20)  
        #     shutil.copy(origin+filename, target+filename)          
        #     os.remove(origin+filename)
            
def moveimg():
    # file = [entry.name for entry in sorted(os.scandir(origin),
    #     key=lambda x: x.stat().st_mtime, reverse=True)]


    with os.scandir(origin) as it:
        for entry in it:
            current=datetime.utcnow()
            modified=datetime.utcfromtimestamp(os.path.getmtime(entry.path))
            diff = (current - modified).total_seconds()
            print(diff)
            if entry.name.endswith('.jpg') or entry.name.endswith(".jpeg") and entry.is_file():
                # print(entry.name, entry.path)
                if diff < 999999:
                    os.remove(origin+entry.name)
    time.sleep(10)
        

while True:
    moveimg()

