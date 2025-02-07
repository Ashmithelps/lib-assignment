from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Connection URL
MONGO_URI = "database url"
DB_NAME = "e_library"

# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
