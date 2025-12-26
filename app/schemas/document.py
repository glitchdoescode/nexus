from datetime import datetime
from pydantic import BaseModel, ConfigDict

class DocumentBase(BaseModel):
    title:str
    content:str

class DocumentCreate(DocumentBase):
    pass

class DocumentOut(DocumentBase):
    id: int
    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

