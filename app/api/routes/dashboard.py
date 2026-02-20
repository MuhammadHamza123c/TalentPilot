from fastapi import APIRouter,HTTPException
from app.agents.dashboard_skills import dash_board
from groq import APIConnectionError,APIError,APITimeoutError,RateLimitError


dashboard_router=APIRouter()
@dashboard_router.get('/TalentPilot/dashboard')
def today_dashboard():
    try:
        result=dash_board()
        
        return{
            'TalentPilot':'Dashboard of Skill....',
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
