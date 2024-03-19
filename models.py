from sqlalchemy import ForeignKey

from database import Base, intpk, str30, num10_2
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import time, date


class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[intpk]
    name: Mapped[str30]

    books: Mapped[list["Book"]] = relationship(back_populates="genre")


class Author(Base):
    __tablename__ = "author"

    id: Mapped[intpk]
    name: Mapped[str30]

    books: Mapped[list["Book"]] = relationship(back_populates="author")


class Book(Base):
    __tablename__ = "book"

    id: Mapped[intpk]
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"))
    price: Mapped[num10_2]
    quantity: Mapped[int]

    author: Mapped["Author"] = relationship(back_populates="books")
    genre: Mapped["Genre"] = relationship(back_populates="books")


class City(Base):
    __tablename__ = "city"

    id: Mapped[intpk]
    name: Mapped[str30]
    delivery_time: Mapped[time]

    clients: Mapped[list["Client"]] = relationship(back_populates="city")


class Client(Base):
    __tablename__ = "client"

    id: Mapped[intpk]
    name: Mapped[str30]
    email: Mapped[str30]
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))

    city: Mapped["City"] = relationship(back_populates="clients")
    buys: Mapped[list["Buy"]] = relationship(back_populates="client")


class Buy(Base):
    __tablename__ = "buy"

    id: Mapped[intpk]
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))
    wishes: Mapped[str]

    client: Mapped["Client"] = relationship(back_populates="buys")
    buy_books: Mapped[list["BuyBook"]] = relationship(back_populates="buy")


class BuyBook(Base):
    __tablename__ = "buy_book"

    buy_id: Mapped[intpk] = mapped_column(ForeignKey("buy.id"))
    book_id: Mapped[intpk] = mapped_column(ForeignKey("book.id"))
    quantity_ordered: Mapped[int]

    buy: Mapped["Buy"] = relationship(back_populates="buy_books")
    book: Mapped["Book"] = relationship(back_populates="buy_books")


class Step(Base):
    __tablename__ = "step"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str30]

    buy_steps: Mapped[list["BuyStep"]] = relationship(back_populates="step")


class BuyStep(Base):
    __tablename__ = "buy_step"

    buy_id: Mapped[intpk] = mapped_column(ForeignKey("buy.id"))
    step_id: Mapped[intpk] = mapped_column(ForeignKey("step.id"))
    start_date: Mapped[date]
    end_date: Mapped[date]

    buy: Mapped["Buy"] = relationship(back_populates="buy_steps")
    step: Mapped["Step"] = relationship(back_populates="buy_steps")
