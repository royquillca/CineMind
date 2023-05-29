from sqlalchemy import func
from models.movie import Movie as MovieModel # Emtidad de la base de datos
from schemas.movie import Movie # Esquema de validacion de los datos
import locale
# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


class MovieService():
    
    def __init__ (self, db) -> None:
        self.db = db
    
    # ------------------------ Movies ------------------------#
    
    def count_production_countries(self, production_country: str) -> dict:
        count = self.db.query(func.count()).filter(func.lower(MovieModel.production_countries) == production_country.lower()).scalar()
        return {
            "pais_produccion": production_country.title(),
            "cantidad": count,
        }

    
    def get_movie_by_id(self, id: int):
        result = self.db.query(MovieModel).filter(MovieModel.movie_id == id).first()
        return result
    
    
    # --------------------- CRUD Movies ----------------------#

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    
    def update_movie_by_id(self, id: int, data: Movie):
        movie_filtered = self.db.query(MovieModel).filter(MovieModel.movie_id == id).first()

        if movie_filtered:
            for field, value in data.dict().items():
                if field != 'movie_id':
                    # setattr() asigna dinámicamente el valor al campo correspondiente en la instancia de movie.
                    # setattr(class_object, attribute_name, attribute_value)
                    setattr(movie_filtered, field, value)
            self.db.commit()
            return True
        else:
            return False

  
    def remove_movie(self, movie_id: int):
        movie_to_remove = self.db.query(MovieModel).filter(MovieModel.movie_id == movie_id).first()
        self.db.delete(movie_to_remove)
        self.db.commit()
        return 
    
    
    # --------------- Proyecto Individual --------------------#
    
    def get_movies_month(self, mes: str) -> dict:
        meses = {
            "enero": "01",
            "febrero": "02",
            "marzo": "03",
            "abril": "04",
            "mayo": "05",
            "junio": "06",
            "julio": "07",
            "agosto": "08",
            "septiembre": "09",
            "octubre": "10",
            "noviembre": "11",
            "diciembre": "12"
        }
        
        numero_mes = meses.get(mes.lower())
        
        # Realiza la consulta de conteo por mes
        count = self.db.query(func.count()).filter(func.strftime("%m", MovieModel.release_date) == numero_mes).scalar()

        return {
            "mes": mes.title(),
            "cantidad": count,
        }
        

    def get_movies_day(self, dia: str) -> dict:
        # Convertir el nombre del día a un número de la semana (0-6)
        days_of_week = {
            "domingo": "0",
            "lunes": "1",
            "martes": "2",
            "miercoles": "3",
            "jueves": "4",
            "viernes": "5",
            "sabado": "6",
        }
        
        day_number = days_of_week.get(dia.lower())

        # Realizar la consulta para obtener el conteo de registros
        count = self.db.query(func.count()).filter(func.strftime("%w", MovieModel.release_date) == day_number).scalar()
        
        return {
            "dia": dia,
            "cantidad": count
        }


    def get_movie_by_franchise(self, franquicia: str):
        # franchise_name_mask = self.db.query(MovieModel).filter(MovieModel.collection_name == franquicia).all()
        
        movie_count = self.db.query(func.count()).filter(func.lower(MovieModel.collection_name) == franquicia.lower()).scalar()
        
        total_revenue = self.db.query(func.sum(MovieModel.revenue)).filter(func.lower(MovieModel.collection_name) == franquicia.lower()).scalar()
        
        avg_revenue = self.db.query(func.avg(MovieModel.revenue)).filter(func.lower(MovieModel.collection_name )== franquicia.lower()).scalar()
        return {
            "franquicia": franquicia.title(),
            # "data": franchise_name_mask,
            "cantidad": movie_count,
            "ganancia_total": total_revenue,
            "ganancia_promedio": avg_revenue
        }
    
    
    def get_movie_by_country(self, pais: str):
        movie_count = self.db.query(func.count()).filter(func.lower(MovieModel.production_countries) == pais.lower()).scalar()
        return {
            "pais": pais.title(),
            "cantidad": movie_count
        }

    
    def get_film_production_company(self, company: str) -> dict:
        total_revenue = self.db.query(func.sum(MovieModel.revenue)).filter(func.lower(MovieModel.production_company_name) == company.lower()).scalar()
        count = self.db.query(func.count()).filter(func.lower(MovieModel.production_company_name) == company.lower()).scalar()
        return {
            "productora": company,
            "ganancia_total": total_revenue,
            "cantidad": count
        }


    def get_movie_return_on_investment(self, movie_title: str) -> dict:
        
        investment = self.db.query(func.sum(MovieModel.budget)).filter(func.lower(MovieModel.title) == movie_title.lower()).scalar()
        
        return_on_investment = self.db.query(func.sum(MovieModel.return_on_investment)).filter(func.lower(MovieModel.title) == movie_title.lower()).scalar()
        
        revenue = self.db.query(func.sum(MovieModel.revenue)).filter(func.lower(MovieModel.title) == movie_title.lower()).scalar()

        year = self.db.query(func.strftime('%Y', func.date(MovieModel.release_date))).filter(func.lower(MovieModel.title) == movie_title.lower()).scalar()
        
        return {
            "pelicula": movie_title.title(),
            "inversion": investment,
            "ganancia": revenue,
            "retorno": return_on_investment,
            "anio": year
        }
