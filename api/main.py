# Python
from typing import Optional
from models.movie import Movie as MovieModel
from config.database import Base, engine
from schemas.movie import Movie

# Pydantic
# from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path
from routers.movie import movie_router


app = FastAPI(
    title="CineMind API",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Roy Quillca",
        "url": "https://royquillca.github.io/portafolio/",
        "email": "roquidata@gamil.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://mit-license.org/"
    }
)


# Home de la Aplicacion

@app.get("/", tags=["Home"])
def hello():
    return {"Hola"}


# Routers

# Movie Router
app.include_router(movie_router)


# Crear todas las tablas definidas en SQLite
Base.metadata.create_all(bind=engine)



"""
# Request and Response Body

@app.post("/movie/new")
def create_movie(movie_model: MovieModel = Body(...)):
    return movie_model

# Validaciones Query Parameters

@app.get("/movies/details")
def show_movie(
    title: Optional[str] = Query(
        default=None,
        min_length=1,
        max_length=100,
        title="Movie Title", 
        description="This is a description about the each movie. It's between 1 and 100 characters."
        ),
    overview: Optional[str] = Query(
        min_length=1,
        max_length=250,
        title="Overview about the movie",
        description="This an overview about the movie. It give us a summary what is it about the movie."
        ),
    movie_id: int = Query(
        # ...,
        title="Movie Id",
        description="This a movie id. It's required."
        )
    # budget: Optional[],
    # genres: Optional[],
    # homepage: Optional[],
    # movie_id: Optional[],
    # original_language: Optional[],
    # overview: Optional[],
    # popularity: Optional[],
    # production_countries: Optional[],
    # release_date: Optional[],
    # revenue: Optional[],
    # runtime: Optional[],
    # spoken_languages: Optional[],
    # status: Optional[],
    # tagline: Optional[],
    # title: Optional[],
    # vote_average: Optional[],
    # collection_name: Optional[],
    # production_company_name: Optional[],
    # invest_return: Optional[]
):
    return {title: [overview, movie_id]}



@app.get("/movie/{movie_id}")
def show_movie(
    movie_id: int = Path(
        ..., 
        gt=0,
        title="Movie Id",
        description="It's a requiered natural number related to a unique movie."
        )
):
    return {movie_id: "It exists"}


# Validaciones: Request Body
@app.put("/movie/{movie_id}", response_model=Movie)
def update_movie(
    movie_id: int = Path(
        ...,
        gt=0,
        title="Movie Id",
        description="It's a requiered natural number related to a unique movie."
        ),
    movie: MovieModel = Body(
        ...,
        )
    ):
    return movie


"""