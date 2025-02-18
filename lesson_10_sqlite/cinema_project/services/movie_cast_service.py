from datetime import datetime
from typing import Tuple, List, Dict

from cinema_project.exceptions.not_found_error import NotFoundError
from cinema_project.repositories.movie_cast_repository import MovieCastRepository


class MovieCastService:
    """
    Service class to manage movie cast related operations.
    """

    def __init__(self, movie_cast_repository: MovieCastRepository):
        self.__movie_cast_repository = movie_cast_repository

    def add_movie_cast(self, movie_cast_list: List[Tuple[int, int]]) -> None:
        """
        Add a movie cast to the database.
        :param movie_cast_list:
        :return:
        """
        self.__movie_cast_repository.add_cast_to_movie(movie_cast_list)

    def get_movies_with_actors(self) -> Dict[str, List[str]]:
        """
        Get movies with actors.
        :return:
        """
        movies_with_actors_dict: Dict[str, List[str]] = {}
        movies_with_actors = self.__movie_cast_repository.get_movies_with_actors()
        for movie_actor in movies_with_actors:
            if movie_actor[0] in movies_with_actors_dict:
                movies_with_actors_dict[movie_actor[0]].append(movie_actor[1])
                continue
            movies_with_actors_dict[movie_actor[0]] = [movie_actor[1]]
        return movies_with_actors_dict

    def get_avg_actors_age_in_movie_genre(self, movie_genre: str) -> int:
        """
        Get average age in movie genre.
        :param movie_genre:
        :return:
        """
        avg_year = self.__movie_cast_repository.get_average_birth_year_for_actors_in_movie_genre(movie_genre)
        if avg_year is None:
            raise NotFoundError(f"There is no actors for genre {movie_genre}")
        return datetime.now().year - int(avg_year)

    def get_movies_and_actors_names(self) -> List[Tuple[str]]:
        """
        Get movies and actors names.
        :return:
        """
        return self.__movie_cast_repository.get_movies_and_actors_names()
