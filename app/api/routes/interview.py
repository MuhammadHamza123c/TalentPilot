from fastapi import APIRouter,HTTPException
from app.agents.interviewer import ask_questions
from groq import APIConnectionError,APIError,APITimeoutError,RateLimitError


interview_router=APIRouter()
@interview_router.get('/TalentPilot/interview')
def create_roadmap(image_name:str,text:str):
    try:
        result=ask_questions(image_name=image_name,user_text=text)
        return{
            'TalentPilot':'Interview Agent....',
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
