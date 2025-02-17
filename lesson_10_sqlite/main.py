import os
from typing import Any

from dotenv import load_dotenv

from database import Database
from src.exceptions.not_found_error import NotFoundError
from src.exceptions.template_mismatch_error import TemplateMismatchError
from src.repositories.actor_repository import ActorRepository
from src.repositories.movie_cast_repository import MovieCastRepository
from src.services.actor_service import ActorService
from src.services.movie_cast_service import MovieCastService
from src.repositories.movie_repository import MovieRepository
from src.services.movie_service import MovieService


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
database = Database(os.getenv("DATABASE_NAME"))
database.create_database()

movie_repository = MovieRepository(database.connection)
actor_repository = ActorRepository(database.connection)
movie_cast_repository = MovieCastRepository(database.connection)

movie_service = MovieService(movie_repository)
actor_service = ActorService(actor_repository)
movie_cast_service = MovieCastService(movie_cast_repository)

while True:
    menu_list = """
    1. Add movie
    2. Add actor
    3. Add actor to movie
    4. Get movies with actors
    5. Get movies genre
    6. Get movies count by genre 
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
            print("Movies genre:")
            genre_list = ''
            for genre in movie_service.get_movie_genre():
                genre_list += f"- {genre}\n"
            print(genre_list)
        elif number == 6:
            print("Movies genre:")
            movie_genre_list = ''
            for genre in movie_service.get_movies_count_by_genre():
                movie_genre_list += f"- {genre[0]}: {genre[1]}\n"
            print(movie_genre_list)
    except (TemplateMismatchError, NotFoundError, ValueError) as error:
        print(error)
