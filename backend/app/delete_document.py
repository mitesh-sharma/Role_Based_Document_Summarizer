from app.db.session import SessionLocal
from app.db.models.document import Document

session = SessionLocal()

session.query(Document).delete()

session.commit()

session.close()