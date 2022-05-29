from sqlalchemy import MetaData, Column, text, String, Boolean, Table, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

# create table users
users = Table(
    "users",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True,  server_default=text("uuid_generate_v4()"), unique=True),
    Column("text", String, nullable=False),
    Column("completed", Boolean)
)

# create table foods
foods = Table(
    "foods",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True,  server_default=text("uuid_generate_v4()"), unique=True),
    Column("name", String, nullable=False, unique=True),
    Column("description", String, nullable=False),
    Column("image", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("discount", Float, nullable=True, default=0)
)

# create table orders
orders = Table(
    "orders",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"), unique=True),
    Column("name", String, nullable=False, unique=True),
    Column("description", String, nullable=False),
    Column("total", Float, nullable=False),
    Column('user_id', UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
)

# create table orders
order_details = Table(
    "order_details",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"), unique=True),
    Column('food_id', UUID(as_uuid=True), ForeignKey("foods.id"), nullable=False),
    Column('order_id', UUID(as_uuid=True), ForeignKey("orders.id"), nullable=False)
)

# create table user_action_logs
user_action_logs = Table(
    "user_action_logs",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"), unique=True),
    Column('food_id', UUID(as_uuid=True), ForeignKey("foods.id"), nullable=False),
    Column('order_id', UUID(as_uuid=True), ForeignKey("orders.id"), nullable=False)
)

