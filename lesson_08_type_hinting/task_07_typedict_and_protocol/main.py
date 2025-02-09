from src.storages.in_memory_user_db import InMemoryUserDB

db = InMemoryUserDB()
db.save_user({"id": 1, "name": "Alice", "is_admin": False})
print(db.get_user(1))  # {"id": 1, "name": "Alice", "is_admin": False}
print(db.get_user(2))  # None
