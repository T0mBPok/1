from src.database import Base, int_pk
from sqlalchemy.orm import Mapped

class Animal(Base):
    __tablename__ = "animal"
    id: Mapped[int_pk]
    kind: Mapped[str]
    name: Mapped[str]
    age: Mapped[int]