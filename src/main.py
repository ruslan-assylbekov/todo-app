from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import task_router, user_router

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, 
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

app.include_router(user_router.router)
app.include_router(task_router.router)



#uvicorn src.main:app --reload
#.venv\Scripts\activate