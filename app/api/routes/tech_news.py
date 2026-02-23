from app.api.src.news_api import fetch_news
from fastapi import APIRouter,HTTPException,Query
import requests
from typing import Literal

tech_name=Literal[
    "Artificial Intelligence",
    "Machine Learning",
    "Blockchain",
    "Quantum Computing",
    "Edge Computing",
    "Metaverse",
    "5G Networks",
    "Cybersecurity",
    "Cloud Computing",
    "Robotic Process Automation"
]


news_router=APIRouter()
@news_router.get('/TalentPilot/tech_news')
def today_news_fetch(q:tech_name=Query(default='Machine Learning'),page_number:int=Query(default=1,ge=1)):
    try:
        result=fetch_news(q,page_number)
        return{
            'TalentPilot':f'Today News related to {q}',
            'response':result
        }
    except requests.exceptions.ConnectTimeout:
        raise HTTPException(
            status_code=504,
            detail="News API timeout"
        )

    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=503,
            detail="Cannot connect to News API"
        )

    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Request error: {str(e)}"
        )