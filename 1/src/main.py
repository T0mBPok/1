from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.animal.router import router as animal_router

# app = FastAPI(title="IP_belkin", docs_url=None, redoc_url=None, openapi_url=None)
app = FastAPI(title="IAD")
PORT=9000
HOST = "0.0.0.0"

app.include_router(animal_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run('src.main:app', host = HOST, port=PORT, reload = True)