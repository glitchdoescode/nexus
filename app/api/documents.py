from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pypdf import PdfReader 
from io import BytesIO

from app.core.database import getdb
from app.models.user import User
from app.schemas.document import DocumentCreate, DocumentOut
from app.crud.document import create_document
from app.api.auth import get_current_user

router = APIRouter()

@router.post("/upload", response_model=DocumentOut)
async def upload_document(
        file: UploadFile = File(...),
        db: AsyncSession = Depends(getdb),
        current_user: User = Depends(get_current_user)
):
    if file.content_type!="application/pdf":
        raise HTTPException(400, detail="File must be a pdf")

    content = await file.read()

    try:
        pdf_reader = PdfReader(BytesIO(content))
        text = ""
        for page in pdf_reader.pages:
            text+=page.extract_text() or ""
    except Exception:
        raise HTTPException(400, detail="Could not read PDF File")

    doc_in = DocumentCreate(
        title = file.filename or "Untitled",
        content = text
    )

    return await create_document(db, doc_in, current_user.id)

