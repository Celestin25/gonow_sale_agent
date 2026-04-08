from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "GoNow Sales AI Agent"
    class Config:
        env_file = ".env"

settings = Settings()
