from fastapi import APIRouter,HTTPException,Query,Body,Form
from app.agents.new_resume import main_resume
from groq import APIConnectionError,APIError,APITimeoutError,RateLimitError
from typing import Optional,Literal


new_resume_router=APIRouter()
@new_resume_router.post('/TalentPilot/new_resume')
def create_it(user_choice:Literal['1','2','3'],image_name:str=Query(None),text:str=Form(None)):
    try:
        result=main_resume(user_resume_choice=user_choice,take_text=text,image_name=image_name)
        return{
            'TalentPilot':'New Resume....',
            'respone':result
        }
    except APIConnectionError as e:
        raise HTTPException(
            status_code=503,
            detail='API unable to connect'
        )
    except APITimeoutError as e:
        raise HTTPException(
            status_code=504,
            detail='External Servr Timeout Error'
        )
    
    except RateLimitError as e:
        raise HTTPException(
            status_code=429,
            detail='Too many requests in one minute'
        )
    except APIError as e:
        raise HTTPException(
            status_code=502,
            detail='External Server Error'
        )


    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f'Unexpected Server Error: {str(e)}'
        )
