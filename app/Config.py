from pydantic_settings import  BaseSettings

class Settings(BaseSettings):
    MONGO_URL: str
    HOST: str
    PORT: int

    class Config:
        env_file = ".env"

settings = Settings()