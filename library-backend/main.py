from fastapi import FastAPI
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Include the book routes
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "E-Library API is running"}
