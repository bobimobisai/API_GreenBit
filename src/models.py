from sqlalchemy import (
    Table,
    Column,
    Integer,
    BigInteger,
    String,
    Boolean,
    MetaData,
    DateTime,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database import Base


class UserOrm(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    midle_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column(nullable=False)
    date_registr: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(), nullable=False
    )
    subscrip_status: Mapped[bool] = mapped_column(default=False, nullable=False)
    user_is_active: Mapped[bool] = mapped_column(default=True, nullable=False)


meta_data_obj = MetaData()


user_tanble = Table(
    "user",
    meta_data_obj,
    Column("id", BigInteger, primary_key=True),
    Column("first_name", String(length=264), nullable=False),
    Column("midle_name", String(length=264), nullable=True),
    Column("last_name", String(length=264), nullable=False),
    Column("date_registr", DateTime, default=func.now()),
    Column("subscrip_status", Boolean, default=False),
    Column("user_is_active", Boolean, default=True),
)
