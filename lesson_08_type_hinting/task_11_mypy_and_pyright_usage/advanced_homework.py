from lesson_08_type_hinting.task_07_typedict_and_protocol.src.storages.in_memory_user_db import InMemoryUserDB
from lesson_08_type_hinting.task_08_callable_and_generics.main import double, to_upper
from lesson_08_type_hinting.task_08_callable_and_generics.processor import Processor
from lesson_08_type_hinting.task_09_final_and_metaclasses.src.repositories.sql_repository import SQLRepository

# Task 7
db = InMemoryUserDB()
db.save_user({"id": 1, "name": "Alice", "is_admin": False})
print(db.get_user(1))  # {"id": 1, "name": "Alice", "is_admin": False}
print(db.get_user(2))  # None

# Task 8
p1 = Processor([1, 2, 3])
print(p1.apply(double))  # [2, 4, 6]

p2 = Processor(["hello", "world"])
print(p2.apply(to_upper))  # ["HELLO", "WORLD"]

# Task 9
repo = SQLRepository()
repo.save({"name": "Product1", "price": 10.5})
