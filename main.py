from fastapi import FastAPI
from app.api.routes.upload_image import upload_router
from app.api.routes.tech_news import news_router
from app.api.routes.analyze import analyze_router
from app.api.routes.dashboard import dashboard_router
from app.api.routes.roadmap import road_map_router
from app.api.routes.interview import interview_router
from app.api.routes.job import job_router
from app.api.routes.create_resume import new_resume_router
from app.api.routes.resume_review import review_router
app=FastAPI()
@app.get('/')
def home():
    return{
        'TalentPilot':'Welcome to TalentPilot!'
    }

app.include_router(upload_router)
app.include_router(news_router)
app.include_router(analyze_router)
app.include_router(dashboard_router)
app.include_router(road_map_router)
app.include_router(interview_router)
app.include_router(job_router)
app.include_router(new_resume_router)
app.include_router(review_router)