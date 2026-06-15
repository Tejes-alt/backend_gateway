from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes import settings
from routes import search
from routes import users
from routes import analytics

from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-d0rx.onrender.com"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(settings.router)

app.include_router(search.router)

app.include_router(auth_router)

app.include_router(users.router)

app.include_router(analytics.router)

@app.get("/")
def home():

    return {
        "message":
        "Backend Gateway Running"
    }