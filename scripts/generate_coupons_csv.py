import csv
import os
import uuid
import qrcode

# Config
NUM_PEOPLE = 500
COUPONS_PER_PERSON = 5
OUTPUT_DIR = "generated_coupons"
CSV_FILE = "coupons.csv"

# Ensure output dir exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_coupon_code(person_id, idx):
    # Unique code: UUID-based + person id
    return f"P{person_id}-{uuid.uuid4().hex[:10]}-{idx}"

def generate_qr_code(code, filename):
    img = qrcode.make(code)
    img.save(filename)

def main():
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["PersonID", "CouponCode", "Category", "QRCodeFile"])

        for person_id in range(1, NUM_PEOPLE + 1):
            for idx in range(1, COUPONS_PER_PERSON + 1):
                code = generate_coupon_code(person_id, idx)
                qr_file = os.path.join(OUTPUT_DIR, f"{code}.png")
                generate_qr_code(code, qr_file)
                writer.writerow([person_id, code, "general", qr_file])

    print(f"✅ Generated {NUM_PEOPLE * COUPONS_PER_PERSON} coupons")
    print(f"CSV file: {CSV_FILE}")
    print(f"QR images in: {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
