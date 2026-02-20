#(-----------------------LIBRARIES--------------)
import os
from dotenv import load_dotenv
from .src.data_read import get_data
from .prompt import prompt_job_finder
from .model_detail import model_data
from groq import Groq,APIConnectionError,APIError,APITimeoutError,RateLimitError
#(-----------------------LOAD ENV FILE-----------)
load_dotenv()
groq_api_key=os.getenv('groq_api_key')
client = Groq(api_key=groq_api_key)

#(---------------------------RESUME SUMMARY-------)
def get_job_details(text_resume:str):
    try:
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """You are a helpful AI assistant. 

    Your task: 

    1. Receive a resume text as input. 
    2. Extract the candidate’s:
    - Key skills
    - Relevant work experience
    - Core expertise or domain (e.g., Machine Learning, Data Science, Backend)
    3. Compose a **concise, professional paragraph** summarizing the candidate’s profile for job matching. 
    - Include skills, years of experience, and domain.
    - Use clear language suitable for searching or filtering jobs online.
    4. Return **ONLY the paragraph**, with no lists, JSON, tables, or extra text.
    5. Do not include any explanations, instructions, or additional commentary."""
    },
        
            {
                "role": "user",
                "content":text_resume,
            }
        ],

        
        model=model_data[4]['JOB_MODEL'][0],
        temperature=model_data[4]['TEMPERATURE'][0]

    )

        return chat_completion.choices[0].message.content
    except (APIConnectionError, APITimeoutError, RateLimitError, APIError) as e:
        raise e


#(----------------------------SEARCH 10 JOB ONLINE------------)

def collect_jobs(text:str):
    try:
        response = client.chat.completions.create(
            model=model_data[4]['JOB_MODEL'][1],
            messages=[



                {
                                    "role":"system",
                                    "content":prompt_job_finder
                                },
                {
                    "role": "user",
                    "content": text}
                            
            ],
            temperature=model_data[4]['TEMPERATURE'][1]
        )
        
        return response.choices[0].message.content
    
    except (APIConnectionError, APITimeoutError, RateLimitError, APIError) as e:
        raise e
    



#(-------------------------MAIN FUNCTION TO GET JOB-----------)
def get_job(image_name:str):
    text_resume=get_data(image_name)
    job_dt=get_job_details(text_resume)
    result=collect_jobs(job_dt)
    return result

