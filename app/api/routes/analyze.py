from fastapi import APIRouter,HTTPException
from app.agents.analyze_resume import analyze
from groq import APIConnectionError,APIError,APITimeoutError,RateLimitError


analyze_router=APIRouter()
@analyze_router.get('/TalentPilot/analyz_resume')

def resume_analyze_(image_name:str):
    try:
        result=analyze(image_name=image_name)
        return{
            'TalentPilot':'Analyze Resume Agent working...',
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
