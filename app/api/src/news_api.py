import requests 
from dotenv import load_dotenv
import os

RANGE=16
load_dotenv()
NEWS_API_KEY=os.getenv('news_api_key')
def fetch_news(q:str,page_number:int):
   
        if page_number<5 and page_number>0:
            data_store=[]
            
            url="https://newsapi.org/v2/everything"
            try:
                response=requests.get(url,
                                params={
                                    'q':q,
                                    'page':page_number,
                                   "sortBy": "publishedAt",
                                    'apiKey':NEWS_API_KEY
                                })
            
                if response.status_code==200:
                    data=response.json()
                    articles = data.get("articles", [])[:RANGE]
                    data_store=[
                        {
                            'Author':result.get('author','Unknown'),
                            'Title':result.get('title','Unknown'),
                            'Description':result.get('description','Unknown'),
                            'Resource_url':result.get('url','Unknown'),
                            'Image_url':result.get('urlToImage')
                        }
                    for result in articles]
                    return data_store
                else:
                    return 'API RESPONSE ERROR'
            except requests.exceptions.RequestException as e:
                 raise e
        else:
            return 'Page Number Should be less than 5(1-5)'
    

