from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from src.database import Base

from src.auth.models import User


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String)
    image = Column(String)
    description = Column(String)
    url = Column(String)
    url_orig = Column(String)
    user_rating = Column(Integer)
    owner_id = Column(UUID, ForeignKey(User.id))

    owner = relationship(User, back_populates="items")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class BookRating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, unique=True)
    url_orig = Column(String)
    title = Column(String)
    image = Column(String)
    description = Column(String)
    general_rating = Column(Float)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
