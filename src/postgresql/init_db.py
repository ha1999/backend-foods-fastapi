import databases
import sqlalchemy
from src.config.settings import settings
from src.config.tables import metadata

database = databases.Database(settings.SQLALCHEMY_DATABASE_URI, min_size=1, max_size=5)


def create_all_table() -> None:
    engine = sqlalchemy.create_engine(
        settings.SQLALCHEMY_DATABASE_URI
    )
    print("Starting create database structure...!")
    metadata.create_all(engine)
    print("Completed create database structure!")
