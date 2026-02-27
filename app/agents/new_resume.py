#(-----------------------------------------------LIBRARIES-----------------------------------)
import os
import json
from dotenv import load_dotenv
from ..schema.resume import Resume
from .prompt import resume_create_prompt
from ..agents.extract_text import get_text
from .src.read_resume import resume_content
from ..agents.src.data_read import get_data
from ..agents.model_detail import model_data
from ..api.src.resume_upload import upload_resume
from groq import Groq,APIConnectionError,APIError,APITimeoutError,RateLimitError
from ..agents.src.resume_file import build_resume_png,build_resume_png_second,build_resume_png_third

#(------------------------------------LOAD ENV FILE---------------------------------------------)
load_dotenv()
groq_api_key=os.getenv('groq_api_key')
client=Groq(api_key=groq_api_key)

#(--------------------------------------USER MEMORY----------------------------------------------)
user=[]
agent_res=[]

#(----------------------------------------------------RESUME CREATE FUNCTION----------------------)
def create_new_resume(image_name:str=None,text:str=None):
    user_text=''
    if image_name is not None:
        user_text+=get_data(image_name=image_name)
    if text is not None:
         user_text+=text
    try:

        messages=[
                {
                    "role": "system",
                    "content": resume_create_prompt
                    }
            ]
        for u, a in zip(user, agent_res):
                messages.append({"role": "user", "content": u})
                messages.append({"role": "assistant", "content": a})

        messages.append({"role": "user", "content": user_text})

        response = client.chat.completions.create(
            messages=messages,
            model=model_data[7]['RESUME_CREATE_MODEL'],
            temperature=model_data[7]['TEMPERATURE'],

            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "resume_create",
                    "schema": Resume.model_json_schema()
                }
            }
        )
        user.append(user_text)
        

        sql_query_generation = Resume.model_validate(json.loads(response.choices[0].message.content))

    
        response=json.dumps(sql_query_generation.model_dump(), indent=2)
        agent_res.append(response)
        return sql_query_generation
    except (APIConnectionError, APITimeoutError, RateLimitError, APIError,json.JSONDecodeError,TypeError) as e:
        raise e



def main_resume(user_resume_choice:str,take_text:str=None,image_name:str=None):
    
     User_answer=create_new_resume(image_name=image_name,text=take_text)
     
     if User_answer.question is None:
            if user_resume_choice=='1':
                file_name=build_resume_png(User_answer)
            elif user_resume_choice=='2':
                file_name=build_resume_png_second(User_answer)
            elif user_resume_choice=='3':
                 file_name=build_resume_png_third(User_answer)
            content_store=resume_content(file_name=file_name)
            public_url=upload_resume(image_name=file_name,image_content=content_store)
            file_add=get_text(image_name=file_name,image_url=public_url)
            return{
                 'File_status':file_add,
                 'File_name':file_name,
                 'Public_url':public_url
            }
     else:
        return{
             'response':User_answer.question
        }
          
