import os
from typing import Any, List

from dotenv import load_dotenv

from database import Database
from cinema_project.repositories.actor_repository import ActorRepository
from cinema_project.repositories.movie_cast_repository import MovieCastRepository
from cinema_project.services.actor_service import ActorService
from cinema_project.services.movie_cast_service import MovieCastService
from cinema_project.repositories.movie_repository import MovieRepository
from cinema_project.services.movie_service import MovieService
from cinema_project.exceptions.not_found_error import NotFoundError
from cinema_project.exceptions.template_mismatch_error import TemplateMismatchError


def create_actor() -> None:
    """
    There is a client code of creating actor.
    :return:
    """
    actor_name = input("Enter actor name:")
    actor_birth_year = int(input("Enter birth year:"))
    actor_service.add_actor(actor_name.strip(), actor_birth_year)


def show_actor_list(actor_list: list[Any]) -> None:
    """
    Show actors list
    :param actor_list:
    :return:
    """
    actor_options = ""
    for actor in actor_list:
        actor_options += f"{actor[0]}. {actor[1]}\n"
    print(actor_options)


def show_movie_list(movie_list: list[Any]) -> None:
    """
    Show movies list
    :param movie_list:
    :return:
    """
    movie_options = ""
    for movie in movie_list:
        movie_options += f"{movie[0]}. {movie[1]}\n"
    print(movie_options)


# Setup and preparing database and infrastructure
load_dotenv()
db_name = os.getenv("DATABASE_NAME")
if db_name is None:
    raise ValueError("DATABASE_NAME environment variable is not set")
database = Database(db_name)
database.create_database()

movie_repository = MovieRepository(database.connection)
actor_repository = ActorRepository(database.connection)
movie_cast_repository = MovieCastRepository(database.connection)

movie_service = MovieService(movie_repository)
actor_service = ActorService(actor_repository)
movie_cast_service = MovieCastService(movie_cast_repository)

try:
    while True:
        menu_list = """
        1. Add movie
        2. Add actor
        3. Add actor to movie
        4. Get movies with actors
        5. Get movies genre
        6. Get movies count by genre 
        7. Search movies by title
        8. Get average actor's age for given genre
        9. Get movies by page
        10. Get movies and actors names
        0. Exit
        """
        print(menu_list)
        number = int(input("Select action using number:"))

        try:
            if number == 0:
                break
            elif number == 1:
                # save movie info
                movie_title = input("Enter movie title:")
                release_date = input("Enter release date:")
                genre = input("Enter genre:")
                movie_service.add_movie(movie_title, release_date, genre)
                print("Movie added.")
                # get movie
                movie = movie_service.get_movie_by_title(movie_title)
                # should cast be added
                is_added_cast = input("Would you like to add cast? (y/n)")
                if is_added_cast.lower() == "y":
                    show_actor_list(actor_service.get_all())
                    # get actors with particular ids
                    actor_ids = input("Select actor ids separated by comma (,):")
                    actors_by_id = actor_service.get_actors_by_ids(
                        tuple([int(id.strip()) for id in actor_ids.split(',')])
                    )
                    # add movie cast
                    movie_cast_list = [(movie[0], actor[0]) for actor in actors_by_id]
                    movie_cast_service.add_movie_cast(movie_cast_list)
                    print("Movie cast created.")
            elif number == 2:
                create_actor()
                print("Actor created.")
            elif number == 3:
                # print movie list
                show_movie_list(movie_service.get_all_movies())
                movie_id = int(input("Select movie id:\n"))
                selected_movie = movie_service.get_movie_by_id(movie_id)
                show_actor_list(actor_service.get_all())
                # get actors with particular ids
                actor_ids = input("Select actor ids separated by comma (,):")
                actors_by_id = actor_service.get_actors_by_ids(
                    tuple([int(id.strip()) for id in actor_ids.split(',')])
                )
                # add movie cast
                movie_cast_list = [(selected_movie[0], actor[0]) for actor in actors_by_id]
                movie_cast_service.add_movie_cast(movie_cast_list)
                print("Movie cast created.")
            elif number == 4:
                # show movies with actors
                movies_with_actors = movie_cast_service.get_movies_with_actors()
                options = 'Movies with actors:'
                for movie_actor in movies_with_actors:
                    options += f"- Movie Name: {movie_actor}, Actors: {', '.join([actor_name for actor_name in movies_with_actors[movie_actor]])}\n"
                print(options)
            elif number == 5:
                # get all movies genres
                print("Movies genre:")
                genre_options = ''
                for genre in movie_service.get_movie_genre():
                    genre_options += f"- {genre[1]}\n"
                print(genre_options)
            elif number == 6:
                # get genre movie's count
                print("Movies genre:")
                movie_genre_list = ''
                for genre_name, movie_count in movie_service.get_movies_count_by_genre():
                    movie_genre_list += f"- {genre_name}: {movie_count}\n"
                print(movie_genre_list)
            elif number == 7:
                # search movie by title or key title
                movie_title = input("Enter a movie title or movie title key:")
                movies = movie_service.search_movies_by_title(movie_title)
                movie_list = 'Search results:\n'
                for movie_title, release_year in movies:
                    movie_list += f"- {movie_title} ({release_year})\n"
                print(movie_list)
            elif number == 8:
                print("Select movies genre id:")
                movie_genre_list = ''
                genre_list: List[str] = movie_service.get_movie_genre()
                for index, genre in enumerate(genre_list):
                    movie_genre_list += f"{index + 1}: {genre}\n"
                print(movie_genre_list)
                movie_genre_id = int(input("Select a movie genre id:"))
                if 1 > movie_genre_id >= len(genre_list):
                    raise ValueError('Provided genre id is incorrect.')
                print("Average actors' age:",
                      movie_cast_service.get_avg_actors_age_in_movie_genre(genre_list[movie_genre_id - 1]))
            elif number == 9:
                while True:
                    print('To return into main menu, enter 0')
                    total_movie_page_count = movie_service.get_total_movies_page()
                    page = int(input(f"Enter page number (from 1 to {total_movie_page_count})):"))
                    if page <= 0:
                        break
                    if page > total_movie_page_count:
                        page = total_movie_page_count
                        print('Provided page number is incorrect. Will use last page')
                    movies = movie_service.get_paginated_movies(page)
                    print(f"Page {page} of {total_movie_page_count}:")
                    movie_list = ''
                    for movie_title, release_year in movies:
                        movie_list += f"- {movie_title} ({release_year})\n"
                    print(movie_list)
            elif number == 10:
                names = movie_cast_service.get_movies_and_actors_names()
                name_options = ''
                for name in names:
                    name_options += f"- {name[0]}\n"
                print(name_options)

        except (ValueError, NotFoundError, TemplateMismatchError) as error:
            print(error)
except Exception:
    exit(1)
