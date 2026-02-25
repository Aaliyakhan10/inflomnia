from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PricingRequestIn(BaseModel):
    creator_id: str
    platform: str                    # instagram | youtube | tiktok
    deliverable_type: str            # post | reel | video | story
    follower_count: int
    engagement_rate: float           # e.g. 0.045 = 4.5%
    niche: str                       # fashion | tech | food | fitness | gaming | travel | general
    brand_name: Optional[str] = None
    brand_industry: Optional[str] = None
    offered_price: Optional[float] = None  # brand's offer to evaluate


class PricingResultOut(BaseModel):
    creator_id: str
    platform: str
    deliverable_type: str
    suggested_price_min: float
    suggested_price_max: float
    recommended_price: float
    offered_price: Optional[float] = None
    deal_verdict: Optional[str] = None  # "fair" | "low" | "good" | "great"
    reasoning: str
    confidence: float
    created_at: datetime

    class Config:
        from_attributes = True


class PricingHistoryOut(BaseModel):
    items: list[PricingResultOut]
    total: int
