from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.pricing import PricingRequestIn, PricingResultOut, PricingHistoryOut
from app.services.pricing_service import PricingService

router = APIRouter(prefix="/api/v1/pricing", tags=["Pricing"])
_svc = PricingService()


@router.post("/estimate", response_model=PricingResultOut, summary="Estimate brand deal price range")
def estimate_price(payload: PricingRequestIn, db: Session = Depends(get_db)):
    try:
        return _svc.estimate_price(
            db=db,
            creator_id=payload.creator_id,
            platform=payload.platform,
            deliverable_type=payload.deliverable_type,
            follower_count=payload.follower_count,
            engagement_rate=payload.engagement_rate,
            niche=payload.niche,
            brand_name=payload.brand_name,
            brand_industry=payload.brand_industry,
            offered_price=payload.offered_price,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{creator_id}", response_model=PricingHistoryOut, summary="Get past pricing estimates")
def get_history(creator_id: str, limit: int = 20, db: Session = Depends(get_db)):
    return _svc.get_history(db, creator_id, limit)
