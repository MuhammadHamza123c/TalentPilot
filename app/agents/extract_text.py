#(----------------------------LIBRARIES-------------------------------)

import os
import json
from dotenv import load_dotenv
from supabase import create_client
from .prompt import prompt_text_extract
from .model_detail import model_data
from groq import Groq,APIError,RateLimitError,APIConnectionError,APITimeoutError

#(------------------------------LOAD ENV KEYS--------------------------)
load_dotenv()
supabase_url=os.getenv('SUPABASE_PROJECT_URL')
supabase_api_key=os.getenv('SUPABASE_API_KEY')
groq_api_key=os.getenv("groq_api_key")
client = Groq(api_key=groq_api_key)
supabase=create_client(supabase_url,supabase_api_key)


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
        check_res=create_file(image_name=image_name,text=text)
        if check_res:
       
            return "Successfully, Image text extracted and store in data.json"
    except (APIConnectionError, APITimeoutError, RateLimitError, APIError) as e:
        raise e

#(----------------------------CREATE FILE FUNCTION USE TO MAKE DATA.JSON TO ADD RESUME TEXT-------)
def create_file(image_name: str, text: str):
    try:
        if image_name is not None and text is not None:
            resonse=supabase.table('resume_data').insert({
                'image_name':image_name,
                'image_describe':text
            }).execute()
            return resonse.data
    except Exception as e:
        return f'Error: {e}'

   
