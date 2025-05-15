from pydantic_settings import BaseSettings

'''to get the database url from the .env file'''
class Settings(BaseSettings):
    DATABASE_HOST: str = "host.docker.internal"  
    DATABASE_PORT: str = "5432"  
    DATABASE_USER: str = "postgres"  
    DATABASE_PASSWORD: str = "password"  
    DATABASE_NAME: str = "postgres"  
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"

    class Config:
        env_file = ".env"

settings = Settings()

