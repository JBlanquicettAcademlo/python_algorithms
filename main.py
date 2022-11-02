import pyautogui
import os
from os import listdir


BASE_PATH = os.getenv('BASE_PATH')
print(BASE_PATH)
onlyfiles = [f for f in listdir(BASE_PATH) 
if os.path.isfile(os.path.join(BASE_PATH, f))]

print(onlyfiles)

for i in onlyfiles:
    print(i, os.path.getsize(BASE_PATH+'/'+i))