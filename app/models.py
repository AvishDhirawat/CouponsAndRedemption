from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    external_id = Column(String(64), unique=True)
    name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    created_at = Column(DateTime, server_default=func.now())

class Coupon(Base):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    code = Column(String(128), unique=True, index=True, nullable=False)
    category = Column(String(64))
    created_at = Column(DateTime, server_default=func.now())
    user = relationship("User")

class Redemption(Base):
    __tablename__ = "redemptions"
    id = Column(Integer, primary_key=True)
    coupon_id = Column(Integer, ForeignKey("coupons.id"))
    redeemed_at = Column(DateTime, server_default=func.now())
    location = Column(String(255))
    operator_id = Column(String(255))

class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True)
    coupon_id = Column(Integer, ForeignKey("coupons.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Integer, nullable=True)
    comments = Column(String(1024), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
