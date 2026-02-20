from fastapi import APIRouter,HTTPException
from app.agents.roadmap import road_map
from groq import APIConnectionError,APIError,APITimeoutError,RateLimitError


road_map_router=APIRouter()
@road_map_router.get('/TalentPilot/roadmap')
def create_roadmap(tech_name:str):
    try:
        result=road_map(tech_name=tech_name)
        print(type(result))
        return{
            'TalentPilot':'Road Map Agent....',
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
