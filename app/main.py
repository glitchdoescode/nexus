from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database import getdb
from app.api.auth import router as auth_router
from app.api.documents import router as documents_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(documents_router, prefix="/documents", tags=["Documents"])

@app.get("/health")
async def health_check(db: AsyncSession = Depends(getdb)):
    try:
        result = await db.execute(text("SELECT 1"))
        value = result.scalar()

        return {
            "status": "online",
            "message": "Database connected successfully!",
            "db_response": value
        }
    except Exception as e:
        return {
            "status": "offline",
            "error": str(e)
        }

