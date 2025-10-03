from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from app.deps import get_db, API_KEY, SURVEY_BASE
from app.models import Coupon, Redemption

router = APIRouter()

@router.post("/redeem")
def redeem(code: str, location: str = None, operator_id: str = None,
           x_api_key: str = Header(...), db: Session = Depends(get_db)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    coupon = db.query(Coupon).filter(Coupon.code == code).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")

    try:
        redemption = Redemption(
            coupon_id=coupon.id,
            redeemed_at=datetime.utcnow(),
            location=location,
            operator_id=operator_id
        )
        db.add(redemption)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Coupon already redeemed")

    return {"success": True, "survey_url": f"{SURVEY_BASE}?coupon={coupon.code}"}
