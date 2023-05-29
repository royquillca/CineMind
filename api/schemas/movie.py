from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import date
import numpy as np

class Movie(BaseModel):
    movie_id: Optional[int] = None
    budget: float = Field(ge=0)
    genres: str = Field(min_length=1, max_length=300)
    homepage: Optional[str] | None = Field(min_length=1)
    original_language: Optional[str] | None = Field(min_length=1, max_length=300)
    overview: Optional[str] | None = Field(min_length=1)
    popularity: float = Field(ge=0)
    production_countries: str = Field(min_length=1)
    release_date: str = Field(min_length=1) # date #
    revenue: float = Field(ge=0)
    runtime: Optional[float] | None = Field(ge=0)
    spoken_languages: str= Field(min_length=1)
    status: Optional[str] | None = Field(min_length=1)
    tagline: Optional[str] | None = Field(min_length=1)
    title: str = Field(min_length=1)
    vote_average: float = Field(ge=0)
    collection_name: Optional[str] | None = Field(min_length=1)
    production_company_name: Optional[str] | None = Field(min_length=1)
    return_on_investment: Optional[float] | None = Field(ge=0)

    class Config:
        schema_extra = {
            "example": {
                    'movie_id': 394645,
                    'budget': 0.0,
                    'genres': 'Thriller',
                    'homepage': None,
                    'original_language': 'nl',
                    'overview': 'The family of the Belgian prime minister is kidnapped. To get them released, he must murder the American president.',
                    'popularity': 1.3048709630966187,
                    'production_countries': 'Belgium',
                    'release_date': '2016-10-26',
                    'revenue': 0.0,
                    'runtime': 115.0,
                    'spoken_languages': 'Nederlands',
                    'status': 'Released',
                    'tagline': None,
                    'title': 'De Premier',
                    'vote_average': 5.199999809265137,
                    'collection_name': None,
                    'production_company_name': 'FBO',
                    'return_on_investment': None
            }
        }