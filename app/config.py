from pydantic import BaseSettings


class Settings(BaseSettings):
    database_username:str
    database_password:str
    database_hostname:str
    database_port:int
    database_name:str
    MAIL_USERNAME:str
    MAIL_PASSWORD:str
    MAIL_FROM:str
    MAIL_PORT:int
    MAIL_SERVER:str
    MAIL_FROM_NAME:str
    MAIL_STARTTLS:bool
    MAIL_SSL_TLS:bool
    USE_CREDENTIALS:bool
    VALIDATE_CERTS:bool
    class Config:
        env_file = ".env"

settings = Settings()