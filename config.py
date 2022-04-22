import os
import psycopg2


class Config(object):
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://admin_db:admin_12345678@localhost:5432/gestor_documental"
    )
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 1,
        "pool_recycle": 10,
        "pool_pre_ping": True,
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
