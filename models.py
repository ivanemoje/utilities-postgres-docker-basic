from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base

# SQLAlchemy model
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Pydantic schema for item creation
class ItemCreate(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True
