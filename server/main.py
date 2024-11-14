from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from apps.routes.user_router import router as user_router

app = FastAPI()

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)

