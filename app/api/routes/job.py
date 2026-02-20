from fastapi import APIRouter,HTTPException
from app.agents.search_job import get_job
from groq import APIConnectionError,APIError,APITimeoutError,RateLimitError


job_router=APIRouter()
@job_router.get('/TalentPilot/job')
def job_finder(image_name:str):
    try:
        result=get_job(image_name=image_name)
        
        return{
            'TalentPilot':'Search Jobs......',
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
