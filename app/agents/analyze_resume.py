
#(------------------LIBRARIES----------------)


import os
import json
from dotenv import load_dotenv
from .src.data_read import get_data
from ..schema.analyze import main_model
from .prompt import prompt_resume_analyzer
from .model_detail import model_data
from groq import Groq,APIConnectionError,APIError,APITimeoutError,RateLimitError

#(----------------LOAD ENV FILE---------------)
load_dotenv()
groq_api_key=os.getenv('groq_api_key')



client=Groq(api_key=groq_api_key)



    
    

def analyze_text(text:str):
    try:
        response = client.chat.completions.create(
        model=model_data[0]['ANALYZE_RESUME_MODEL'],
        messages=[
            {
                "role": "system",
                "content": prompt_resume_analyzer        },
            {"role": "user", "content": text},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "analyze",
                "schema": main_model.model_json_schema()
            }
        },
        temperature=model_data[0]['TEMPERATURE']
    )

        query_generation = main_model.model_validate(json.loads(response.choices[0].message.content))
        data_dict = query_generation.model_dump()
        return data_dict
    
    except (APIConnectionError, APITimeoutError, RateLimitError, APIError) as e:
        raise e



#(-----------------MAIN METHOD TO CALL BOTH FUNCTIONS-------------------)
def analyze(image_name:str):
    text=get_data(image_name=image_name)
    result=analyze_text(text)
    return result

# print(analyze(image_name='123456'))



