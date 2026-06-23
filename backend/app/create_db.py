from app.db.base import Base
from app.db.session import engine
from app.db.models.document import Document
from app.db.models.chunk import Chunk
from app.db.models.summary import Summary

Base.metadata.create_all(bind=engine)