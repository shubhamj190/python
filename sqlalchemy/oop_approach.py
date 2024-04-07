import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base

db = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=db)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    username: Mapped[str]
    email: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"


def main() -> None:
    Base.metadata.create_all(db)
    user1 = User(username="Shubham", email="shubham@gmail.com")
    user2 = User(username="sawant", email="sawant@gmail.com")

    with Session() as session:
        session.add(user1)
        session.add(user2)
        session.commit()
        print(session.query(User).all())


if __name__ == "__main__":
    main()