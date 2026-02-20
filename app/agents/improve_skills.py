#('-----------------------LIBRARIES----------------)
import os
from dotenv import load_dotenv
from .src.data_read import get_data
from .prompt import prompt_resume_reviewer
from .model_detail import model_data
from groq import Groq,APIConnectionError,APIError,APITimeoutError,RateLimitError

#(--------------------------LOAD ENV FILE------------)
load_dotenv()
groq_api_key=os.getenv('groq_api_key')
client = Groq(api_key=groq_api_key)

#(-----------------------------USER HISTORY-----------)
user=[]
agent_res=[]

#(-----------------------------------RESUME REVIEWER AGENT-------------)
def reviewer(image_name:str,user_text:str):
    try:
        res_text=get_data(image_name=image_name)
        messages = [
            {
                "role": "system",
                "content": prompt_resume_reviewer + f"\n\nHere is the candidate resume:\n{res_text}"
            }
        ]

        for u, a in zip(user, agent_res):
            messages.append({"role": "user", "content": u})
            messages.append({"role": "assistant", "content": a})

        messages.append({"role": "user", "content": user_text})
        


        chat_completion = client.chat.completions.create(
        messages=messages,

        
        model=model_data[6]['SKILLS_IMPROVE_MODEL'],
        temperature=model_data[6]['TEMPERATURE']
    )
        reply=chat_completion.choices[0].message.content
        user.append(user_text)
        agent_res.append(reply)
        


        return chat_completion.choices[0].message.content
    except (APIConnectionError, APITimeoutError, RateLimitError, APIError) as e:
        raise e

