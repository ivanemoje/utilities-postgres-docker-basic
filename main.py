from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Item, ItemCreate
from database import SessionLocal, engine

# Create the database tables
Item.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "pong"}

# Endpoint to create an item
@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Endpoint to get all items
@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items

# Endpoint to get a specific item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
