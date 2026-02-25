from fastapi import APIRouter
import json
from pathlib import Path

router_road_made = APIRouter()

JSON_FILE = Path(__file__).parent.parent / "src" / "roadmap_data.json"

@router_road_made.get('/TalentPilot/roadmap_made')
def get_all_roadmaps():
    
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return{
            'TalentPilot':'Already made roadmap......',
            'respone':data
        }