#(-----------------------------LIBRARIES--------------------)
import os
import json
from dotenv import load_dotenv
from .prompt import roadmap_prompt
from .model_detail import model_data
from ..schema.roadmap import RoadmapGraph
from groq import Groq,APIConnectionError,APIError,APITimeoutError,RateLimitError
#(-----------------------------LOAD ENV FILE-----------------)
load_dotenv()
groq_api_key=os.getenv('groq_api_key')
client=Groq(api_key=groq_api_key)
#(----------------------------FUNCTION TO CREATE A ROAD MAP---)
def road_map(tech_name:str):
    try:
        response = client.chat.completions.create(
        model=model_data[3]['ROAD_MAP_MODEL'],
        messages=[
            {
                "role": "system",
                "content": roadmap_prompt},
            {"role": "user", "content": tech_name},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "ROADMAPS",
                "schema": RoadmapGraph.model_json_schema()
            }
        },
        temperature=model_data[3]['TEMPERATURE']
    )
        

        sql_query_generation = RoadmapGraph.model_validate(json.loads(response.choices[0].message.content))
        data_dict = sql_query_generation.model_dump()
        return data_dict
    except (APIConnectionError, APITimeoutError, RateLimitError, APIError) as e:
        raise e



# print(type(road_map(tech_name='Machine Learning')))