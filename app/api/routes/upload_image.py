from fastapi import (
    APIRouter,UploadFile,File,HTTPException
    )

from app.api.src.resume_upload import upload_resume
from app.agents.extract_text import get_text
from uuid import uuid4
from supabase import create_client,StorageException,SupabaseException
from groq import APIError,RateLimitError,APIConnectionError,APITimeoutError


upload_router=APIRouter()
@upload_router.post('/TalentPilot/resume_upload')
async def get_image(f1:UploadFile=File(...)):
    file_extension=f1.content_type.split('/')[-1]
    file_name=f'{uuid4()}.{file_extension}'
    try:
        content=await f1.read()
        image_url=upload_resume(image_name=file_name,image_content=content)
        image_text_read=get_text(image_name=file_name,image_url=image_url)
        if image_text_read:

            return{
            'TalentPilot':'Image has been Upload. Use Image_name for further process!',
            'Image_name':file_name
        }
        raise HTTPException(
            status_code=400,
            detail='Failed to Extract text from uploaded resume'
        )


    except SupabaseException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Supabase Error: {str(e)}"
        )
    except APIError as e:
        raise HTTPException(
            status_code=502,
            detail=f'Server API error: {str(e)}'

        )
    except RateLimitError as e:
        raise HTTPException(
            status_code=429,
            detail=f'Rate Limit Excede: {str(e)}'

        )
    except APIConnectionError as e:
        raise HTTPException(
            status_code=503,
            detail=f'Unable to connect to Internet: {str(e)}'
        )
    except APITimeoutError as e:
        raise HTTPException(
            status_code=504,
            detail=f'Request Time out excede: {str(e)}'
        )
    except StorageException as e:
        raise HTTPException(
            status_code=400,
            detail=f'Supabase Storage Problem: {str(e)}'
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected server error: {str(e)}")