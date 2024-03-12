from fastapi import FastAPI
from routes.route import router as api_router
from routes.auth import router as auth_router

app = FastAPI()

app.include_router(api_router)
app.include_router(auth_router, prefix="/auth")