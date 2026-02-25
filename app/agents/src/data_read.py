import json
import os
import re
from dotenv import load_dotenv
from supabase import create_client
load_dotenv()




load_dotenv()
supabase_url=os.getenv('SUPABASE_PROJECT_URL')
supabase_api_key=os.getenv('SUPABASE_API_KEY')
supabase=create_client(supabase_url,supabase_api_key)



#(---------------GET DATA FROM DATA.JSON File---------)
def get_data(image_name: str):
    try:
        response = supabase.table('resume_data') \
            .select('image_describe') \
            .eq('image_name', image_name) \
            .execute()

        data = response.data

        if not data:
            return "Image not found"

        return data[0]['image_describe']

    except Exception as e:
        return f"Error: {e}"

