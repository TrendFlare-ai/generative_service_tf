from fastapi import FastAPI
from app.database.repositories.test_repo import test_repo

app = FastAPI()

print(test_repo.db_name)