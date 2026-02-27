from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4

from app.api.src.resume_upload import upload_resume
from app.agents.extract_text import get_text
from app.api.src.pdf_doc_text import extract_docx_from_url,extract_pdf_from_url
from app.agents.extract_text import create_file

from supabase import StorageException, SupabaseException
from groq import APIError, RateLimitError, APIConnectionError, APITimeoutError


upload_router = APIRouter()


@upload_router.post('/TalentPilot/resume_upload')
async def upload_resume_route(f1: UploadFile = File(...)):
    try:
   
        file_extension = f1.filename.split('.')[-1].lower()
        file_name = f"{uuid4()}.{file_extension}"
        print(file_name)

        content = await f1.read()

        file_url = upload_resume(image_name=file_name, image_content=content)
        
        print('File Upload hgae')

        if file_extension == 'pdf':
            text = extract_pdf_from_url(file_url)
            

        elif file_extension == 'docx':
            text = extract_docx_from_url(file_url)

        elif file_extension in ['png', 'jpg', 'jpeg']:
            text = get_text(image_name=file_name, image_url=file_url)
        


        else:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file format"
            )
        
        upload_text=create_file(image_name=file_name,text=text)
    
        if not text:
            raise HTTPException(
                status_code=400,
                detail="Failed to extract text from resume"
            )

       
        return {
            "message": "Resume uploaded & processed successfully",
            "Image_name": file_name
        }

  
    except SupabaseException as e:
        raise HTTPException(500, f"Supabase Error: {str(e)}")

    except StorageException as e:
        raise HTTPException(400, f"Supabase Storage Problem: {str(e)}")

    except APIError as e:
        raise HTTPException(502, f"Groq API error: {str(e)}")

    except RateLimitError as e:
        raise HTTPException(429, f"Rate limit exceeded: {str(e)}")

    except APIConnectionError as e:
        raise HTTPException(503, f"Connection error: {str(e)}")

    except APITimeoutError as e:
        raise HTTPException(504, f"Request timeout: {str(e)}")

    except Exception as e:
        raise HTTPException(500, f"Unexpected error: {str(e)}")
