from fastapi import FastAPI
from routes.route import router as api_router
from routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



# Define CORS settings
origins = [
    "http://localhost",
    "http://localhost:3000",
      "http://localhost:8000"  # Add the URL of your frontend application
    # Add more origins as needed
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Include the API routes defined in routes.route module
app.include_router(api_router)


# Include the authentication routes defined in routes.auth module,
# and specify a prefix for these routes
app.include_router(auth_router, prefix="/auth")