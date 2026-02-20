from app.api.src.news_api import fetch_news
from fastapi import APIRouter,HTTPException,Query
import requests




news_router=APIRouter()
@news_router.get('/TalentPilot/tech_news')
def today_news_fetch(q:str=Query(default='Technology'),page_number:int=Query(default=1)):
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