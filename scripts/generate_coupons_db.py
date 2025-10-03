import uuid
from sqlalchemy.orm import Session
from app.deps import SessionLocal
from app.models import Coupon

# Config
NUM_PEOPLE = 500
COUPONS_PER_PERSON = 5

def generate_coupon_code(person_id, idx):
    """
    Create a unique coupon code for a person and index.
    Example: P23-5f9a3bc12e-3
    """
    return f"P{person_id}-{uuid.uuid4().hex[:10]}-{idx}"

def main():
    db: Session = SessionLocal()
    total = NUM_PEOPLE * COUPONS_PER_PERSON

    try:
        for person_id in range(1, NUM_PEOPLE + 1):
            for idx in range(1, COUPONS_PER_PERSON + 1):
                code = generate_coupon_code(person_id, idx)
                coupon = Coupon(code=code, category="general")
                db.add(coupon)

        db.commit()
        print(f"✅ Inserted {total} coupons into DB (category=general).")

    except Exception as e:
        db.rollback()
        print(f"❌ Error inserting coupons: {e}")

    finally:
        db.close()

if __name__ == "__main__":
    main()
