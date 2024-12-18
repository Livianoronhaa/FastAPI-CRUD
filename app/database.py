# database.py
from pydantic_settings import BaseSettings
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base  # Importação agora do models.py

class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file = ".env"

settings = Settings()

db_user = settings.POSTGRES_USER
db_password = settings.POSTGRES_PASSWORD
db_host = settings.POSTGRES_HOST
db_name = settings.POSTGRES_DB
db_port = settings.DATABASE_PORT

admin_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/postgres"
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_database_if_not_exists():
    try:
        conn = psycopg2.connect(admin_url)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        
        cursor = conn.cursor()
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'")
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f'Banco de dados {db_name} criado com sucesso!')
        else:
            print(f'Banco de dados {db_name} já existe!')
        
    except Exception as e:
        print(f"Erro ao criar banco de dados: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
