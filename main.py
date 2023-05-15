
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Import and include the address router
from app.views import router as address_router

app.include_router(address_router, prefix="/addresses", tags=["addresses"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
