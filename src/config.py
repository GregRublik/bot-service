from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from faststream.rabbit import RabbitBroker


class RabbitSettings(BaseSettings):
    rabbitmq_user: str = Field(json_schema_extra={".env": "RABBITMQ_USER"})
    rabbitmq_password: str = Field(json_schema_extra={".env": "RABBITMQ_PASSWORD"})
    rabbitmq_host: str = Field(json_schema_extra={".env": "RABBITMQ_HOST"})
    rabbitmq_port: int = Field(json_schema_extra={".env": "RABBITMQ_PORT"})

    queue_incoming: str = Field(json_schema_extra={'.env': 'QUEUE_INCOMING'})
    queue_outgoing: str = Field(json_schema_extra={'.env': 'QUEUE_OUTGOING'})

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="RABBITMQ_",
        extra="ignore"
    )


class Settings(BaseSettings):
    token_telegram: str = Field(json_schema_extra={'.env': 'TOKEN_TELEGRAM'})

    rabbitmq: RabbitSettings

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings(
    rabbitmq=RabbitSettings(),
)

bot = Bot(
    token=settings.token_telegram,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
