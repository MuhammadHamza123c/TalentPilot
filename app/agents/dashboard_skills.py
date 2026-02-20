#(-----------------------------LIBRARIES--------------------)
import os
import json
from dotenv import load_dotenv
from .prompt import dashboard_prompt
from .model_detail import model_data
from ..schema.dashboard import TechJobsCountryDashboard
from groq import Groq,APIConnectionError,APIError,APITimeoutError,RateLimitError
#(-----------------------------LOAD ENV FILE-----------------)
load_dotenv()
groq_api_key=os.getenv('groq_api_key')
client=Groq(api_key=groq_api_key)
#(----------------------------FUNCTION TO CREATE A ROAD MAP---)
def dash_board():
    try:
        response = client.chat.completions.create(
        model=model_data[5]['DASHBOARD_MODEL'],
        messages=[
            {
                "role": "system",
                "content": dashboard_prompt},
            {"role": "user", "content": 'Make a Dashbaord according to current time'},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "Dashboard",
                "schema": TechJobsCountryDashboard.model_json_schema()
            }
        },
        temperature=model_data[5]['TEMPERATURE']
    )
        

        sql_query_generation = TechJobsCountryDashboard.model_validate(json.loads(response.choices[0].message.content))
        data_dict = sql_query_generation.model_dump()
        return data_dict
    except (APIConnectionError, APITimeoutError, RateLimitError, APIError) as e:
        raise e

