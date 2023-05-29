# Python
# from typing import Optional
# from datetime import date
# Pydantic

# from pydantic import BaseModel

# FastAPI
# from fastapi import FastAPI

# SQLAlchemy
from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Movie(Base):
    
    __tablename__ = "movies"
    
    movie_id = Column(Integer, primary_key=True)
    budget = Column(Float, default = None)
    genres = Column(String)
    homepage = Column(String)
    original_language = Column(String)
    overview = Column(String)
    popularity = Column(Float)
    production_countries = Column(String)
    release_date = Column(String) # Column(Date) # 
    revenue = Column(Float)
    runtime = Column(Float)
    spoken_languages = Column(String)
    status = Column(String)
    tagline = Column(String)
    title = Column(String)
    vote_average = Column(Float)
    collection_name = Column(String)
    production_company_name = Column(String)
    return_on_investment = Column(Float)
    
    # __allow_unmapped__ = True