from pydantic import BaseModel
from typing import Optional



class skill_year(BaseModel):
    name: Optional[str]=None
    year: Optional[list[str]]=None             
    skill_value_overyear: Optional[list[int]]=None  

class experience(BaseModel):
    company: Optional[str]=None
    start_year: Optional[int]=None
    end_year: Optional[int]=None
    role: Optional[str]=None
    

class project(BaseModel):
    name: Optional[str]=None
    skill_name:Optional[list[str]]=None              
    each_skill_score:Optional[list[int]]=None    

class message(BaseModel):
    resume_thought:str

class main_model(BaseModel):
    skills: list[skill_year]
    ATS: Optional[int]=None
    experience: list[experience]
    project: list[project]
    message:message

