from fastapi import FastAPI,APIRouter,BackgroundTasks,Request
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List,Dict,Any
from ..config import settings
from pathlib import Path
from ..schemas import EmailSchema

conf = ConnectionConfig(
    MAIL_USERNAME = settings.MAIL_USERNAME,
    MAIL_PASSWORD = settings.MAIL_PASSWORD,
    MAIL_FROM = settings.MAIL_FROM,
    MAIL_PORT = settings.MAIL_PORT,
    MAIL_SERVER = settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS = settings.MAIL_STARTTLS,
    MAIL_SSL_TLS = settings.MAIL_SSL_TLS,
    USE_CREDENTIALS = settings.USE_CREDENTIALS,
    VALIDATE_CERTS = settings.VALIDATE_CERTS,
    TEMPLATE_FOLDER =  './app/templates/',
)

router=APIRouter(
    prefix="/email",
    tags=['Email']
)


@router.post("/")
async def email(request:Request,background:BackgroundTasks) -> JSONResponse:
    email=await request.json()
    message = MessageSchema(
        subject="Welcome to FastAPI",
        recipients=email,
        body="Simple background task",
        # template_body=email.dict().get("body"),
        subtype=MessageType.plain
        )

    fm = FastMail(conf)
    # background.add_task(fm.send_message,message)
    await fm.send_message(message,template_name="email.html")
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
