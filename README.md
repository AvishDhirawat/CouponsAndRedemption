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


### 2. Build and run containers

From the project root:

```bash
docker-compose up -d --build
```
This will build the FastAPI service, start the MySQL database, and bring up both containers in detached mode.

## 3. 🧪 Testing

1. Open `http://localhost:8000` in your browser.  
   You should see: `{"status": "ok"}`  

2. Generate coupons by running the script inside the API container:  
   `docker exec -it coupons_api python -m scripts.generate_coupons_db`  
   This will insert 2500 coupons into the database.  

3. Check that coupons exist in the database:  
   `docker exec -it mysql mysql -ufestuser -pFestPass123! fest_coupons -e "SELECT id, code FROM coupons LIMIT 5;"`  

4. Redeem a coupon (replace `<code>` with an actual code from the database):  
   In PowerShell:
   $headers = @{ "x-api-key" = "supersecret" }
Invoke-RestMethod -Uri "http://localhost:8000/redeem?code=
   **Linux (curl):**

```bash
curl -X POST "http://localhost:8000/redeem?code=
<code>&location=food_stall&operator_id=staff1"
-H "x-api-key: supersecret"
```

```bash

You should get a response with `"success": true` and a survey URL.
```
6. Try redeeming the same coupon again.  
   The response should say: `"detail": "Coupon already redeemed"`.  

7. Verify that redemption is logged in the database:  
   `docker exec -it mysql mysql -ufestuser -pFestPass123! fest_coupons -e "SELECT * FROM redemptions LIMIT 5;"`  

You should see an entry with the coupon ID, timestamp, and location/operator details.

## 4. Generate QR Codes for Coupons  

   Run the QR generator script inside the API container:  
   `docker exec -it coupons_api python -m scripts.generate_qr_from_db`  

   This will:  
   - Create a `generated_qr/` folder with PNG QR code images for each coupon  
   - Write a `coupon_qr_map.csv` file mapping coupon IDs and codes to their QR image paths  

   These QR codes can be distributed to participants and scanned to redeem coupons.

