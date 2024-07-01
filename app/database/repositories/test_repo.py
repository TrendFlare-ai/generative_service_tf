from app.database.repositories.base_repo import BaseRepository

class TestRepository(BaseRepository):

    def __init__(self,db_name,collection_name):
        super().__init__(db_name,collection_name)

test_repo = TestRepository("trendflare","test")