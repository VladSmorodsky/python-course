from math import ceil
from typing import List, Tuple

from cinema_project.repositories.movie_repository import MovieRepository
from cinema_project.validators.validation import Validation

from cinema_project.exceptions.not_found_error import NotFoundError


class MovieService:
    """
    Service class to manage movies related operations.
    """

    def __init__(self, movie_repository: MovieRepository) -> None:
        self.__validation = Validation()
        self.__movie_repository = movie_repository

    def add_movie(self, title: str, release_year: str, genre: str = '') -> None:
        """
        Add a movie to the database.
        :param release_year:
        :param title:
        :param genre:
        :return:
        """
        self.__validation.is_empty(title)
        self.__validation.is_year(release_year)
        self.__movie_repository.add_movie(title, int(release_year), genre)

    def get_all_movies(self) -> list:
        """
        Get all movies.
        :return:
        """
        movies = self.__movie_repository.find_all()
        if len(movies) == 0:
            raise NotFoundError(f"No movies in database.")
        return movies

    def get_movie_by_id(self, movie_id: int) -> dict:
        """
        Get movie by id.
        :param movie_id:
        :return:
        """
        movie = self.__movie_repository.find_by_id(movie_id)
        if movie is None:
            raise NotFoundError(f"Movie with id {movie_id} not found.")
        return movie

    def get_movie_by_title(self, movie_title: str) -> list:
        """
        Get movie by id.
        :param movie_title:
        :return:
        """
        movie = self.__movie_repository.find_one_by_title(movie_title)
        if movie is None:
            raise NotFoundError(f"Movie with title or key {movie_title} not found.")
        return movie

    def get_movie_genre(self) -> List[str]:
        """
        Get all movies genre.
        :return:
        """
        return [genre[0] for genre in self.__movie_repository.find_all_genres()]

    def get_movies_count_by_genre(self) -> List[Tuple[str, int]]:
        """
        Get movies count by genre.
        :return:
        """
        return self.__movie_repository.get_movie_count_by_genres()

    def search_movies_by_title(self, movie_title: str) -> List[Tuple[str, int]]:
        """
        Get movies by title.
        :param movie_title:
        :return List[Tuple[str, int]]:
        """
        return self.__movie_repository.find_by_title(movie_title)

    def get_total_movies_page(self) -> int:
        """
        Get movies count.
        :return:
        """
        return int(ceil(self.__movie_repository.get_movies_count() / self.__movie_repository.movie_count_by_page))

    def get_paginated_movies(self, page: int = 1) -> List[Tuple[str, int]]:
        """
        Get paginated movies.
        :param page:
        :return:
        """
        return self.__movie_repository.get_movies_by_page(page)
