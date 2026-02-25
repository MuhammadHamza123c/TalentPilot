from pydantic import BaseModel, Field
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
    yearly_trends: List[TechnologyYearlyTrend] = Field(default_factory=list)


class TechnologyScore(BaseModel):
    technology_name: str
    overall_score: int
    job_count: Optional[int] = None
    avg_salary: Optional[int] = None

    # ✅ FIXED: no more crashes
    top_companies: List[str] = Field(default_factory=list)

    yearly_trends: List[TechnologyYearlyTrend] = Field(default_factory=list)
    countries: List[CountryTechnologyMetrics] = Field(default_factory=list)


class UpcomingTrends(BaseModel):
    skill_name: str
    year: str
    score: int


class SkillAreaScore(BaseModel):
    skill_area_name: str
    average_score: float
    job_count: Optional[int] = None
    avg_salary: Optional[int] = None

    # ✅ Avoid None → always list
    top_technologies: List[TechnologyScore] = Field(default_factory=list)
    yearly_trends: List[TechnologyYearlyTrend] = Field(default_factory=list)
    countries: List[CountryTechnologyMetrics] = Field(default_factory=list)


class TechJobsCountryDashboard(BaseModel):
    top_technologies: List[TechnologyScore] = Field(default_factory=list)
    skill_areas: List[SkillAreaScore] = Field(default_factory=list)
    upcoming_trends: List[UpcomingTrends] = Field(default_factory=list)

    chart_type: str = "bar"
