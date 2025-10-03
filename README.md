# Coupons and Redemption System

A containerized Python + FastAPI + MySQL project to manage **fest coupons**.  
Each participant gets unique coupons which can be redeemed once. Redemption is logged and a feedback survey link is returned.

---

## 🚀 Features Implemented (Confirmed Working)

- ✅ **Coupon Generation** (500 people × 5 coupons each = 2500 unique coupons)
- ✅ **MySQL Database** with tables: `users`, `coupons`, `redemptions`, `feedbacks`
- ✅ **FastAPI Service** running on `localhost:8000`
- ✅ **Redeem API** (`/redeem`) with:
  - Validates coupon code
  - Allows one-time use only
  - Logs redemption (time, location, operator)
  - Returns feedback survey link
- ✅ **QR Code Generator Script** to produce PNGs + CSV mapping

---

## 📂 Project Structure

