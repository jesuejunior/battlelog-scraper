__author__ = 'jesuejunior'
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData
from sqlalchemy import create_engine


engine = create_engine("postgresql+psycopg2://postgres:vivo22@localhost:5432/battlelog")
Metadata = MetaData(bind=engine)
Model = declarative_base(metadata=Metadata)
Session = sessionmaker(bind=engine)

