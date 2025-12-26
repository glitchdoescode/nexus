from sqlalchemy.ext.asyncio import AsyncSession
from app.models.document import Document
from app.schemas.document import DocumentCreate

async def create_document(db: AsyncSession, doc_in: DocumentCreate, owner_id: int) -> Document:
    db_doc = Document(
        title=doc_in.title,
        content=doc_in.content,
        owner_id=owner_id
    )

    db.add(db_doc)
    await db.commit()
    await db.refresh(db_doc)
    return db_doc
