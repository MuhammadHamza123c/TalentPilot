from pydantic import BaseModel
from typing import List, Optional

class TechnologyYearlyTrend(BaseModel):
    year: int
    job_count: int
    score: float
    avg_salary: Optional[float] = None

class CountryTechnologyMetrics(BaseModel):
    country_name: str
    job_count: int
    avg_salary: Optional[float] = None
    score: Optional[float] = None
    yearly_trends: Optional[List[TechnologyYearlyTrend]] = None

class TechnologyScore(BaseModel):
    technology_name: str
    overall_score: int
    job_count: Optional[int] = None
    avg_salary: Optional[int] = None
    top_companies: List[str]
    yearly_trends: Optional[List[TechnologyYearlyTrend]] = None
    countries: Optional[List[CountryTechnologyMetrics]] = None

class UpcomingTrends(BaseModel):
    skill_name: str
    year: str
    score: int

class SkillAreaScore(BaseModel):
    skill_area_name: str
    average_score: float
    job_count: Optional[int] = None
    avg_salary: Optional[int] = None
    top_technologies: Optional[List[TechnologyScore]] = None
    yearly_trends: Optional[List[TechnologyYearlyTrend]] = None
    countries: Optional[List[CountryTechnologyMetrics]] = None

class TechJobsCountryDashboard(BaseModel):
    top_technologies: List[TechnologyScore]
    skill_areas: List[SkillAreaScore]
    upcoming_trends: List[UpcomingTrends]
    chart_type: str = "bar"
