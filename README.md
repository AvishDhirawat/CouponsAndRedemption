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

### 📌 Notes
- **docker-compose.yml** — Orchestrates `db` (MySQL) and `api` (FastAPI). Includes healthcheck for MySQL.  
- **.env** — Holds all secrets and connection config (DB credentials, API_KEY, SURVEY_BASE). Must be created locally and *not* committed.  
- **mysql-init/schema.sql** — Database schema (idempotent). Runs automatically on first DB init.  
- **mysql-init/always-init.sh** — Optional per-startup script; keep it lightweight.  
- **app/** — Application code (FastAPI). Runs via `uvicorn app.main:app`.  
- **scripts/** — Helper scripts to generate coupons and QR codes. Run as modules (`python -m scripts.generate_coupons_db`).  


