from pydantic import BaseSettings


class Settings(BaseSettings):
    # base_uri:str
    # client_id: str
    # client_secret_key: str
    database_username:str
    database_password:str
    database_hostname:str
    database_port:int
    database_name:str
    class Config:
        env_file = ".env"

settings = Settings()