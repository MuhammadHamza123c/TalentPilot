#(-------------------------LIBRARIES-----------------)

import os
from dotenv import load_dotenv
from supabase import create_client,StorageException,SupabaseException
#(----------------------LOAD SUPABASE API AND PROJECT URL_-------------)
load_dotenv()
project_url=os.getenv('SUPABASE_PROJECT_URL')
api_key=os.getenv('SUPABASE_API_KEY')
#(----------------------BUCKED NAME AND FOLDER WHERE IMAGES WILL UPLOAD---------)
BUCKET_NAME="files"
FOLDER_NAME="resume_analyze"
#(-------------------------CREATE SUPABASE CLIENT-----------------------)
supabase=create_client(project_url,api_key)
#(---------------------------FUNCTION TO UPLOAD IMAGES-------------------)
def upload_resume(image_name:str,image_content:bytes):
    try:
        file_path=f"{FOLDER_NAME}/{image_name}"
        supabase.storage.from_(BUCKET_NAME).upload(file_path, image_content)
        public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(file_path)
        return public_url
    except (StorageException,SupabaseException) as e:
        raise e
