from fastapi import FastAPI
from routes.route import router as api_router
from routes.auth import router as auth_router

app = FastAPI()


# Include the API routes defined in routes.route module
app.include_router(api_router)


# Include the authentication routes defined in routes.auth module,
# and specify a prefix for these routes
app.include_router(auth_router, prefix="/auth")