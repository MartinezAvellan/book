from peewee import Database, Model
from playhouse.shortcuts import dict_to_model

from app.repository.config import get_database_connection, get_database_schema


class BaseModel(Model):
    class Meta:
        database = get_database_connection()
        schema = get_database_schema()

    @classmethod
    def get_database(cls) -> Database:
        return cls._meta.database

    @classmethod
    def from_dict(cls, data):
        return dict_to_model(cls, data)
