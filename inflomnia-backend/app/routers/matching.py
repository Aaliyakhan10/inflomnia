from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.matching import BrandIn, BrandOut, MatchOut, MatchRequestIn
from app.services.matching_service import MatchingService

router = APIRouter(prefix="/api/v1/matching", tags=["Matching"])
_svc = MatchingService()


@router.post("/brands", response_model=BrandOut, summary="Add a brand to the catalogue")
def add_brand(payload: BrandIn, db: Session = Depends(get_db)):
    try:
        return _svc.add_brand(db, **payload.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/brands", response_model=List[BrandOut], summary="List all brands")
def list_brands(db: Session = Depends(get_db)):
    return _svc.get_brands(db)


@router.post("/find-brands", summary="Find best-fit brands for a creator")
def find_brands(payload: MatchRequestIn, db: Session = Depends(get_db)):
    try:
        return _svc.find_matches(
            db=db,
            creator_id=payload.creator_id,
            niche=payload.niche,
            platform=payload.platform,
            follower_count=payload.follower_count,
            engagement_rate=payload.engagement_rate,
            audience_description=payload.audience_description,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/matches/{creator_id}", summary="Get saved brand matches for a creator")
def get_matches(creator_id: str, db: Session = Depends(get_db)):
    return _svc.get_matches(db, creator_id)
