import json
import os
import re
#(---------------GET DATA FROM DATA.JSON File---------)
def get_data(image_name:str):
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_name = os.path.join(PROJECT_ROOT, "data", "data.json")
    print(f'File Location of data stored: {file_name}')
    try:
            with open(file_name,'r',encoding='utf-8') as r:

                data=json.load(r)
                
            for item in data:
                if item.get('image_name') == image_name:
                    return re.sub(r'[^\w\s,.!?@#]','',item.get('image_describe', 'No description found'))
               
            return 'Image not Found'
    except FileNotFoundError:
         return 'File not found on Server'
    except PermissionError:
         return 'You dont have permission to read file'


