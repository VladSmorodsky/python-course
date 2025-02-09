from src.repositories.sql_repository import SQLRepository

repo = SQLRepository()
repo.save({"name": "Product1", "price": 10.5})
