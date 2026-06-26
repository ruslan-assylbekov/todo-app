from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import user_router

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, 
    allow_origins = origins, # allow all origins from above
    allow_credentials=True,
    allow_methods=["*"], # allow all methods
    allow_headers=["*"],
    )

app.include_router(user_router.router)
# app.include_router(auth_router.router)


#uvicorn src.main:app --reload
#.venv\Scripts\activate