"""
This module handles application configurations
"""

from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")


TESTING = config("TESTING", cast=bool, default=False)
DEBUG = config("DEBUG", cast=bool, default=False)
LIVE = config("LIVE", cast=bool, default=False)

POSTGRES_USER = config("DATABASE_USER", cast=Secret)
POSTGRES_PASSWORD = config("DATABASE_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("DATABASE_HOST", cast=Secret)
POSTGRES_PORT = config("DATABASE_PORT", cast=Secret)
POSTGRES_DB = config("DATABASE_DB", cast=Secret)
