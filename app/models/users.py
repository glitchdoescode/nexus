from collections import UserString, defaultdict
from sqlalchemy import Boolean, String, true
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_class import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    
    hashed_password: Mapped[str] = mapped_column(String)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    role: Mapped[str] = mapped_column(String, default="user")

    full_name: Mapped[str] = mapped_column(String, nullable=True)


