__author__ = 'jesuejunior'
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from sqlalchemy import create_engine

CONN_STRING = "postgresql+psycopg2://postgres:vivo22@localhost:5432/battlelog"

CONN_STRING = os.environ.get("CONN_STRING", "sqlite+pysqlite:///:memory:" )

engine = create_engine(CONN_STRING)
Metadata = MetaData(bind=engine)
Model = declarative_base(metadata=Metadata)
Session = sessionmaker(bind=engine)

