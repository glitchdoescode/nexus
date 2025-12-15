from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    hashed_password = get_password_hash(user_in.password)

    db_user = User(
        email = user_in.email,
        full_name = user_in.full_name,
        hashed_password = hashed_password
    )

    db.add(db_user)

    await db.commit()
    await db.refresh(db_user)

    return db_user
