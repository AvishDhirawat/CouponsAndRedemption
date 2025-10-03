from fastapi import FastAPI
from app.models import Base
from app.deps import engine
from app.routers import redeem

app = FastAPI()

# Create tables at startup if they don't exist
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(redeem.router)

@app.get("/")
def health():
    return {"status": "ok"}
