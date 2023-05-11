import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

API_VERSION = os.getenv("API_VERSION", "0.0.1")

# database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost:5432/api-db-test")
