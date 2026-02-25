from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ScriptRequestIn(BaseModel):
    creator_id: str
    topic: str                       # e.g. "sustainable skincare routine"
    brand_name: Optional[str] = None
    brand_brief: Optional[str] = None  # what the brand wants to highlight
    tone: str = "entertaining"       # educational | entertaining | inspiring


class ScriptSection(BaseModel):
    section: str                     # e.g. "Hook", "Problem", "Solution", "Demo", "CTA"
    content: str
    duration_seconds: Optional[int] = None
    tips: Optional[str] = None


class ScriptOut(BaseModel):
    id: str
    creator_id: str
    brand_name: Optional[str]
    topic: str
    tone: str
    hook: str
    structure: List[ScriptSection]
    cta: str
    tips: List[str]
    reasoning: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
