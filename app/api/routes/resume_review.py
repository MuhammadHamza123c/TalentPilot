from fastapi import APIRouter,HTTPException
from app.agents.improve_skills import reviewer
from groq import APIConnectionError,APIError,APITimeoutError,RateLimitError


review_router=APIRouter()
@review_router.get('/TalentPilot/review')
def resume_better(image_name:str,user_text:str):
    try:
        result=reviewer(image_name=image_name,user_text=user_text)
        return{
            'TalentPilot':'Resume Reviewer Agent....',
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
