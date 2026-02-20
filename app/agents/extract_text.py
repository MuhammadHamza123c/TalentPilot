#(----------------------------LIBRARIES-------------------------------)

import os
import json
from dotenv import load_dotenv
from .prompt import prompt_text_extract
from .model_detail import model_data
from groq import Groq,APIError,RateLimitError,APIConnectionError,APITimeoutError
#(------------------------------LOAD ENV KEYS--------------------------)
load_dotenv()
groq_api_key=os.getenv("groq_api_key")
client = Groq(api_key=groq_api_key)


#(-------------------------------GET TEXT FROM UPLOAD RESUME IMAGE-------)
def get_text(image_name:str,image_url:str):
    
    try:
        completion = client.chat.completions.create(
        model=model_data[1]['EXTRACT_TEXT_MODEL'],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt_text_extract
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url
                        }
                    }
                ]
            }
        ],
        temperature=model_data[1]['TEMPERATURE'],
        max_completion_tokens=1024,
        top_p=1,
    )
        text=completion.choices[0].message.content
#(---------------------CALLING CREATE FILE TO MAKE DATA.JSON and ADDD TEXT---------)
        create_file(image_name=image_name,text=text)
       
        return "Successfully, Image text extracted and store in data.json"
    except (APIConnectionError, APITimeoutError, RateLimitError, APIError) as e:
        raise e

#(----------------------------CREATE FILE FUNCTION USE TO MAKE DATA.JSON TO ADD RESUME TEXT-------)
def create_file(image_name: str, text: str):
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_folder = os.path.join(PROJECT_ROOT, "agents", "data")
    file_name = os.path.join(data_folder, "data.json")
    print(f'File Created and data Stored at: {file_name}')
    

    os.makedirs(data_folder, exist_ok=True)
    
    entry = {"image_name": image_name, "image_describe": text}
    
    data_list = []

    
    if os.path.exists(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f_r:
                data_list = json.load(f_r)
                if not isinstance(data_list, list):
                    data_list = [data_list]
        except (json.JSONDecodeError, FileNotFoundError):
            data_list = []

    data_list.append(entry)

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)



