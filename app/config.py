from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str
    DATABASE_PORT: int

    class Config:
        env_file = ".env"

# Criando uma instância global de settings
settings = Settings()
