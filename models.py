from sqlalchemy import ForeignKey, DECIMAL, Time

from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import time, date


class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    books: Mapped["Book"] = relationship(back_populates="genre")


class Author(Base):
    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    books: Mapped["Book"] = relationship(back_populates="author")


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"))
    price: Mapped[float] = mapped_column(DECIMAL(10, 2))
    quantity: Mapped[int]

    author: Mapped["Author"] = relationship(back_populates="books")
    genre: Mapped["Genre"] = relationship(back_populates="books")


class City(Base):
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    delivery_time: Mapped[time] = mapped_column(Time)

    clients: Mapped["Client"] = relationship(back_populates="city")


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))

    city: Mapped["City"] = relationship(back_populates="clients")
    buys: Mapped["Buy"] = relationship(back_populates="client")


class Buy(Base):
    __tablename__ = "buy"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
    wishes: Mapped[str]

    client: Mapped["Client"] = relationship(back_populates="buys")
    buy_books: Mapped["BuyBook"] = relationship(back_populates="buy")


class BuyBook(Base):
    __tablename__ = "buy_book"

    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.id"), primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"), primary_key=True)
    quantity_ordered: Mapped[int]

    buy: Mapped["Buy"] = relationship(back_populates="buy_books")
    book: Mapped["Book"] = relationship(back_populates="buy_books")


class Step(Base):
    __tablename__ = "step"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    buy_steps: Mapped["BuyStep"] = relationship(back_populates="step")


class BuyStep(Base):
    __tablename__ = "buy_step"

    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.id"), primary_key=True)
    step_id: Mapped[int] = mapped_column(ForeignKey("step.id"), primary_key=True)
    start_date: Mapped[date]
    end_date: Mapped[date]

    buy: Mapped["Buy"] = relationship(back_populates="buy_steps")
    step: Mapped["Step"] = relationship(back_populates="buy_steps")
