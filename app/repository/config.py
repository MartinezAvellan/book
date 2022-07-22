from peewee import MySQLDatabase
from app.utils.constants import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, ENV


def get_database_connection(auto_connect=True) -> MySQLDatabase:

    db = MySQLDatabase(
        DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        autoconnect=auto_connect,
        autorollback=True
    )

    return db


def get_database_schema():
    if 'TEST' in ENV:
        return ''
    else:
        return DB_NAME
